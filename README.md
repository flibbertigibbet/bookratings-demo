# bookratings-demo
Small Django site with PostgreSQL and Docker


## Requirements

 - docker
 - docker-compose


## Build and run locally

 - - `./scripts/build.sh` to build containers, run migrations, and `collectstatic`
 - `docker-compose up`
 - Runs at http://localhost:8000/
 - Tests run with `./scripts/test.sh` with the containers up
 - `./scripts/manage.sh` to run Django management commands
 - `docker-compose exec django /bin/sh` for shell


 ## Ports

  - `8000`: web server
  - `5432`: database
