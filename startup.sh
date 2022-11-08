#!/bin/bash
echo "[INFO] This is the startup script for this FullStacks Application..."
echo "[INFO] Defining Environment Variables..."
ENV=$1

if [ ${ENV} = "prod" ]; then
    echo "The environment is: ${ENV}"
    export DJANGO_SETTINGS_MODULE='fs_accounting_app_core.settings.production'
    echo ${DJANGO_SETTINGS_MODULE}
    python3 manage.py check --deploy
    python3 manage.py migrate
    python3 manage.py runserver 0.0.0.0:8000
fi
