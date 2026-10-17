# EduCaps - Daily Micro-Learning App

EduCaps is a web application designed for daily micro-learning, inspired by Duolingo. It delivers bite-sized lessons ("capsules") and activities every day to help users grasp diverse topics like personal finance, soft skills, and more.

## Features

- **User Authentication:** Secure signup, login, and logout functionality.
- **Interactive Dashboard:** A personalized dashboard with a "glassmorphism" design, animated background, and progress tracking.
- **Subject & Topic Library:** A collapsible accordion view to browse all available learning content and track progress.
- **Flip-Card Learning:** Daily lessons are presented as interactive flip cards for an engaging experience.
- **Admin Content Management:** A full-featured Django admin panel for easily adding and managing subjects, topics, and daily capsules.

## Tech Stack

- **Backend:** Python, Django
- **Frontend:** HTML, CSS, JavaScript
- **Database:** SQLite (for development), PostgreSQL (for production)
- **Deployment:** Render

## Local Setup

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/YOUR_USERNAME/educaps.git
    cd educaps
    ```

2.  **Create and activate a virtual environment:**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: venv\Scripts\activate
    ```

3.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Run migrations and create a superuser:**
    ```bash
    python manage.py migrate
    python manage.py createsuperuser
    ```

5.  **Run the development server:**
    ```bash
    python manage.py runserver
    ```

## Configuration & Environment Variables

EduCaps supports 12-factor environment variables for production while defaulting to local SQLite for frictionless development.

| Variable | Default (Local) | Production Requirement | Purpose |
|---|---|---|---|
| `DEBUG` | `True` (locally) | Set to `False` | Controls Django debug mode. |
| `SECRET_KEY` | Dev-only fallback | **Required** when `DEBUG=False` | Django cryptographic signing key. |
| `ALLOWED_HOSTS` | `127.0.0.1,localhost,[::1]` | Auto-set on Render | Comma-separated allowed domains. |
| `DATABASE_URL` | None (uses `db.sqlite3`) | **Required** on Render | PostgreSQL connection URL. |

### Running with PostgreSQL
To connect to a PostgreSQL database locally or in staging/production:
```bash
export DATABASE_URL="postgresql://user:password@localhost:5432/educaps"
# On Windows PowerShell: $env:DATABASE_URL="postgresql://user:password@localhost:5432/educaps"
python manage.py migrate
```

### Initial Content Seeding
EduCaps includes an idempotent content-seeding command that loads the 5 subjects, 5 topics, and 50 capsules from `learning/fixtures/initial_content.json`:

```bash
python manage.py seed_initial_content
```

- **Idempotent & Safe**: If the target database already contains any learning content, seeding is skipped automatically, preserving all existing and administrator-edited records.
- **Privacy Preserved**: The fixture and command contain zero user accounts, passwords, progress records, or session data.
- **Atomic**: Wrapped in a database transaction to ensure all-or-nothing population without partial state.

## Deployment on Render

### Service Commands Configuration

When deploying EduCaps as a Web Service on Render, configure the service commands as follows:

- **Build Command:** `./build.sh`
- **Pre-Deploy Command:** `python manage.py migrate && python manage.py seed_initial_content`
- **Start Command:** `gunicorn educaps_project.wsgi:application`

### Pre-Deploy Command Requirements & Safe Fallback
Render provides Pre-Deploy Commands to execute database tasks after the container build completes and persistent networking to the PostgreSQL instance is established, but before web traffic is routed to the new deploy.

> **Note on Plan Support**: The Pre-Deploy Command is available on Render instance plans that support release commands (Starter plan and above).
> 
> **Safe Alternative for Free/Unsupported Plans**: If your instance type does not support Pre-Deploy Commands, keep database operations strictly separate from `./build.sh` to ensure image builds remain stateless. Instead, initialize the database once after provisioning and linking the PostgreSQL service using the Render Shell (SSH) or a manual one-off task:
> ```bash
> python manage.py migrate
> python manage.py seed_initial_content
> ```