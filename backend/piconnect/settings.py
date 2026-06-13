from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'django-insecure-piconnect-dev-key-troque-em-producao'

DEBUG = True

ALLOWED_HOSTS = ['*']

# ── Apps ─────────────────────────────────────────────────────────────────────
# jazzmin OBRIGATORIAMENTE antes de django.contrib.admin (Passo 6 da atividade)

INSTALLED_APPS = [
    'jazzmin',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # apps do projeto
    'usuarios',
    'projetos',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'piconnect.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'piconnect.wsgi.application'

# ── Banco de Dados (Passo 1 da atividade) ────────────────────────────────────
# SQLite para desenvolvimento — troque por PostgreSQL em produção

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# ── Autenticação ──────────────────────────────────────────────────────────────
# Aponta para o model Usuario customizado (estende AbstractUser)

AUTH_USER_MODEL = 'usuarios.Usuario'

AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

# ── Internacionalização ───────────────────────────────────────────────────────

LANGUAGE_CODE = 'pt-br'
TIME_ZONE     = 'America/Recife'
USE_I18N      = True
USE_TZ        = True

# ── Arquivos estáticos ────────────────────────────────────────────────────────

STATIC_URL  = '/static/'

# Arquivos enviados via FileField (PDFs, ZIPs dos projetos)
MEDIA_URL  = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# ── Jazzmin — Interface visual do Admin (Passo 6 da atividade) ────────────────

JAZZMIN_SETTINGS = {
    # Identidade
    "site_title":   "PI Connect Admin",
    "site_header":  "PI Connect",
    "site_brand":   "PI Connect",
    "site_icon":    None,
    "welcome_sign": "Bem-vindo ao Painel Administrativo",
    "copyright":    "PI Connect — SENAC Pernambuco",

    # Busca global disponível no topo
    "search_model": ["projetos.Projeto", "usuarios.Usuario"],

    # Ícones Font Awesome para cada model
    "icons": {
        "auth":                    "fas fa-shield-alt",
        "usuarios.Usuario":        "fas fa-users",
        "projetos.Curso":          "fas fa-graduation-cap",
        "projetos.Aluno":          "fas fa-user-graduate",
        "projetos.Professor":      "fas fa-chalkboard-teacher",
        "projetos.Projeto":        "fas fa-project-diagram",
        "projetos.Avaliacao":      "fas fa-clipboard-check",
        "projetos.Comentario":     "fas fa-comments",
    },
    "default_icon_parents":  "fas fa-folder",
    "default_icon_children": "fas fa-circle",

    # Ordem dos grupos na sidebar
    "order_with_respect_to": [
        "projetos",
        "usuarios",
        "auth",
    ],

    # Links de acesso rápido no topo
    "topmenu_links": [
        {"name": "Início", "url": "admin:index", "permissions": ["auth.view_user"]},
    ],

    # Formato do formulário de edição (abas horizontais)
    "changeform_format":        "horizontal_tabs",
    "changeform_format_overrides": {
        "projetos.projeto": "collapsible",
    },

    "navigation_expanded": True,
    "hide_apps":   [],
    "hide_models": [],
    "related_modal_active": True,
}

JAZZMIN_UI_TWEAKS = {
    # Tema base — "pulse" tem sidebar roxa, próxima ao Painel Administrativo (#7C3AED)
    "theme":           "pulse",
    "dark_mode_theme": "darkly",

    # Sidebar escura com accent roxo (cor do Painel Admin)
    "sidebar":         "sidebar-dark-primary",
    "brand_colour":    "navbar-primary",
    "accent":          "accent-purple",
    "navbar":          "navbar-white navbar-light",

    "navbar_fixed":  False,
    "sidebar_fixed": False,
    "footer_fixed":  False,
    "layout_boxed":  False,

    "sidebar_nav_compact_style": True,
    "sidebar_nav_flat_style":    False,

    "button_classes": {
        "primary":   "btn-primary",
        "secondary": "btn-outline-secondary",
        "info":      "btn-info",
        "warning":   "btn-warning",
        "danger":    "btn-danger",
        "success":   "btn-success",
    },
}
