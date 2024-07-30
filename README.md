# Dynamic Portfolio and Blog App
A database-driven portfolio and blog site built with Django, PostgreSQL, and Bootstrap.

## Motivation
I had a portfolio site before but I was tired of changing HTML content and wanted to have a more structured approach. For my portfolio site, I wanted to organize work experience, projects, blog posts, publications, and skills associated with a common set of programming languages and frameworks. For example, adding 'Django' into a portfolio project and then adding it again to another blog post about Django development. This design ensures that data is linked across multiple entities minimizing redundancy. It also facilitates finding related entity types through programming language matches. Django includes a built-in admin interface for inserting new data into these entities. I am currently using this project for my portfolio and plan to update various components regularly.

## Features
- Skills, Work Experiences, Projects, Publications all of these are database-driven
- Mostly used pure Bootstrap components for minimalistic and sleek design
- CKEditor is used in the Django admin interface for writing the description field of projects and blog posts as rich text

## Prerequisites
- Python 3.12.0 or higher

## Dev Installation
1. Setup PostgreSQL
2. Clone repo: `git clone git@github.com:romy47/portfolio.git`
3. Create a virtual environment: `python3 -m venv venv`
4. Activate virtual environment:
    - Bash: `. venv/bin/activate`
    - Windows: `. .\venv\Scripts\activate`
5. Create an environment variable file in the root directory for storing development and production keys. Use the '.env.example' as the example.
6. Install dependencies: `pip install -r requirements.txt`
7. Migrate database: `python manage.py migrate`
8. Start app: `python manage.py runserver`

## Docker Installation (Production)
1. Install docker, docker-compose
2. Create '.env' file following the example given on '.env.example'
2. Add ssl certificate with
    - sudo docker-compose -f docker-compose.prod.yaml run --rm certbot /app/certbot_init.sh
3. Once the certificate is added stop all containers
    - docker-compose -f docker-compose.prod.yaml down
4. Return the docker compose file. Use only this command for all subsequent deployments:
    - docker-compose -f docker-compose.prod.yaml up
