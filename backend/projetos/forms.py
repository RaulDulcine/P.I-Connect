# projetos/forms.py  — Passo 5 da atividade prática

from django import forms
from .models import Avaliacao, Comentario, Projeto


class ProjetoAdminForm(forms.ModelForm):
    """
    Formulário customizado para o Admin do Projeto.
    Aplica validações de negócio e melhora o layout dos campos no painel.
    """

    descricao = forms.CharField(
        widget=forms.Textarea(attrs={'rows': 4, 'cols': 60}),
        required=False,
        help_text='Descreva a motivação, metodologia e impacto esperado do projeto.',
    )

    objetivos = forms.CharField(
        widget=forms.Textarea(attrs={'rows': 4, 'cols': 60,
                                     'placeholder': 'Um objetivo por linha:\nFacilitar a gestão acadêmica...\nMelhorar a comunicação...'}),
        required=False,
        help_text='Um objetivo por linha. Exibido como lista na tela de Avaliações.',
    )

    tecnologias = forms.CharField(
        widget=forms.TextInput(attrs={
            'placeholder': 'Ex: React, Node.js, PostgreSQL',
            'style': 'width: 100%;',
        }),
        required=False,
        help_text='Liste as tecnologias separadas por vírgula.',
    )

    class Meta:
        model  = Projeto
        fields = '__all__'

    # ── Validações de negócio (clean_<campo>) ─────────────────────────────────

    def clean_ano(self):
        ano = self.cleaned_data.get('ano')
        if ano and (ano < 2000 or ano > 2100):
            raise forms.ValidationError('Ano inválido. Informe um valor entre 2000 e 2100.')
        return ano

    def clean_titulo(self):
        titulo = self.cleaned_data.get('titulo', '').strip()
        if len(titulo) < 5:
            raise forms.ValidationError('O título deve ter pelo menos 5 caracteres.')
        return titulo

    def clean(self):
        cleaned = super().clean()
        status  = cleaned.get('status_projeto')
        arquivo = cleaned.get('arquivo')

        # RF05: projeto não pode avançar para avaliação sem arquivo anexado
        if status == Projeto.StatusProjeto.AGUARDANDO_AVALIACAO and not arquivo:
            self.add_error(
                'arquivo',
                'É obrigatório anexar o arquivo antes de enviar para avaliação.',
            )
        return cleaned


class AvaliacaoAdminForm(forms.ModelForm):
    """Formulário da decisão do Professor — tela Avaliações."""

    feedback = forms.CharField(
        widget=forms.Textarea(attrs={'rows': 5, 'cols': 60}),
        help_text='Este feedback será visível para o estudante.',
    )

    class Meta:
        model  = Avaliacao
        fields = '__all__'

    def clean_feedback(self):
        feedback = self.cleaned_data.get('feedback', '').strip()
        if len(feedback) < 20:
            raise forms.ValidationError(
                'O feedback deve ter pelo menos 20 caracteres para orientar o estudante.'
            )
        return feedback

    def clean(self):
        cleaned   = super().clean()
        projeto   = cleaned.get('projeto')
        if projeto and projeto.status_projeto not in (
            Projeto.StatusProjeto.AGUARDANDO_AVALIACAO,
            Projeto.StatusProjeto.PENDENTE,
        ):
            raise forms.ValidationError(
                f'Este projeto já foi avaliado (status atual: '
                f'{projeto.get_status_projeto_display()}).'
            )
        return cleaned


class ComentarioAdminForm(forms.ModelForm):
    """Formulário de comentário no histórico do projeto."""

    conteudo = forms.CharField(
        widget=forms.Textarea(attrs={'rows': 3, 'cols': 60}),
        label='Comentário',
    )

    class Meta:
        model  = Comentario
        fields = '__all__'
