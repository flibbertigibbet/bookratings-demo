#!/bin/bash

set -e

docker-compose exec django python manage.py "${@}"

