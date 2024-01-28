import pandas as pd
import numpy as np
from statsmodels.tsa.statespace.sarimax import SARIMAX
from sklearn.preprocessing import MinMaxScaler
from keras.models import Sequential
from keras.layers import Dense, LSTM

df = pd.read_csv('alipur,-delhi, delhi, india-air-quality.csv', parse_dates=['date'])  
df.index = pd.to_datetime(df['date'])
df.set_index('date', inplace=True)

numeric_columns = [' o3', ' pm25', ' pm10', ' no2', ' so2', ' co']
non_numeric_values = df[numeric_columns].apply(lambda x: pd.to_numeric(x, errors='coerce')).isnull().sum()

df[numeric_columns] = df[numeric_columns].apply(pd.to_numeric, errors='coerce')

df.ffill(inplace=True)

exog_cols = [' pm25', ' pm10', ' no2', ' so2', ' co']
train_size = int(len(df) * 0.95)
train, test = df[:train_size], df[train_size:]

sarimax_model = SARIMAX(train[' o3'], exog=train[exog_cols], order=(0, 0, 1), seasonal_order=(0, 1, 2, 7), trend='ct')
sarimax_results = sarimax_model.fit(disp=False)


sarimax_pred = sarimax_results.get_forecast(steps=len(test), exog=test[exog_cols])

sarimax_pred_mean = sarimax_pred.predicted_mean

sarimax_pred_mean.index = test.index

sarimax_pred_hourly = np.repeat(sarimax_pred_mean.values, 24)

scaler = MinMaxScaler()
scaled_data = scaler.fit_transform(sarimax_pred_hourly.reshape(-1, 1))

sequence_length = 10
x, y = [], []
for i in range(len(scaled_data) - sequence_length):
    x.append(scaled_data[i:(i + sequence_length)])
    y.append(scaled_data[i + sequence_length])

x, y = np.array(x), np.array(y)

x = np.reshape(x, (x.shape[0], x.shape[1], 1))

lstm_model = Sequential()
lstm_model.add(LSTM(units=50, return_sequences=True, input_shape=(x.shape[1], 1)))
lstm_model.add(LSTM(units=50))
lstm_model.add(Dense(units=1))
lstm_model.compile(optimizer='adam', loss='mean_squared_error')
lstm_model.fit(x, y, epochs=17, batch_size=32)

future_hours = 12  # Number of hours to predict
input_sequence = scaled_data[-sequence_length:].reshape(1, -1, 1)

lstm_preds = []
for _ in range(future_hours):
    lstm_pred = lstm_model.predict(input_sequence)
    lstm_preds.append(lstm_pred[0, 0])
    input_sequence = np.append(input_sequence[:, 1:, :], lstm_pred.reshape(1, 1, 1), axis=1)

lstm_preds = scaler.inverse_transform(np.array(lstm_preds).reshape(-1, 1))


data = pd.DataFrame(lstm_preds, pd.date_range(start=test.index.max(), periods=future_hours, freq='H'))
data.to_csv('alipur_predictions_o3.csv')