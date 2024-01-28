import pandas as pd


real_time = pd.read_csv("./realtime/alipur_realtime.csv")
predictor = pd.read_csv("./predictor/alipur,-delhi, delhi, india-air-quality.csv")

oldest = real_time.iloc[1, :]
oldest = oldest.to_list()
predictor.loc[len(predictor)]=oldest
pd.to_csv("./predictor/alipur,-delhi, delhi, india-air-quality.csv")