<!DOCTYPE html>

# JobSphere 🌐

<div align="center">
  <img src="https://readme-typing-svg.herokuapp.com?font=Fira+Code&pause=1000&color=FF6B6B&center=true&vCenter=true&width=620&lines=Where+Passion+Meets+Purpose;Connecting+Talent+with+Opportunity;Full-Stack+Job+Platform;Django+%7C+JavaScript+%7C+SCSS;Bridging+the+Talent+Gap" alt="Typing Animation" />
</div>

<p align="center">
  <img alt="JavaScript" src="https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black"/>
  <img alt="Python" src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=FFD43B"/>
  <img alt="Django" src="https://img.shields.io/badge/Django-092E20?style=for-the-badge&logo=django&logoColor=white"/>
  <img alt="SCSS" src="https://img.shields.io/badge/SCSS-CC6699?style=for-the-badge&logo=sass&logoColor=white"/>
  <img alt="HTML5" src="https://img.shields.io/badge/HTML5-E34F26?style=for-the-badge&logo=html5&logoColor=white"/>
  <img alt="CSS3" src="https://img.shields.io/badge/CSS3-1572B6?style=for-the-badge&logo=css3&logoColor=white"/>
</p>

<p align="center">
  <img alt="JS" src="https://img.shields.io/badge/JavaScript-47.2%25-F7DF1E?style=flat-square"/>
  <img alt="CSS" src="https://img.shields.io/badge/CSS-25.0%25-1572B6?style=flat-square"/>
  <img alt="SCSS" src="https://img.shields.io/badge/SCSS-12.3%25-CC6699?style=flat-square"/>
  <img alt="HTML" src="https://img.shields.io/badge/HTML-12.0%25-E34F26?style=flat-square"/>
  <img alt="Python" src="https://img.shields.io/badge/Python-3.5%25-3776AB?style=flat-square"/>
</p>

---

## 💡 Mission

> *"Where passion meets purpose."*

**JobSphere** bridges the gap between talented professionals and employers seeking the right fit. Beyond matching skills to roles, JobSphere focuses on meaningful alignment — connecting people with opportunities that reflect not just what they can do, but what they genuinely care about.

---

## 🚀 What JobSphere Does

<div align="center">

| 👤 **For Job Seekers** | 🏢 **For Employers** | 🔐 **Platform Core** |
|---|---|---|
| Browse all live job postings | Create & publish job listings | Secure user registration |
| View full job details | Edit and update postings | Login / logout session management |
| Filter by role, passion & fit | Remove filled positions | Role-based access control |
| Apply with purpose | Find candidates that truly fit | Authentication-protected routes |

</div>

---

## 🗂️ Core Features

### 📋 Job Listings
Full CRUD support for job postings — create, browse, view, edit, and delete — backed by a relational database and rendered through Django templates.

### 🔍 Job Detail Pages
Each posting surfaces its full attributes: title, description, requirements, and employer details — in a clean, scannable layout.

### 🔐 User Authentication
Secure login, logout, and registration flows with session management, ensuring users can only perform actions appropriate to their role.

### 🎨 Responsive UI
Built with SCSS and vanilla JavaScript for a polished, responsive experience across devices — no heavy frontend framework required.

---

## ⚙️ Views & Route Logic (`views.py`)

| View | Method | Purpose |
|---|---|---|
| `job_list` | `GET` | Retrieve and display all active job postings |
| `job_detail` | `GET` | Show full details for a specific job by ID |
| `job_create` | `GET / POST` | Render creation form; validate and save new posting |
| `job_update` | `GET / POST` | Pre-fill edit form; validate and persist changes |
| `job_delete` | `POST` | Confirm and remove a job entry; redirect to list |
| `login_view` | `GET / POST` | Authenticate user; initiate session |
| `logout_view` | `POST` | Terminate session; redirect to landing |
| `register_view` | `GET / POST` | Create new user account; validate and save |

---

## 🚀 Getting Started

### Prerequisites
- Python 3.8+
- pip
- Node.js (optional — for SCSS compilation)

### Installation

**1. Clone the repository**
```sh
git clone https://github.com/abinraju23/JobSphere.git
cd JobSphere
```

**2. Create a virtual environment**
```sh
python -m venv venv
source venv/bin/activate        # macOS / Linux
venv\Scripts\activate           # Windows
```

**3. Install Python dependencies**
```sh
pip install -r requirements.txt
```

**4. Apply migrations**
```sh
python manage.py migrate
```

**5. Run the development server**
```sh
python manage.py runserver
# Navigate to http://localhost:8000
```

---

## 📁 Project Structure

```
JobSphere/
│
├── 📂 jobs/
│   ├── models.py          # Job & User data models
│   ├── views.py           # Core view functions (CRUD + Auth)
│   ├── urls.py            # Route definitions
│   └── forms.py           # Django form classes
│
├── 📂 templates/
│   ├── base.html          # Base layout template
│   ├── job_list.html      # All postings page
│   ├── job_detail.html    # Single job page
│   ├── job_form.html      # Create / update form
│   └── auth/              # Login, logout, register templates
│
├── 📂 static/
│   ├── css/               # Compiled CSS
│   ├── scss/              # SCSS source files
│   └── js/                # JavaScript modules
│
├── manage.py
├── requirements.txt
└── README.md
```

---

## 🛠️ Tech Stack Breakdown

```
Frontend  — JavaScript (47.2%) · CSS (25.0%) · SCSS (12.3%) · HTML (12.0%)
Backend   — Python / Django (3.5%)
Database  — SQLite (dev) / PostgreSQL (prod-ready)
Auth      — Django session-based authentication
Styling   — SCSS with component-level architecture
```

---

## 👤 Author

**Abin Raju**
MSc Data Analytics — Dublin Business School (September 2025 cohort)

<p>
  <a href="https://www.linkedin.com/in/abinraju2308">
    <img alt="LinkedIn" src="https://img.shields.io/badge/LinkedIn-0A66C2?style=for-the-badge&logo=linkedin&logoColor=white"/>
  </a>
  <a href="https://github.com/abinraju23">
    <img alt="GitHub" src="https://img.shields.io/badge/GitHub-181717?style=for-the-badge&logo=github&logoColor=white"/>
  </a>
</p>

---

## 📄 License

This project does not currently specify an open-source licence. Default copyright laws apply — the source code may not be reproduced, distributed, or used without explicit permission from the author.

---

<div align="center">
  <sub>Built with Django · JavaScript · SCSS · HTML · Python</sub><br/>
  <sub>© 2026 Abin Raju</sub>
</div>
