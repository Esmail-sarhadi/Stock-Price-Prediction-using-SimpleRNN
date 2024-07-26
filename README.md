

# 📈 Stock Price Prediction using SimpleRNN

This project implements a stock price prediction model using a Recurrent Neural Network (RNN) in Python. The model is trained on historical stock price data to forecast future prices. The key steps include data preprocessing, model training, and visualization of predictions.

## 📑 Table of Contents
- [⚙️ Installation](#installation)
- [🚀 Usage](#usage)
- [📂 Project Structure](#project-structure)
- [📊 Data Preprocessing](#data-preprocessing)
- [🏗️ Model Architecture](#model-architecture)
- [🔄 Training](#training)
- [📉 Visualization](#visualization)
- [📈 Results](#results)
- [🤝 Contributing](#contributing)
- [📄 License](#license)

## ⚙️ Installation

To run this project, you need to have Python 3.x installed along with the necessary libraries. You can install the required libraries using:

```bash
pip install numpy pandas matplotlib keras scikit-learn
```

## 🚀 Usage

1. Clone this repository:
    ```bash
    git clone https://github.com/esmail-sarhadi/Stock-Price-Prediction-using-SimpleRNN.git
    ```
2. Navigate to the project directory:
    ```bash
    cd stock-price-prediction
    ```
3. Place your dataset (`dataset.csv`) in the project directory.
4. Run the script:
    ```bash
    python main.py
    ```

## 📂 Project Structure

- `main.py`: Main script containing the code for data preprocessing, model training, and visualization.
- `dataset.csv`: CSV file containing the historical stock price data.

## 📊 Data Preprocessing

The dataset is loaded and the 'open' prices are extracted. The prices are normalized using MinMaxScaler. The data is then split into training and testing sets. Sequences of a specified length are created for the model input.

## 🏗️ Model Architecture

The model is built using Keras and consists of:
- A SimpleRNN layer with 50 units
- A Dense layer with 1 unit for the output

The model uses the Adam optimizer and mean squared error loss function.

## 🔄 Training

The model is trained for 100 epochs with a batch size of 64. The training data consists of sequences of 7 days, and the model learns to predict the price of the next day.

## 📉 Visualization

The true stock prices and the model predictions for both training and testing sets are plotted for comparison.

## 📈 Results

The model's performance is visualized through plots, showing the comparison between actual stock prices and the predicted values for both the training and testing data.

## 🤝 Contributing

Contributions are welcome! Please open an issue or submit a pull request for any changes.

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 📝 Description

This project showcases a machine learning model to predict stock prices using historical data. By utilizing a SimpleRNN, the model learns from past stock prices and forecasts future trends, providing valuable insights for stock market analysis and trading strategies.

<a href="https://nowpayments.io/donation?api_key=REWCYVC-A1AMFK3-QNRS663-PKJSBD2&source=lk_donation&medium=referral" target="_blank">
     <img src="https://nowpayments.io/images/embeds/donation-button-black.svg" alt="Crypto donation button by NOWPayments">
</a>

