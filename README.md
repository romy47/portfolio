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


## Dockerized Deployment (Production)
1. SSH to your server
2. Install docker, docker-compose, git
3. CLone the project: git clone https://github.com/romy47/portfolio.git
4. CD into the project directory: cd portfolio
5. Switch to the appropriate branch: git checkout medium_2_docker_prod
6. Create '.env' file following the example given on '.env.example'
7. Change the value of the PROD_ALLOWED_HOST and PROD_CERTBOT_EMAIL in .env with your own email address and domain

8. Add ssl certificate with
    - sudo docker-compose -f docker-compose.prod.yaml run --rm certbot /app/certbot_init.sh
5. Once the certificate is added stop all containers
    - sudo docker-compose -f docker-compose.prod.yaml down
6. Restart all services:
    - sudo docker-compose -f docker-compose.prod.yaml up
