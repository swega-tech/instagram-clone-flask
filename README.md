# Instagram Clone (Flask Web Application)

A fully responsive, full-stack Instagram Clone built using the **Flask** microframework, **Bootstrap 5**, and **SQLite**. This application features complete **CRUD** functionality, database validations, dynamic user profile generation, and a responsive layout featuring a fixed advertisement side rail.

## 🚀 Features

* **Full CRUD Operations**: Users can register accounts, create picture posts with captions, view specific details, edit post content, and delete existing entries.
* **Database Management (SQLite)**: Built-in persistence layer driven by **SQLAlchemy** ORM mapping.
* **Security & Constraints**: 
    * Form validation ensuring passwords are at least 6 characters long.
    * Database-level unique constraint handling to block duplicate email registrations.
* **Dynamic UI Layout**: Built with a sleek Bootstrap 5 structure incorporating a modern, sticky sidebar advertisement rail designed to hide on smaller mobile displays.

---

## 📂 Project Architecture

```text
instagram_clone/
│
├── static/                 # Directory for static web assets (images, CSS)
├── templates/              # Jinja2 HTML layout components
│   ├── base.html           # Core master layout with the sticky ad sidebar
│   ├── home.html           # Global feed layout interface
│   ├── register.html       # User signup form with password requirements
│   ├── profile.html        # Targeted user profile and post-grid gallery
│   ├── post_detail.html    # Expanded viewport for a post with Update/Delete nodes
│   └── create_post.html    # Unified dynamic form for creating/modifying posts
│
├── app.py                  # Primary application configuration and route engine
├── models.py               # SQLite Database structure configuration definitions
├── .gitignore              # Protects database.db from being uploaded to GitHub
└── README.md               # Project documentation
