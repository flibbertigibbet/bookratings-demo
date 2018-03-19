# bookratings-demo
Small Django site with PostgreSQL and Docker


## Build status

[![Build Status](https://travis-ci.org/flibbertigibbet/bookratings-demo.svg?branch=develop)](https://travis-ci.org/flibbertigibbet/bookratings-demo)


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
