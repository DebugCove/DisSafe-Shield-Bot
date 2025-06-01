#!/bin/bash

set -e

clear
echo
echo

echo "  _____  _      _____        __        _____ _     _      _     _   ____        _   "
echo " |  __ \(_)    / ____|      / _|      / ____| |   (_)    | |   | | |  _ \      | |  "
echo " | |  | |_ ___| (___   __ _| |_ ___  | (___ | |__  _  ___| | __| | | |_) | ___ | |_ "
echo " | |  | | / __|\___ \ / _\` |  _/ _ \  \___ \| '_ \| |/ _ \ |/ _\` | |  _ < / _ \| __|"
echo " | |__| | \__ \____) | (_| | ||  __/  ____) | | | | |  __/ | (_| | | |_) | (_) | |_ "
echo " |_____/|_|___/_____/ \__,_|_| \___| |_____/|_| |_|_|\___|_|\__,_| |____/ \___/ \__|"
echo "                                                                                    "
echo "                                                                                    "
echo
echo "Starting ...."

project_path="${PWD}"
environment_create=false
env_path="${project_path}/.env"
environment_path="${project_path}/.venv"
requirements_path="${project_path}/requirements.txt"

if [ ! -d "${environment_path}" ]; then
  environment_create=true
  echo "INFO - Virtual environment not found! Creating"
  python3 -m venv "${environment_path}" || { echo "ERROR - Failed to create virtual environment"; exit 1; }
fi

echo "INFO - Activating virtual environment"
source "${environment_path}/bin/activate"

if [ "$environment_create" = "true" ]; then
  if [ ! -f "$requirements_path" ]; then
    echo "ERROR - requirements.txt not found!"
    exit 1
  fi
  echo "INFO - Installing dependencies"
  pip install -r "$requirements_path"
fi

echo "INFO - Starting the application"
echo
python3 app.py
echo
echo
