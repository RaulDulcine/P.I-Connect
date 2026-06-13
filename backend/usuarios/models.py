from django.contrib.auth.models import AbstractUser
from django.db import models


class Usuario(AbstractUser):

    class TipoPerfil(models.TextChoices):
        ALUNO          = 'aluno',          'Aluno'
        PROFESSOR      = 'professor',      'Professor'
        ADMINISTRADOR  = 'administrador',  'Administrador'

    tipo_perfil = models.CharField(
        max_length=20,
        choices=TipoPerfil.choices,
        default=TipoPerfil.ALUNO,
        verbose_name='Tipo de Perfil',
    )
    telefone    = models.CharField(max_length=20, blank=True, null=True, verbose_name='Telefone')
    localizacao = models.CharField(max_length=100, blank=True, null=True, verbose_name='Localização', help_text='Ex: Recife, PE')
    biografia   = models.TextField(blank=True, null=True, verbose_name='Biografia')
    foto_url    = models.CharField(max_length=500, blank=True, null=True, verbose_name='URL da Foto')
    setor       = models.CharField(max_length=100, blank=True, null=True, verbose_name='Setor / Departamento', help_text='Usado no perfil do Administrador')

    class Meta:
        db_table            = 'usuario'
        verbose_name        = 'Usuário'
        verbose_name_plural = 'Usuários'
        ordering            = ['first_name', 'last_name']

    def __str__(self):
        nome = self.get_full_name()
        return nome if nome.strip() else self.username
