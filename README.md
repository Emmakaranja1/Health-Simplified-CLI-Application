# 🥗 Health Simplified CLI Application

A command-line tool to help users manage their nutrition goals, track daily food intake, and plan weekly meals—designed for busy professionals and developer students.

---

## 📌 Project Overview

**Health Simplified** is a Python-based CLI application that enables users to:

- Log and review meals
- Set and track daily and weekly nutrition goals
- Generate weekly meal plans
- View reports on their progress

This project is built to reinforce object-oriented programming (OOP), CLI tooling with [`typer`](https://typer.tiangolo.com/), and SQLAlchemy with a PostgreSQL backend. It also emphasizes clean software practices, modular design, and unit testing.

---

## 🎯 Objectives

### 📚 Educational
- Reinforce key CS concepts: OOP, inheritance, and composition
- Practice SQLAlchemy ORM with PostgreSQL
- Apply CLI application architecture using Typer
- Gain experience with testing and packaging Python applications

### ✅ Functional
- Provide a full-featured CLI for nutrition tracking
- Include CRUD operations for users, food entries, goals, and meal plans
- Implement input validation, error handling, and reports
- Package the tool for easy installation (`pip install .`)

---

## 📦 Features & Commands

### 👤 User Management
```bash
myapp user create --name <name>
myapp user list

### FOOD ENTRIES
myapp entry add --user <name> --food <food> --calories <int> --date <YYYY-MM-DD>
myapp entry list [--user <name>] [--date <date>]
myapp entry update --id <int> [fields...]
myapp entry delete --id <int>


🎯 Goals
myapp goal set --user <name> --daily <int> --weekly <int>
myapp goal list --user <name>

📊 Reporting
myapp report --user <name> --date <YYYY-MM-DD>


📅 Meal Planning
myapp plan-meal --user <name> --week <int>
myapp plan-meal update --id <int> [fields...]



#### 🧑‍💼 User Personas
Busy Professional
Quickly log meals via terminal

Set and monitor calorie goals

View daily summaries

Plan meals for the week

Developer Student
Submit daily progress via PRs

Understand code structure and testing

Validate changes with test coverage


🛠️ Tech Stack
Language: Python 3.x

CLI: Typer

Database: PostgreSQL with SQLAlchemy ORM

Testing: pytest

Packaging: setuptools or pyproject.toml with entry points

🧪 Testing
Ensure at least 80% code coverage using pytest. To run tests:
pytest --cov=myapp tests/

📦 Installation
Clone the repository and install locally:
git clone https://github.com/yourusername/health-simplified-cli.git
cd health-simplified-cli
pip install .

CLI Entry Point
Once installed, you can use the CLI via:
myapp --help


🧭 Development Guidelines
Follow milestone-based PRs for daily check-ins

Include tests with each feature or bug fix

Keep functions and classes modular and well-documented

🤝 Contributing
Contributions are welcome! Please:

Fork the repo

Create a new branch (git checkout -b feature/your-feature)

Commit your changes

Open a PR with a clear description

📃 License
This project is licensed under the MIT License.

