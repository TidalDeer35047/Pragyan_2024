import pandas as pd

pm25 = pd.read_csv('./predictor/data/alipur_predictions_pm2.5.csv')
pm10 = pd.read_csv('./predictor/data/alipur_predictions_pm10.csv')
o3 = pd.read_csv('./predictor/data/alipur_predictions_o3.csv')
no2 = pd.read_csv('./predictor/data/alipur_predictions_no2.csv')
so2 = pd.read_csv('./predictor/data/alipur_predictions_so2.csv')
co = pd.read_csv('./predictor/data/alipur_predictions_co.csv')

df = pd.DataFrame()

pm25.rename(columns= {"Unnamed: 0": "date"}, inplace=True)
pm25.rename(columns= {"0": "pm25"}, inplace=True)

pm10.rename(columns= {"Unnamed: 0": "date"}, inplace=True)
pm10.rename(columns= {"0": "pm10"}, inplace=True)

o3.rename(columns= {"Unnamed: 0": "date"}, inplace=True)
o3.rename(columns= {"0": "o3"}, inplace=True)

no2.rename(columns= {"Unnamed: 0": "date"}, inplace=True)
no2.rename(columns= {"0": "no2"}, inplace=True)

so2.rename(columns= {"Unnamed: 0": "date"}, inplace=True)
so2.rename(columns= {"0": "so2"}, inplace=True)

co.rename(columns= {"Unnamed: 0": "date"}, inplace=True)
co.rename(columns= {"0": "co"}, inplace=True)

df = pd.merge(pm25, pm10, on='date')
df = pd.merge(df, o3, on='date')
df = pd.merge(df, no2, on='date')
df = pd.merge(df, so2, on='date')
df = pd.merge(df, co, on='date')

df.to_csv("./future/alipur_future.csv")