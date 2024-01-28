#! /bin/bash

python3 "mover.py"

python3 "predictor/main_co.py"
python3 "predictor/main_no2.py"
python3 "predictor/main_o3.py"
python3 "predictor/main_pm2.5.py"
python3 "predictor/main_pm10.py"
python3 "predictor/main_so2.py"
