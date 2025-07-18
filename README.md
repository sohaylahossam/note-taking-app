# 📝 Note-Taking Web App

A simple web-based note-taking application built with **Flask** and **MariaDB**, deployed on an **AWS EC2** instance with a backup strategy using an EBS volume.

## 🚀 Features

- Add and store notes using a web form
- Notes are saved in a MariaDB database
- Hosted on AWS EC2 running RHEL 9
- Daily backups to an attached EBS volume

## 🛠️ Tech Stack

- Python 3 (Flask)
- MariaDB
- HTML/CSS (Jinja2 templates)
- Amazon EC2 (Red Hat Enterprise Linux 9)
- AWS EBS for database backup

## 📁 Project Structure

note-taking-app/
├── app.py
├── templates/
│ └── index.html
├── backup/
│ └── (database dumps go here)
├── requirements.txt
└── README.md
