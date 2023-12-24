# StudyBuddy

StudyBuddy is a web application built with Django that allows users to create profiles, study rooms, and engage in discussions related to specific topics within those rooms. It incorporates user authentication to ensure only authenticated users can create rooms and participate in discussions.

## Features

- **User Profiles:** Users can create and manage their profiles.
- **Study Rooms:** Authenticated users can create study rooms.
- **Room Chat:** Users can participate in room-specific discussions.
- **User Authentication:** Includes functionalities like login and logout.

## Tech Stack

- **Frontend:**
  - HTML
  - CSS
  - JavaScript

- **Backend:**
  - Python (Django)

- **Database:**
  - SQLite3

## Getting Started

To set up this project locally, follow these steps:

1. Clone the repository.
2. Set up a virtual environment.
3. Install dependencies from `requirements.txt`.
4. Run migrations to set up the database.
5. Start the Django development server.

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/studybuddy.git



2. Create and activate a virtual environment:

```bash
python -m venv venv
source venv/bin/activate   # For Unix/Mac
venv\Scripts\activate      # For Windows
```

3. Install dependencies:

```bash
pip install -r requirements.txt
```

4. Run migrations:

```bash
python manage.py migrate
```

5. Start the development server:

```bash
python manage.py runserver
```