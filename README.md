# Arts Management System

A web-based event management platform for arts organizations, built with Django.

## Features

- User authentication (signup, login, logout)
- Event creation and management
- Registration for events
- Scoreboard and results tracking
- Suggestion box for feedback and complaints
- Admin interface for managing users and events

## Project Structure

```
artsmanagementsystem/
├── manage.py
├── requirements.txt
├── db.sqlite3
├── artsmanagementsystem/
│   ├── settings.py
│   ├── urls.py
│   ├── wsgi.py
│   └── asgi.py
├── authentication/
│   ├── models.py
│   ├── views.py
│   ├── urls.py
│   └── templates/
└── event/
    ├── models.py
    ├── views/
    ├── urls.py
    └── templates/
```

## Getting Started

1. **Clone the repository:**
   ```sh
   git clone https://github.com/yourusername/artsmanagementsystem.git
   cd artsmanagementsystem
   ```

2. **Create and activate a virtual environment:**
   ```sh
   python -m venv artmng_env
   source artmng_env/Scripts/activate  # Windows
   # or
   source artmng_env/bin/activate      # macOS/Linux
   ```

3. **Install dependencies:**
   ```sh
   pip install -r requirements.txt
   ```

4. **Apply migrations:**
   ```sh
   python manage.py migrate
   ```

5. **Run the development server:**
   ```sh
   python manage.py runserver
   ```

6. **Access the app:**
   Open [http://127.0.0.1:8000/](http://127.0.0.1:8000/) in your browser.

## Usage

- Register a new account or login.
- Create and manage events.
- Register for events and view scoreboards.
- Submit suggestions or complaints via the suggestion box.

## Admin

To access the Django admin panel:

1. Create a superuser:
   ```sh
   python manage.py createsuperuser
   ```
2. Login at [http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/)

## Technologies

- Python 3.11+
- Django 5.1.4
- Bootstrap 5 (frontend)

## License

MIT License

---

*For more details, see the source code and documentation.*
