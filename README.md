# bookratings-demo
Small Django site with PostgreSQL and Docker


## Requirements

 - docker
 - docker-compose


## Build and run locally

 - `docker-compose build`
 - `docker-compose up`
 - `./scripts/build.sh` to run migrations and `collectstatic`
 - Runs at http://localhost:8000/
 - `./scripts/manage.sh` to run Django management commands
 - `docker-compose exec django /bin/sh` for shell


 ## Ports

  - `8000`: web server
  - `5432`: database
