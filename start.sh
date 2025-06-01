#!/bin/bash

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

environment_create=false

if [ ! -f .env ]; then
  echo
  echo "ERROR - .env file not found!"
  exit 1
fi

if [ ! -d ".venv" ]; then
  environment_create=true
  echo "INFO - Virtual environment not found! Creating"
  python3 -m venv .venv
fi

echo "INFO - Activating virtual environment"
source .venv/bin/activate

if [ "$environment_create" = true ]; then
  echo "INFO - Installing dependencies"
  pip install -r requirements.txt
fi

echo "INFO - Starting the application"
echo
python3 app.py

echo
echo
