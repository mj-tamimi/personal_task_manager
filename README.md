# Task Manager
![Static Badge](https://img.shields.io/badge/Python-3.8%2B-Blue)


A simple command-line task manager written in Python. Users can enter their name, add multiple tasks, and save everything to a local `task.txt` file. A hidden admin mode is available, protected by a password stored in `.env`.

## Description

Task Manager CLI is a beginner-friendly Python script that lets you:
- Authenticate as an admin using a password from environment variables.
- Enter your name and a list of tasks.
- Save all tasks to a `task.txt` file (append mode).

It's a small project to practice file I/O, environment variables, and basic control flow in Python.

## Table of Contents

- [Description](#description)
- [Features](#features)
- [Project Structure](#project-structure)
- [File Description](#file-description)
- [Requirements](#requirements)
- [Installation](#installation)
- [Environment Setup](#environment-setup)
- [Usage](#usage)
- [Example Output](#example-output)
- [Screenshots](#screenshots)
- [Demo](#Demo)
- [Roadmap](#roadmap)
- [Contributing](#contributing)
- [License](#license)
- [Author](#author)

## Features

- 🔐 **Admin mode** — gated by a password loaded from `.env`.
- 👤 **User name input** — recorded alongside the tasks.
- ➕ **Unlimited task entry** — keep adding until you type `q`.
- 💾 **Persistent storage** — tasks are appended to `task.txt`.
- 🌱 **Environment-based config** — secrets stay out of the source code.

## Project Structure
task-manager/
│
├── main.py
├── requirements.txt
├── .env.example
├── .gitignore
└── README.md
## File Description

| File | Description |
|------|-------------|
| `main.py` | Main script: handles admin login, task input, and writes to `task.txt`. |
| `requirements.txt` | Python packages needed to run the project. |
| `.env.example` | Template for environment variables. Copy it to `.env` and fill in values. |
| `.gitignore` | Tells git which files and folders to ignore (e.g. `.env`, `task.txt`). |
| `README.md` | Project documentation (this file). |

## Requirements

- Python 3.8 or higher
- `python-dotenv`

## Installation

1. open a terminal in the project folder.
2. chech that python is installed:
```bash
python --version
```
3. install the python packages:
```bash
pip install -r requirements.txt
```

## Environment Setup
The admin password is read from an environment variable. Create a .env file in the project root:
1. Copy the template:
cp .env.example .env
2. Open .env and set your password:
TASK_MANAGER_ADMIN_PASSWORD=your_secret_password_here
Quote ⚠️ Never commit .env to git. It's already listed in .gitignore.

## Usage
Run the script:
python main.py
You'll be prompted to:
1. Open admin mode (optional).
2. Enter your name.
3. Add tasks one by one. Type q when you're done.

## Example Output
do you want to open admin mode? yes/no: no
Welcome. Please enter your name: Alex
Enter a task (or 'q' to quit): Buy groceries
Enter a task (or 'q' to quit): Finish homework
Enter a task (or 'q' to quit): Call mom
Enter a task (or 'q' to quit): q
After running, task.txt will contain something like:
Name: Alex | All tasks: ['  -Title: Buy groceries\n  -Status: Pending...', '  -Title: Finish homework\n  -Status: Pending...', '  -Title: Call mom\n  -Status: Pending...']

## Screenshots
![image1](pictures\image0.png)
### ------------------------------------------------
![image2](pictures\image1.png)
### ------------------------------------------------
![image3](pictures\image2.png)

## Demo
![demo_gif](gifs\demo.gif)

## Roadmap
- [x] Add unlimited tasks
- [x] Tasks get saved to task.txt
- [ ] Mark tasks as done / pending
- [ ] Edit or delete existing tasks
- [ ] View previous tasks from task.txt
- [ ] Save tasks in JSON instead of a plain string
- [ ] Add timestamps to each task

## Contributing

## License

## Author
Created by [Mojtaba Tamimi](https://github.com/mj-tamimi).