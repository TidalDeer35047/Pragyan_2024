#! /bin/bash

unzip "static.zip"
python3 "update_realtime.py" &
sh "app_run.sh" &
python3 "mover.py" &
sh "predict_run.sh" &