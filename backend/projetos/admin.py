from django.contrib import admin, messages
from django.db.models import Count
from django.utils import timezone
from django.utils.html import format_html

from .forms import AvaliacaoAdminForm, ComentarioAdminForm, ProjetoAdminForm
from .models import Aluno, Avaliacao, Comentario, Curso, Professor, Projeto


@admin.action(description='✓ Aprovar projetos selecionados')
def aprovar_projetos(modeladmin, request, queryset):
    count = queryset.exclude(status_projeto=Projeto.StatusProjeto.APROVADO).update(
        status_projeto=Projeto.StatusProjeto.APROVADO,
        visivel_portfolio=True,
        data_avaliacao=timezone.now(),
    )
    modeladmin.message_user(request, f'{count} projeto(s) aprovado(s).', messages.SUCCESS)


@admin.action(description='✗ Rejeitar projetos selecionados')
def rejeitar_projetos(modeladmin, request, queryset):
    count = queryset.exclude(status_projeto=Projeto.StatusProjeto.REJEITADO).update(
        status_projeto=Projeto.StatusProjeto.REJEITADO,
        data_avaliacao=timezone.now(),
    )
    modeladmin.message_user(request, f'{count} projeto(s) rejeitado(s).', messages.WARNING)


@admin.action(description='↩ Reenviar para avaliação')
def reenviar_para_avaliacao(modeladmin, request, queryset):
    count = queryset.filter(
        status_projeto=Projeto.StatusProjeto.PENDENTE
    ).update(status_projeto=Projeto.StatusProjeto.AGUARDANDO_AVALIACAO)
    modeladmin.message_user(request, f'{count} projeto(s) enviado(s) para avaliação.', messages.INFO)


@admin.register(Curso)
class CursoAdmin(admin.ModelAdmin):
    list_display  = ('id', 'sigla', 'nome', 'total_alunos', 'total_projetos', 'ativo')
    list_editable = ('ativo',)
    search_fields = ('nome', 'sigla')
    list_filter   = ('ativo',)

    def get_queryset(self, request):
        return super().get_queryset(request).annotate(
            _total_alunos=Count('alunos', distinct=True),
            _total_projetos=Count('projetos', distinct=True),
        )

    @admin.display(description='Alunos', ordering='_total_alunos')
    def total_alunos(self, obj):
        return obj._total_alunos

    @admin.display(description='Projetos', ordering='_total_projetos')
    def total_projetos(self, obj):
        return obj._total_projetos


@admin.register(Aluno)
class AlunoAdmin(admin.ModelAdmin):
    list_display  = ('id', 'usuario', 'matricula', 'curso', 'semestre_ingresso', 'total_projetos')
    search_fields = ('usuario__first_name', 'usuario__last_name', 'matricula')
    list_filter   = ('curso',)
    autocomplete_fields = ('usuario', 'curso')

    def get_queryset(self, request):
        return super().get_queryset(request).annotate(_total=Count('projetos'))

    @admin.display(description='Projetos', ordering='_total')
    def total_projetos(self, obj):
        return obj._total


@admin.register(Professor)
class ProfessorAdmin(admin.ModelAdmin):
    list_display  = ('id', 'usuario', 'curso', 'titulacao', 'registro_funcional', 'total_orientados')
    search_fields = ('usuario__first_name', 'usuario__last_name', 'registro_funcional')
    list_filter   = ('curso',)
    autocomplete_fields = ('usuario', 'curso')

    def get_queryset(self, request):
        return super().get_queryset(request).annotate(_total=Count('projetos_orientados'))

    @admin.display(description='Orientações', ordering='_total')
    def total_orientados(self, obj):
        return obj._total


class ComentarioInline(admin.TabularInline):
    model           = Comentario
    form            = ComentarioAdminForm
    extra           = 1
    readonly_fields = ('data_criacao',)
    fields          = ('autor', 'conteudo', 'visivel_aluno', 'data_criacao')
    verbose_name_plural = 'Histórico de Comentários'


class AvaliacaoInline(admin.StackedInline):
    model           = Avaliacao
    form            = AvaliacaoAdminForm
    extra           = 0
    readonly_fields = ('data',)
    fields          = ('professor', 'decisao', 'feedback', 'data')
    verbose_name_plural = 'Avaliações do Projeto'


@admin.register(Projeto)
class ProjetoAdmin(admin.ModelAdmin):
    form    = ProjetoAdminForm
    inlines = [ComentarioInline, AvaliacaoInline]
    actions = [aprovar_projetos, rejeitar_projetos, reenviar_para_avaliacao]

    list_display = (
        'id', 'titulo', 'aluno', 'curso', 'tema_badge', 'ano',
        'status_colorido', 'visivel_portfolio', 'visualizacoes', 'data_submissao',
    )
    list_filter         = ('status_projeto', 'curso', 'tema', 'ano', 'visivel_portfolio')
    search_fields       = ('titulo', 'aluno__usuario__first_name', 'aluno__usuario__last_name', 'tecnologias')
    readonly_fields     = ('data_submissao', 'data_atualizacao', 'data_avaliacao', 'visualizacoes')
    list_per_page       = 20
    date_hierarchy      = 'data_submissao'
    list_select_related = ('aluno__usuario', 'curso', 'professor__usuario')

    fieldsets = (
        ('Identificação do Projeto', {
            'fields': ('titulo', 'descricao', 'objetivos', 'tema', 'tecnologias', 'ano'),
        }),
        ('Responsáveis', {
            'fields': ('aluno', 'professor', 'curso'),
        }),
        ('Status e Entrega', {
            'fields': ('status_projeto', 'arquivo'),
        }),
        ('Portfólio / Explorar', {
            'fields': ('visivel_portfolio', 'visualizacoes'),
        }),
        ('Datas', {
            'fields': ('data_submissao', 'data_atualizacao', 'data_avaliacao'),
            'classes': ('collapse',),
        }),
    )

    @admin.display(description='Tema', ordering='tema')
    def tema_badge(self, obj):
        cores = {
            'ODS_4':   '#3b82f6', 'ODS_7':   '#22c55e',
            'ODS_10':  '#8b5cf6', 'ODS_11':  '#06b6d4',
            'ODS_12':  '#f59e0b', 'ODS_13':  '#ef4444',
            'ESG_AMB': '#16a34a', 'ESG_SOC': '#0ea5e9',
            'ESG_GOV': '#7c3aed',
        }
        cor = cores.get(obj.tema, '#6b7280')
        return format_html(
            '<span style="background:{};color:#fff;padding:2px 8px;'
            'border-radius:12px;font-size:11px;white-space:nowrap">{}</span>',
            cor, obj.get_tema_display(),
        )

    @admin.display(description='Status', ordering='status_projeto')
    def status_colorido(self, obj):
        cores = {
            Projeto.StatusProjeto.APROVADO:             ('#dcfce7', '#16a34a'),
            Projeto.StatusProjeto.PENDENTE:             ('#fef9c3', '#854d0e'),
            Projeto.StatusProjeto.AGUARDANDO_AVALIACAO: ('#ffedd5', '#c2410c'),
            Projeto.StatusProjeto.REJEITADO:            ('#fee2e2', '#dc2626'),
        }
        bg, fg = cores.get(obj.status_projeto, ('#f3f4f6', '#374151'))
        return format_html(
            '<span style="background:{};color:{};padding:2px 10px;'
            'border-radius:12px;font-size:11px;font-weight:600">{}</span>',
            bg, fg, obj.get_status_projeto_display(),
        )


@admin.register(Comentario)
class ComentarioAdmin(admin.ModelAdmin):
    form            = ComentarioAdminForm
    list_display    = ('id', 'projeto', 'autor', 'conteudo_resumo', 'visivel_aluno', 'data_criacao')
    list_filter     = ('visivel_aluno', 'data_criacao')
    search_fields   = ('projeto__titulo', 'autor__first_name', 'autor__last_name', 'conteudo')
    readonly_fields = ('data_criacao',)
    date_hierarchy  = 'data_criacao'
    list_select_related = ('projeto', 'autor')

    @admin.display(description='Comentário')
    def conteudo_resumo(self, obj):
        return obj.conteudo[:80] + '…' if len(obj.conteudo) > 80 else obj.conteudo


@admin.register(Avaliacao)
class AvaliacaoAdmin(admin.ModelAdmin):
    form            = AvaliacaoAdminForm
    list_display    = ('id', 'projeto', 'professor', 'decisao_badge', 'feedback_resumo', 'data')
    list_filter     = ('decisao', 'data', 'professor')
    search_fields   = ('projeto__titulo', 'professor__usuario__first_name', 'feedback')
    readonly_fields = ('data',)
    date_hierarchy  = 'data'
    list_select_related = ('projeto', 'professor__usuario')

    fieldsets = (
        ('Projeto Avaliado', {'fields': ('projeto', 'professor')}),
        ('Decisão',          {'fields': ('decisao', 'feedback')}),
        ('Registro',         {'fields': ('data',), 'classes': ('collapse',)}),
    )

    @admin.display(description='Decisão', ordering='decisao')
    def decisao_badge(self, obj):
        if obj.decisao == Avaliacao.Decisao.APROVADO:
            return format_html(
                '<span style="background:#dcfce7;color:#16a34a;padding:2px 10px;'
                'border-radius:12px;font-size:11px;font-weight:600">✓ Aprovado</span>'
            )
        return format_html(
            '<span style="background:#ffedd5;color:#c2410c;padding:2px 10px;'
            'border-radius:12px;font-size:11px;font-weight:600">↩ Revisão</span>'
        )

    @admin.display(description='Feedback')
    def feedback_resumo(self, obj):
        return obj.feedback[:70] + '…' if len(obj.feedback) > 70 else obj.feedback
