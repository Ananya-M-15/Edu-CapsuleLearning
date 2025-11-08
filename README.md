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