from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator
from django.utils import timezone


class Curso(models.Model):
    nome  = models.CharField(max_length=150)
    sigla = models.CharField(max_length=20, unique=True)
    ativo = models.BooleanField(default=True)

    class Meta:
        db_table = 'curso'
        verbose_name = 'Curso'
        verbose_name_plural = 'Cursos'
        ordering = ['nome']

    def __str__(self):
        return self.sigla


class Aluno(models.Model):
    usuario = models.OneToOneField(
        'usuarios.Usuario',
        on_delete=models.CASCADE,
        related_name='perfil_aluno',
    )
    curso = models.ForeignKey(
        Curso,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='alunos',
    )
    matricula = models.CharField(max_length=20, unique=True, null=True, blank=True)
    semestre_ingresso = models.PositiveSmallIntegerField(
        null=True, blank=True,
        validators=[MinValueValidator(2000), MaxValueValidator(2100)],
    )

    class Meta:
        db_table = 'aluno'
        verbose_name = 'Aluno'
        verbose_name_plural = 'Alunos'

    def __str__(self):
        return f'{self.usuario.get_full_name()} ({self.matricula})'


class Professor(models.Model):
    usuario = models.OneToOneField(
        'usuarios.Usuario',
        on_delete=models.CASCADE,
        related_name='perfil_professor',
    )
    curso = models.ForeignKey(
        Curso,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='professores',
        verbose_name='Curso / Departamento',
    )
    titulacao = models.CharField(max_length=100, blank=True, null=True)
    registro_funcional = models.CharField(max_length=30, blank=True, null=True)

    class Meta:
        db_table = 'professor'
        verbose_name = 'Professor'
        verbose_name_plural = 'Professores'

    def __str__(self):
        return f'Prof. {self.usuario.get_full_name()}'


class ProjetoQuerySet(models.QuerySet):

    def visiveis(self):
        return self.filter(visivel_portfolio=True)

    def aprovados(self):
        return self.filter(status_projeto=Projeto.StatusProjeto.APROVADO)

    def do_aluno(self, aluno):
        return self.filter(aluno=aluno)

    def para_portfolio(self, aluno):
        return self.filter(aluno=aluno, visivel_portfolio=True)

    def por_curso(self, curso_id):
        return self.filter(curso_id=curso_id)

    def por_tema(self, tema):
        return self.filter(tema=tema)

    def por_ano(self, ano):
        return self.filter(ano=ano)

    def busca(self, termo):
        return self.filter(
            models.Q(titulo__icontains=termo)
            | models.Q(tecnologias__icontains=termo)
            | models.Q(aluno__usuario__first_name__icontains=termo)
            | models.Q(aluno__usuario__last_name__icontains=termo)
        )


class Projeto(models.Model):

    class StatusProjeto(models.TextChoices):
        PENDENTE             = 'pendente',             'Pendente'
        AGUARDANDO_AVALIACAO = 'aguardando_avaliacao', 'Aguardando Avaliação'
        APROVADO             = 'aprovado',             'Aprovado'
        REJEITADO            = 'rejeitado',            'Rejeitado'

    class TemaProjeto(models.TextChoices):
        ODS_4          = 'ODS_4',   'ODS 4 - Educação de Qualidade'
        ODS_7          = 'ODS_7',   'ODS 7 - Energia Limpa'
        ODS_10         = 'ODS_10',  'ODS 10 - Redução de Desigualdades'
        ODS_11         = 'ODS_11',  'ODS 11 - Cidades Sustentáveis'
        ODS_12         = 'ODS_12',  'ODS 12 - Consumo Responsável'
        ODS_13         = 'ODS_13',  'ODS 13 - Ação Contra a Mudança Global do Clima'
        ESG_AMBIENTAL  = 'ESG_AMB', 'ESG - Ambiental'
        ESG_SOCIAL     = 'ESG_SOC', 'ESG - Social'
        ESG_GOVERNANCA = 'ESG_GOV', 'ESG - Governança'

    objects = ProjetoQuerySet.as_manager()

    titulo      = models.CharField(max_length=255, verbose_name='Título do Projeto')
    descricao   = models.TextField(blank=True, null=True)
    objetivos   = models.TextField(blank=True, null=True, help_text='Um objetivo por linha.')
    tema        = models.CharField(max_length=10, choices=TemaProjeto.choices, verbose_name='Tema (ESG/ODS)')
    tecnologias = models.CharField(max_length=500, blank=True, null=True, verbose_name='Tecnologias')
    ano         = models.PositiveSmallIntegerField(
        validators=[MinValueValidator(2000), MaxValueValidator(2100)],
    )

    aluno = models.ForeignKey(
        Aluno,
        on_delete=models.RESTRICT,
        related_name='projetos',
    )
    professor = models.ForeignKey(
        Professor,
        on_delete=models.SET_NULL,
        null=True,
        blank=True,
        related_name='projetos_orientados',
        verbose_name='Professor Orientador',
    )
    curso = models.ForeignKey(
        Curso,
        on_delete=models.RESTRICT,
        related_name='projetos',
    )

    status_projeto = models.CharField(
        max_length=25,
        choices=StatusProjeto.choices,
        default=StatusProjeto.PENDENTE,
        verbose_name='Status',
        db_index=True,
    )

    arquivo = models.FileField(
        upload_to='projetos/arquivos/%Y/%m/',
        blank=True,
        null=True,
        verbose_name='Arquivo (PDF / ZIP)',
    )

    visivel_portfolio = models.BooleanField(default=False, verbose_name='Visível no Portfólio')
    visualizacoes     = models.PositiveIntegerField(default=0)

    data_submissao   = models.DateTimeField(auto_now_add=True, db_index=True)
    data_atualizacao = models.DateTimeField(auto_now=True)
    data_avaliacao   = models.DateTimeField(null=True, blank=True)

    class Meta:
        db_table = 'projeto'
        verbose_name = 'Projeto'
        verbose_name_plural = 'Projetos'
        ordering = ['-data_submissao']
        indexes = [
            models.Index(fields=['status_projeto', 'curso'], name='idx_projeto_status_curso'),
            models.Index(fields=['aluno', 'status_projeto'],  name='idx_projeto_aluno_status'),
            models.Index(fields=['visivel_portfolio', '-visualizacoes'], name='idx_projeto_explorar'),
        ]

    def __str__(self):
        return f'{self.titulo} ({self.get_status_projeto_display()})'

    def save(self, *args, **kwargs):
        STATUS_FINAIS = {self.StatusProjeto.APROVADO, self.StatusProjeto.REJEITADO}

        if self.pk:
            anterior = Projeto.objects.filter(pk=self.pk).values('status_projeto').first()
            if anterior:
                era_nao_final = anterior['status_projeto'] not in STATUS_FINAIS
                agora_final   = self.status_projeto in STATUS_FINAIS

                if era_nao_final and agora_final:
                    if not self.data_avaliacao:
                        self.data_avaliacao = timezone.now()
                    if self.status_projeto == self.StatusProjeto.APROVADO:
                        self.visivel_portfolio = True

        super().save(*args, **kwargs)

    @property
    def status_badge_css(self):
        mapa = {
            self.StatusProjeto.APROVADO:             'badge-green',
            self.StatusProjeto.PENDENTE:             'badge-orange',
            self.StatusProjeto.AGUARDANDO_AVALIACAO: 'badge-orange',
            self.StatusProjeto.REJEITADO:            'badge-red',
        }
        return mapa.get(self.status_projeto, 'badge-gray')

    @property
    def tecnologias_lista(self):
        if not self.tecnologias:
            return []
        return [t.strip() for t in self.tecnologias.split(',') if t.strip()]

    @property
    def tecnologias_preview(self):
        techs  = self.tecnologias_lista
        extras = max(0, len(techs) - 2)
        return techs[:2], extras

    @property
    def autor_nome(self):
        return self.aluno.usuario.get_full_name()

    @property
    def data_submissao_br(self):
        return self.data_submissao.strftime('%d/%m/%Y') if self.data_submissao else ''

    @property
    def is_aprovado(self):
        return self.status_projeto == self.StatusProjeto.APROVADO


class Comentario(models.Model):

    projeto = models.ForeignKey(
        Projeto,
        on_delete=models.CASCADE,
        related_name='comentarios',
    )
    autor = models.ForeignKey(
        'usuarios.Usuario',
        on_delete=models.CASCADE,
        related_name='comentarios',
    )
    conteudo      = models.TextField(verbose_name='Comentário')
    data_criacao  = models.DateTimeField(auto_now_add=True, db_index=True)
    visivel_aluno = models.BooleanField(default=True, verbose_name='Visível para o Aluno')

    class Meta:
        db_table = 'comentario'
        verbose_name = 'Comentário'
        verbose_name_plural = 'Comentários'
        ordering = ['data_criacao']

    def __str__(self):
        return f'{self.autor} → {self.projeto.titulo[:40]} ({self.data_criacao:%d/%m/%Y})'

    @property
    def data_br(self):
        return self.data_criacao.strftime('%d/%m/%Y')


class Avaliacao(models.Model):
    """Decisão formal do professor sobre um projeto integrador."""

    class Decisao(models.TextChoices):
        APROVADO          = 'aprovado',          'Aprovar Projeto'
        SOLICITAR_REVISAO = 'solicitar_revisao', 'Solicitar Revisão'

    projeto = models.ForeignKey(
        Projeto,
        on_delete=models.CASCADE,
        related_name='avaliacoes',
    )
    professor = models.ForeignKey(
        Professor,
        on_delete=models.CASCADE,
        related_name='avaliacoes_realizadas',
    )
    decisao  = models.CharField(max_length=20, choices=Decisao.choices, verbose_name='Decisão')
    feedback = models.TextField(verbose_name='Feedback')
    data     = models.DateTimeField(auto_now_add=True, db_index=True)

    class Meta:
        db_table = 'avaliacao'
        verbose_name = 'Avaliação'
        verbose_name_plural = 'Avaliações'
        ordering = ['-data']

    def __str__(self):
        return f'{self.get_decisao_display()} — {self.projeto.titulo[:50]}'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        # atualiza status do projeto sem re-disparar Projeto.save()
        aprovado = self.decisao == self.Decisao.APROVADO
        Projeto.objects.filter(pk=self.projeto_id).update(
            status_projeto=(
                Projeto.StatusProjeto.APROVADO
                if aprovado
                else Projeto.StatusProjeto.REJEITADO
            ),
            data_avaliacao=self.data,
            visivel_portfolio=aprovado,
        )
