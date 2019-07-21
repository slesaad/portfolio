#!/bin/bash

sass --watch stylesheets:static/css &
python manage.py runserver 0.0.0.0:8000
