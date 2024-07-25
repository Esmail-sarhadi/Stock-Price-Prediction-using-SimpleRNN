import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from keras import Sequential
from keras.src.layers import SimpleRNN, Dense
from sklearn.preprocessing import MinMaxScaler

stock_data = pd.read_csv('dataset.csv')
close_prices = stock_data['open'].values

price_scaler = MinMaxScaler(feature_range=(0, 1))
normalized_prices = price_scaler.fit_transform(close_prices.reshape(-1, 1))

train_size = len(normalized_prices) - 150
train_data = normalized_prices[:train_size]
test_data = normalized_prices[train_size:]

def create_sequence_data(dataset, sequence_length):
    X, Y = [], []
    for i in range(len(dataset)-sequence_length):
        X.append(dataset[i:i+sequence_length])
        Y.append(dataset[i+sequence_length])
    return np.array(X), np.array(Y)

sequence_length = 7
train_sequences, train_labels = create_sequence_data(train_data, sequence_length)
test_sequences, test_labels = create_sequence_data(test_data, sequence_length)
train_sequences = np.reshape(train_sequences, (train_sequences.shape[0], train_sequences.shape[1], 1))
test_sequences = np.reshape(test_sequences, (test_sequences.shape[0], test_sequences.shape[1], 1))

rnn_model = Sequential()
rnn_model.add(SimpleRNN(units=50, return_sequences=False, input_shape=(sequence_length, 1)))
rnn_model.add(Dense(1))
rnn_model.compile(optimizer='adam', loss='mean_squared_error')
rnn_model.fit(train_sequences, train_labels, epochs=100, batch_size=64)

train_predictions = price_scaler.inverse_transform(rnn_model.predict(train_sequences))
test_predictions = price_scaler.inverse_transform(rnn_model.predict(test_sequences))
true_train_prices = price_scaler.inverse_transform(train_labels.reshape(-1, 1))
true_test_prices = price_scaler.inverse_transform(test_labels.reshape(-1, 1))

plt.figure(figsize=(12, 6))
plt.plot(range(len(close_prices)), price_scaler.inverse_transform(normalized_prices), color='#00BFFF', label='True Stock Prices')
plt.plot(range(sequence_length, len(train_predictions)+sequence_length), train_predictions, color='#ff7f0e', label='Training Predictions')
plt.plot(range(len(close_prices)-len(test_predictions), len(close_prices)), test_predictions.flatten(), color='#32CD32', label='Test Predictions')
plt.xlabel('Time (Days)')
plt.ylabel('Stock Price (USD)')
plt.title('LSTM Stock Price Prediction')
plt.legend()
plt.show()

