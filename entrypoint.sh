#!/bin/bash

set -e

# On PROD, we run migrations at startup unless explicitly disabled.
if [ "$ENV" == "PROD" ]; then
    python3 manage.py migrate
fi

# On PROD, we always collect statics
if [ "$ENV" == "PROD" ]; then
    python3 manage.py collectstatic --no-input
fi

# On DEV, we migrate and generate fixtures
if [ "$ENV" == "DEV" ]; then
    python3 manage.py migrate
    python3 manage.py populate_users
fi

# Run the command
exec $@
