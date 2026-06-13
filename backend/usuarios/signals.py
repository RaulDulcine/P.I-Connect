from django.db.models.signals import post_save
from django.dispatch import receiver

from .models import Usuario


@receiver(post_save, sender=Usuario)
def criar_perfil_automatico(sender, instance, created, **kwargs):
    if not created:
        return

    from projetos.models import Aluno, Professor

    if instance.tipo_perfil == Usuario.TipoPerfil.ALUNO:
        Aluno.objects.get_or_create(usuario=instance)
    elif instance.tipo_perfil == Usuario.TipoPerfil.PROFESSOR:
        Professor.objects.get_or_create(usuario=instance)
