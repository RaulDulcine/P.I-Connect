# 🎓 PI Connect: Digital Repository & Observatory of Integrative Projects

> A web platform for publishing, discovering, and evaluating the Integrative Projects (PIs) developed by Senac students. Built as a Capstone Project (*Projeto Integrador*) for the **Systems Analysis and Development Program** at **Faculdade Senac Pernambuco**.

[![Senac](https://img.shields.io/badge/Institution-Senac%20Pernambuco-blue)](https://www.pe.senac.br/)
[![Status](https://img.shields.io/badge/status-In%20Development-yellow)]()

---

## 📋 Project Overview

**PI Connect** is a digital ecosystem built to amplify the visibility of Integrative Projects produced by Senac students. The platform works as an academic repository/observatory where students publish their work, professors review and provide feedback, and partner companies discover talent and innovative solutions and the UN Sustainable Development Goals (SDGs).

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
* **Backend:** Python, Django
* **Database:** SQLite (development) via Django ORM
* **Authentication:** Django's built-in authentication system with profile-based access control
* **UI/UX Design:** Figma
* **Project Management:** Trello

---

## ⚙️ Getting Started (Local Development)

Follow the steps below to run the project on your machine.

### 1. Prerequisites
Make sure you have installed:

- [Python](https://www.python.org/) (v3.10 or higher)

> No additional database setup required — the project uses SQLite, which is bundled with Python.

### 2. Configuration (`.env`)

Create a `.env` file in the project root and set the environment variables as shown below:

```env
SECRET_KEY = 'django-insecure-alguma-coisa-muito-longa-aqui'

DEBUG = True
```

### 3. Setup and Execution

```bash
# 1. Clone the repository
git clone https://github.com/RaulDulcine/P.I-Connect.git
cd pi-connect

# 2. Install dependencies
pip install -r requirements.txt

# 3. Apply database migrations
python manage.py migrate

# 4. Start the development server
python manage.py runserver
```

The application will be available at `http://127.0.0.1:8000`.

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

If we had another semester, we plan to implement:

- **Thematic Categorization:** Grouping projects into thematic spaces (Sustainability, Health & Well-being, Tech & AI, etc.), as suggested by users in the requirements elicitation survey.
- **External Platform Integration:** Automatic import of GitHub repositories and LinkedIn profiles directly into the student's portfolio.
- **Notification System:** Real-time alerts for students when their project receives an evaluation or feedback from their professor.
- **Course Expansion:** Opening the platform to all Senac courses beyond ADS and Digital Games, serving the entire institution.

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

## 📄 Licença
Este projeto está sob a licença MIT. Veja o arquivo [LICENSE](LICENSE) para mais detalhes.
