# Personal Notes Application

## Overview
The **Personal Notes Application** is a web-based platform that allows users to securely create, edit, delete, and manage personal notes. 
Users must register and log in to access their notes. The application is built using Django, PostgreSQL, and styled with Bootstrap and custom CSS.

---

## Features

- **User Authentication**: Register, log in, and log out functionalities using Django's built-in authentication system.
- **CRUD Operations for Notes**:
  - Create new notes with a title and description.
  - Edit existing notes.
  - Delete notes with confirmation.
- **Search Functionality**: Quickly search through notes by title.
- **User Profile**: Displays user details (username, email, date joined, last login).
- **Responsive UI**: Clean and user-friendly interface designed with Bootstrap.
- **Dynamic Interactions**: Modal pop-ups for editing and deleting notes.

---

## Tech Stack

- **Backend**: Django (Python)
- **Database**: PostgreSQL
- **Frontend**: HTML, CSS, Bootstrap, JavaScript

---

## Installation

### 1. Clone the Repository
```bash
git clone https://github.com/your-username/personal-notes-app.git
cd personal-notes-app
```

### 2. Create Virtual Environment
```bash
python -m venv venv
source venv/bin/activate  # Linux/macOS
venv\Scripts\activate   # Windows
```

### 3. Install Dependencies
```bash
pip install -r requirements.txt
```

### 4. Configure Database
Update `settings.py` with your PostgreSQL credentials:
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'db_name',
        'USER': 'db_user',
        'PASSWORD': 'db_password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

### 5. Apply Migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

### 6. Run the Server
```bash
python manage.py runserver
```
Access the application at `http://127.0.0.1:8000/`

---

## Usage

1. **Register**: Create a new account.
2. **Login**: Log in with your credentials.
3. **Add Notes**: Click on "+ Add Note" to create a new note.
4. **Edit/Delete Notes**: Use the respective buttons on notes.
5. **Search Notes**: Use the search bar to filter notes.
6. **Profile**: View your profile information.

---

## Folder Structure
```
personal_notes/
├── notes/
│   ├── migrations/
│   ├── static/
│   │   └── notes/
│   │       └── home.css
│   ├── templates/
│   │   └── notes/
│   │       ├── add_note.html
│   │       ├── edit_note.html
│   │       ├── home.html
│   │       └── profile.html
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── views.py
│   └── urls.py
├── users/
│   ├── templates/
│   │   └── users/
│   │       ├── login.html
│   │       └── register.html
│   ├── forms.py
│   ├── views.py
│   └── urls.py
├── personal_notes/
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── db.sqlite3
├── manage.py
└── requirements.txt
```

---

## Contributing

1. Fork the repository.
2. Create a new branch: `git checkout -b feature-name`
3. Make your changes.
4. Commit changes: `git commit -m 'Add some feature'`
5. Push to the branch: `git push origin feature-name`
6. Submit a pull request.
---

## Contact

For any inquiries or feedback, feel free to reach out:

- **Developer:** Hussein Ahmed 
- **Email:** hussienphlool@gmail.com 
- **GitHub:** https://github.com/Alhussein20?tab=repositories
- **Vedio**https://youtu.be/Hmq_isb7iz0

---

Thank you for using the **Personal Notes Application**!

