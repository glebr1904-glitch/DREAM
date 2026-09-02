#!/bin/bash
cd "$HOME/Desktop/DREAM" || exit 1
. venv/Scripts/activate
cd "$HOME/Desktop/DREAM/my_shop" || exit 1
python manage.py runserver
