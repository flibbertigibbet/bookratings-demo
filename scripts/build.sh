#!/bin/bash

set -ex

function usage() {
    echo -n \
         "Usage: $(basename "$0")

Build app docker containers and run migrations.
"
}

if [ "${BASH_SOURCE[0]}" = "${0}" ]
then
    if [ "${1:-}" = "--help" ]
    then
        usage
    else
        docker-compose build
        docker-compose up -d database django

        # migrations
        docker-compose \
            run --rm --entrypoint python \
            django manage.py migrate --noinput

        docker-compose \
            run --rm --entrypoint python \
            django manage.py collectstatic --noinput

        docker-compose kill django \
            && docker-compose rm -f django
    fi
fi
