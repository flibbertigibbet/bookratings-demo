#!/bin/bash

set -e

docker-compose up -d database django

# tests
echo $'\nRunning Django tests...'
docker-compose \
    run --rm --entrypoint python \
    django manage.py test

docker-compose kill django \
    && docker-compose rm -f django
echo $'\nDjango tests done.'

# python linter
echo $'\nRunning linter...'
flake8 .
echo 'Linting done.'

echo $'\nTests done.'
