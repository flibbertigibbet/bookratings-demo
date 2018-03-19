# bookratings-demo
Small Django site with PostgreSQL and Docker


## Requirements

 - docker
 - docker-compose


## Build and run locally

 - - `./scripts/build.sh` to build containers, run migrations, and `collectstatic`
 - `./scripts/server.sh` to run at http://localhost:822/
 - Tests run with `./scripts/test.sh` with the containers up
 - `./scripts/manage.sh` to run Django management commands
 - `docker-compose exec django /bin/sh` for shell


 ## Ports

  - `8222`: web server
  - `5432`: database
