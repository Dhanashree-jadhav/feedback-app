# 🚀 Feedback Collector App (Flask + Docker + CI/CD)

A simple Flask-based feedback collection app with a beautiful Bootstrap UI. This project is Dockerized and uses GitHub Actions for CI/CD.

## 📌 Features

- Submit feedback via a form
- Stores all feedbacks in `feedback.txt`
- Clean, modern UI with Bootstrap
- Dockerized for easy deployment
- CI/CD via GitHub Actions

## 📂 Tech Stack

- Python 3.10
- Flask 2.3.2
- Docker
- GitHub Actions
- Bootstrap 5

## 💻 Run Locally

```bash
git clone https://github.com/Dhanashree-jadhav/feedback-app.git
cd feedback-app
docker build -t feedback-app .
docker run -p 5000:5000 feedback-app
