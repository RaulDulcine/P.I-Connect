# Como rodar o backend PI Connect

## 1. Criar e ativar o ambiente virtual

```bash
# Na pasta backend/
python -m venv venv

# Windows
venv\Scripts\activate
```

## 2. Instalar dependências (Passo 6 da atividade)

```bash
pip install -r requirements.txt
```

## 3. Criar as migrações e aplicar no banco (Passo 3 da atividade)

```bash
python manage.py makemigrations
python manage.py migrate
```

## 4. Criar superusuário para acessar o Admin

```bash
python manage.py createsuperuser
```

## 5. Popular o banco via Shell (Passo 4 da atividade)

```bash
python manage.py shell
```

```python
from usuarios.models import Usuario
from projetos.models import Curso, Aluno, Projeto

# Criar curso
ads = Curso.objects.create(nome='Análise e Desenvolvimento de Sistemas', sigla='ADS')

# Criar usuário aluno
u = Usuario.objects.create_user(
    username='joao.vitor',
    password='senha123',
    first_name='João',
    last_name='Vitor',
    tipo_perfil='aluno'
)

# Criar perfil de aluno
aluno = Aluno.objects.create(usuario=u, curso=ads, matricula='ADS2026001')

# Criar projeto
Projeto.objects.create(
    titulo='Sistema de Gestão Escolar',
    tema='ODS_4',
    tecnologias='React, Node.js, PostgreSQL',
    ano=2026,
    aluno=aluno,
    curso=ads,
    descricao='Sistema web para gestão de atividades escolares.',
)
```

## 6. Iniciar o servidor

```bash
python manage.py runserver
```

Acesse: **http://127.0.0.1:8000/admin/**
