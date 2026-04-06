#!/usr/bin/env bash
pip install -r requirements.txt
python ZenZest/manage.py collectstatic --no-input
python ZenZest/manage.py migrate