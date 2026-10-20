# EduCaps 🎓
### Learn Something New Every Day

EduCaps is a micro-learning web application that makes learning simple, engaging, and consistent. It breaks complex topics into bite-sized learning capsules, helping users build knowledge through interactive lessons, quizzes, and personalized progress tracking.

**Tech Stack:** Python · Django · HTML · CSS · JavaScript · PostgreSQL · SQLite

**Live Demo:** [EduCaps](https://edu-capsulelearning-1.onrender.com/)

**Repository:** [GitHub](https://github.com/Ananya-M-15/Edu-CapsuleLearning)

---

## ✨ Features

- **User Authentication** — Secure signup, login, and personalized accounts.
- **Interactive Dashboard** — Track learning activity, completion progress, and goals.
- **Learning Library** — Explore subjects, topics, and bite-sized capsules.
- **Interactive Quizzes** — Test understanding with multiple-choice questions.
- **Contextual AI Tutor** — Get rule-based explanations and learning hints.
- **Personalized Learning Modes** — Standard and Kids modes with distinct mentor experiences.
- **Spaced Repetition** — Revisit concepts using the SM-2 review scheduling algorithm.
- **Search and Navigation** — Find relevant learning content.
- **Admin Panel** — Manage subjects, topics, and capsules through Django Admin.
- **Responsive UI** — A modern interface with pastel visuals and interactive elements.

## 🛠️ Tech Stack

| Category | Technologies |
|---|---|
| Backend | Python, Django |
| Frontend | HTML5, CSS3, JavaScript |
| Database | SQLite, PostgreSQL |
| Static Files | WhiteNoise, Django Staticfiles |
| Web Server | Gunicorn |
| Deployment | Render |
| Testing | Django Test Framework |

## 🚀 Getting Started

### Prerequisites

- Python
- Git
- pip

### Installation

**1. Clone the repository**

```bash
git clone https://github.com/Ananya-M-15/Edu-CapsuleLearning.git
cd Edu-CapsuleLearning
```

**2. Create and activate a virtual environment**

Windows PowerShell:

```powershell
python -m venv venv
.\venv\Scripts\Activate.ps1
```

macOS/Linux:

```bash
python3 -m venv venv
source venv/bin/activate
```

**3. Install dependencies**

```bash
pip install -r requirements.txt
```

**4. Apply migrations**

```bash
python manage.py migrate
```

**5. Create an administrator account**

```bash
python manage.py createsuperuser
```

**6. Start the application**

```bash
python manage.py runserver
```

Open [http://127.0.0.1:8000/](http://127.0.0.1:8000/) in your browser.

## ⚙️ Environment Configuration

EduCaps supports environment-based configuration for local development and production deployment.

| Variable | Purpose |
|---|---|
| `DEBUG` | Controls Django debug mode. |
| `SECRET_KEY` | Django's private cryptographic signing key. |
| `ALLOWED_HOSTS` | Specifies permitted hostnames. |
| `DATABASE_URL` | Configures the database connection. |

For production, use a secure secret key, disable debug mode, configure allowed hosts, and keep credentials out of source control.

## ☁️ Deployment

EduCaps is configured for deployment on Render.

| Setting | Value |
|---|---|
| Build Command | `./build.sh` |
| Start Command | `gunicorn educaps_project.wsgi` |
| Production Database | PostgreSQL |
| Static Files | WhiteNoise |

The build script installs dependencies, applies database migrations, and collects static files.

## 🧪 Testing

Run the automated Django test suite:

```bash
python manage.py test learning.tests
```

The current test suite contains **77 passing tests**.

## 🔮 Future Improvements

- Expand the course and capsule catalogue.
- Improve personalized learning recommendations.
- Add richer progress analytics.
- Enhance accessibility and mobile usability.

## 👩‍💻 Author

**Ananya Maheshwari**

Computer Science Engineering — Artificial Intelligence and Machine Learning

[GitHub Profile](https://github.com/Ananya-M-15)

---

<p align="center">
  Made with 💜 to make daily learning easier.
</p>
