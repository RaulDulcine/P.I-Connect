# 🎓 PI Connect: Digital Repository & Observatory of Integrative Projects

> A web platform for publishing, discovering, and evaluating the Integrative Projects (PIs) developed by Senac students. Built as a Capstone Project (*Projeto Integrador*) for the **Systems Analysis and Development Program** at **Faculdade Senac Pernambuco**.

[![Senac](https://img.shields.io/badge/Institution-Senac%20Pernambuco-blue)](https://www.pe.senac.br/)
[![Status](https://img.shields.io/badge/status-In%20Development-yellow)]()

---

## 📋 Project Overview

**PI Connect** is a digital ecosystem built to amplify the visibility of Integrative Projects produced by Senac students. The platform works as an academic repository/observatory where students publish their work, professors review and provide feedback, and partner companies discover talent and innovative solutions aligned with the UN Sustainable Development Goals (SDGs).

The project was born from a real, data-driven need identified among students: **73% reported moderate to high difficulty** finding previous PIs to use as reference, and **100% considered project upload and technology-based filtering as essential features**.

### Key Features

* **PI Repository:** Publish and search Integrative Projects with filters by course, year, theme and technologies used.
* **Academic Portfolio:** Each student has a public profile showcasing their technical skills, academic background, and project showcase — a digital portfolio for the job market.
* **Professor Panel:** Dedicated interface for project evaluation, sending technical feedback, and tracking team progress.
* **Admin Dashboard:** Centralized management of users and projects, plus institutional reporting with class performance metrics.

---

## 🖥️ Screenshots

### Login Screen
![Login Screen](P.I%20Connect/screenshots/Tela%20Login%20-%20Aluno.png)

---

### 🎓 Student Panel

| Dashboard | My Projects |
|---|---|
| ![Student Dashboard](P.I%20Connect/screenshots/DashBoard%20Aluno.png) | ![My Projects](P.I%20Connect/screenshots/Meus%20Projetos.png) |

| Academic Portfolio | Profile Settings |
|---|---|
| ![Academic Portfolio](P.I%20Connect/screenshots/Portfolio%20Academico.png) | ![Profile Settings](P.I%20Connect/screenshots/Perfil%20Aluno.png) |

---

### 👨‍🏫 Professor Panel

| Dashboard | Supervised Projects |
|---|---|
| ![Professor Dashboard](P.I%20Connect/screenshots/Dashboard%20Professor.png) | ![Supervised Projects](P.I%20Connect/screenshots/Projetos%20Supervisionados.png) |

| Project Evaluation |
|---|
| ![Project Evaluation](P.I%20Connect/screenshots/Sistema%20de%20Gestão%20Escolar.png) |

---

### 🔧 Admin Panel

| Dashboard | User Management |
|---|---|
| ![Admin Dashboard](P.I%20Connect/screenshots/Dashboard%20Administrativo.png) | ![User Management](P.I%20Connect/screenshots/Gestao%20de%20Usuarios.png) |

| Project Management | Reports & Statistics |
|---|---|
| ![Project Management](P.I%20Connect/screenshots/Gestao%20de%20Projetos.png) | ![Reports](P.I%20Connect/screenshots/Relatorios%20e%20Estatisticas.png) |

---

## 👥 User Profiles

The platform operates with three distinct access levels:

| Profile | Platform Responsibilities |
|---|---|
| **Student** | Submit, edit, and track PIs; maintain a public academic portfolio |
| **Professor** | Evaluate projects, provide feedback, and supervise teams |
| **Administrator** | Manage users, moderate content, and generate institutional reports |

---

## 🛠️ Tech Stack

* **Frontend:** HTML5, CSS3, JavaScript
* **Backend:** Python, Django 4.2
* **Database:** SQLite (development) via Django ORM
* **Admin Interface:** Django Jazzmin
* **Authentication:** Django's built-in authentication system with profile-based access control
* **Report Generation:** python-docx
* **UI/UX Design:** Figma
* **Project Management:** Trello

---

## 📁 Project Structure

```
PI Connect/
├── backend/                  ← Django (database, admin, API)
│   ├── manage.py
│   ├── requirements.txt
│   ├── piconnect/            ← project settings and URLs
│   ├── usuarios/             ← custom user model (Student, Professor, Admin)
│   ├── projetos/             ← models: Course, Project, Evaluation, Comment
│   └── gerar_relatorio.py    ← database schema report generator (.docx)
├── Aluno/                    ← student panel (HTML + CSS + JS)
├── administrador/            ← admin panel (HTML + CSS + JS)
├── Telas do Professor/       ← professor panel (HTML + CSS + JS)
└── index.html                ← login screen
```

---

## ⚙️ Getting Started (Local Development)

### Prerequisites

- [Python 3.10+](https://www.python.org/downloads/)
- [VS Code](https://code.visualstudio.com/) with the **Live Server** extension

> No database setup required — the project uses SQLite, which is bundled with Python.

---

### 1. Set up the Backend

All commands below must be run inside the `backend/` folder.

**Open the terminal in the right folder:**
```bash
cd backend
```

**Create and activate the virtual environment:**
```bash
python -m venv venv
venv\Scripts\activate        # Windows
```

The terminal prompt should now start with `(venv)`.

**Install dependencies:**
```bash
pip install -r requirements.txt
```

**Apply database migrations:**
```bash
python manage.py migrate
```

**Create the admin superuser:**
```bash
python manage.py createsuperuser
```

When prompted, enter:
- **Username:** `admin`
- **Email:** *(leave blank)*
- **Password:** `admin123`

---

### 2. Create Test Data

Open the Django shell:
```bash
python manage.py shell
```

Paste the following and press Enter:
```python
from projetos.models import Curso
from usuarios.models import Usuario

ads = Curso.objects.create(nome='Análise e Desenvolvimento de Sistemas', sigla='ADS')
jd  = Curso.objects.create(nome='Jogos Digitais', sigla='JD')

aluno = Usuario.objects.create_user(
    username='aluno01', password='senha123',
    first_name='João', last_name='Vitor',
    email='joao@senac.br', tipo_perfil='aluno'
)
aluno.perfil_aluno.curso = ads
aluno.perfil_aluno.matricula = '2024001'
aluno.perfil_aluno.save()

prof = Usuario.objects.create_user(
    username='prof01', password='senha123',
    first_name='Carlos', last_name='Mendes',
    email='carlos@senac.br', tipo_perfil='professor'
)
prof.perfil_professor.curso = ads
prof.perfil_professor.titulacao = 'Mestre'
prof.perfil_professor.save()

exit()
```

---

### 3. Start the Django Server

With `(venv)` active inside the `backend/` folder:
```bash
python manage.py runserver
```

The terminal should show:
```
Starting development server at http://127.0.0.1:8000/
```

Keep this terminal open while using the system.

**Django Admin Panel** — `http://localhost:8000/admin/`
Login with the superuser created above.

---

### 4. Open the Frontend

The frontend consists of static HTML files and must be opened via **Live Server** — not by double-clicking the files.

> Opening HTML files directly (via `file:///`) blocks communication with the Django backend.

In VS Code:
1. Open `index.html` (project root)
2. Click **Go Live** in the bottom-right corner
3. The browser opens at `http://127.0.0.1:5500/`

**Login credentials:**

| Profile | Username | Password |
|---|---|---|
| Administrator | `admin` | `admin123` |
| Student | `aluno01` | `senha123` |
| Professor | `prof01` | `senha123` |

> The login screen currently redirects to panels with sample (mock) data. Full backend integration is listed under Future Improvements.

---

### 5. Development Login Shortcut

To test backend features without a full login flow, add the following to `piconnect/urls.py`:

```python
if settings.DEBUG:
    from django.contrib.auth import login as auth_login
    from django.shortcuts import redirect
    from usuarios.models import Usuario

    def dev_login(request, tipo):
        u = Usuario.objects.filter(tipo_perfil=tipo).first()
        if u:
            u.backend = 'django.contrib.auth.backends.ModelBackend'
            auth_login(request, u)
        return redirect('/admin/')

    urlpatterns += [path('dev/login/<str:tipo>/', dev_login)]
```

Then access:
- `http://localhost:8000/dev/login/aluno/`
- `http://localhost:8000/dev/login/professor/`
- `http://localhost:8000/dev/login/administrador/`

This shortcut only works when `DEBUG = True` and should never be deployed to production.

---

## ✅ Non-Functional Requirements

| Category | Requirement | Description |
|---|---|---|
| **Security** | Data Encryption | All user passwords stored as hashed values in the database |
| **Usability** | Responsive Design | Interface adapted for desktop, tablet, and smartphone viewing |
| **Performance** | Response Time | Project search queries must load quickly |
| **Availability** | System Uptime | Platform must be available for access 24/7 |
| **Portability** | Browser Compatibility | Compatible with the latest versions of major web browsers |

---

## 📝 Future Improvements

Backend integration for the following features is planned:

| Feature | Endpoint | Panel |
|---|---|---|
| Project submission | `POST /projetos/enviar/` | Student |
| Project evaluation | `POST /projetos/<id>/avaliar/` | Professor |
| Dashboard report export | `GET /relatorios/exportar/` | Admin |

If we had another semester, we also plan to implement:

- **Thematic Categorization:** Grouping projects into thematic spaces (Sustainability, Health & Well-being, Tech & AI, etc.), as suggested by users in the requirements elicitation survey.
- **External Platform Integration:** Automatic import of GitHub repositories and LinkedIn profiles directly into the student's portfolio.
- **Notification System:** Real-time alerts for students when their project receives an evaluation or feedback from their professor.
- **Course Expansion:** Opening the platform to all Senac courses beyond ADS and Digital Games, serving the entire institution.

---

## 🔧 Troubleshooting

**`(venv)` not showing in the terminal**
→ Run again: `venv\Scripts\activate`

**`ModuleNotFoundError: No module named 'django'`**
→ The virtual environment is not active. See step 1.

**`no such table` error**
→ Migrations were not applied. Run: `python manage.py migrate`

**Admin panel loads without styles**
→ Run: `python manage.py collectstatic`

**Frontend not communicating with the backend**
→ Confirm the Django server is running and that the frontend was opened via Live Server, not by clicking the file directly.

---

## 👥 Authors & Project Team

| Name | Role | Contact |
|---|---|---|
| Alice Ralime dos Santos | Designer | — |
| Júlia Maria Silva Parra Torres | Project Manager | — |
| Raul Francisco Dulcine de Oliveira | Front-End | — |
| João Vitor Lima Braga Graciliano de Melo | Back-End | — |

**Academic Advisors / Professors:** Prof. Sônia Gomes de Oliveira & Prof. Filipe Carvalho

**Institution:** Faculdade Senac Pernambuco — Systems Analysis and Development — 2026.1
