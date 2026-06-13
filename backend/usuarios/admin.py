from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from django.db.models import Count
from django.utils.html import format_html

from .models import Usuario


@admin.register(Usuario)
class UsuarioAdmin(UserAdmin):

    list_display  = (
        'avatar_iniciais',
        'get_full_name',
        'email',
        'funcao_badge',
        'curso_display',
        'projetos_count',
        'is_active',
    )
    list_filter   = ('tipo_perfil', 'is_active', 'is_staff')
    search_fields = ('username', 'first_name', 'last_name', 'email')
    ordering      = ('first_name', 'last_name')
    list_per_page = 20
    list_select_related = True

    fieldsets = UserAdmin.fieldsets + (
        ('Perfil PI Connect', {
            'fields': ('tipo_perfil', 'telefone', 'localizacao', 'biografia', 'setor', 'foto_url'),
        }),
    )
    add_fieldsets = UserAdmin.add_fieldsets + (
        ('Perfil PI Connect', {
            'fields': ('first_name', 'last_name', 'email', 'tipo_perfil'),
        }),
    )

    def get_queryset(self, request):
        qs = super().get_queryset(request)
        return qs.annotate(_projetos_count=Count('perfil_aluno__projetos', distinct=True))

    CORES_AVATAR = [
        '#6366f1', '#8b5cf6', '#ec4899', '#14b8a6',
        '#f59e0b', '#22c55e', '#3b82f6', '#ef4444',
    ]

    @admin.display(description='')
    def avatar_iniciais(self, obj):
        nome = obj.get_full_name() or obj.username
        iniciais = ''.join(p[0].upper() for p in nome.split()[:2])
        cor = self.CORES_AVATAR[obj.pk % len(self.CORES_AVATAR)]
        return format_html(
            '<span style="display:inline-flex;align-items:center;justify-content:center;'
            'width:32px;height:32px;border-radius:50%;background:{};color:#fff;'
            'font-size:12px;font-weight:700">{}</span>',
            cor, iniciais,
        )

    @admin.display(description='Função', ordering='tipo_perfil')
    def funcao_badge(self, obj):
        cores = {
            Usuario.TipoPerfil.ALUNO:        ('#ede9fe', '#6d28d9', 'Estudante'),
            Usuario.TipoPerfil.PROFESSOR:     ('#ffedd5', '#c2410c', 'Professor'),
            Usuario.TipoPerfil.ADMINISTRADOR: ('#dbeafe', '#1d4ed8', 'Administrador'),
        }
        bg, fg, label = cores.get(obj.tipo_perfil, ('#f3f4f6', '#374151', obj.tipo_perfil))
        return format_html(
            '<span style="background:{};color:{};padding:2px 10px;'
            'border-radius:12px;font-size:11px;font-weight:600">{}</span>',
            bg, fg, label,
        )

    @admin.display(description='Curso')
    def curso_display(self, obj):
        if hasattr(obj, 'perfil_aluno') and obj.perfil_aluno.curso:
            return obj.perfil_aluno.curso.sigla
        if hasattr(obj, 'perfil_professor') and obj.perfil_professor.curso:
            return obj.perfil_professor.curso.sigla
        return format_html('<span style="color:#aaa">—</span>')

    @admin.display(description='Projetos', ordering='_projetos_count')
    def projetos_count(self, obj):
        return obj._projetos_count
