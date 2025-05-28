#!/bin/bash

set -e

if [[ "$1" == "start" ]]; then
    python3 manage.py migrate
    set -- python3 manage.py runserver 0.0.0.0:8000
fi

exec "$@"
