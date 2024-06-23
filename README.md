# Dynamic Portfolio and Blog App
A database driven portfolio and blog site built with Django, Postgres, and Bootstrap.

## Motivation
I want to have a personal portfolio and blog website where work experience, projects, blog posts and skills can be tagged with common set of programming languages frameworks. This design links blog posts, work experiences, personal projects, and skills together so that the same data is not repeated. This also helps to find related entity types by matching programming languages. Django has built in admin interface where new data for these entities can be inserted. Currently I am using this project for my own portfolio and will continue updating different pieces.

## Features
- Skills, Work Experiences, Projects, Publications all of these are database driven.
- Mostly used pure Bootstrap components for minimalistic and sleek design
- CKEditor is used in the django admin interface for writing the description field of projects and blog posts as rich text.

## Prerequisites
- Python 3.12.0 or higher

## Installation
1. Setup PostgresSQL
2. Clone repo: `git clone git@github.com:romy47/portfolio.git`
3. Create a virtual environment: `python3 -m venv venv`
4. Activate virtual environment:
    - Bash: `. venv/bin/activate`
    - Windows: `. .\venv\Scripts\activate`
5. Create an environment variable file in the root directory for storing development and production keys. Use the '.env.example' as the example.
6. Install dependencies: `pip install -r requirements.txt`
7. Migrate database: `python manage.py migrate`
8. Start app: `python manage.py runserver`
