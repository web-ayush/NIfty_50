import yfinance as yf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# Fetch Nifty 50 data
def fetch_data(symbol='^NSEI', start_date='2005-03-31', end_date=None):
    """
    Fetch Nifty 50 data from Yahoo Finance.
    :param symbol: Ticker symbol for Nifty 50
    :param start_date: Start date for fetching data (format: 'YYYY-MM-DD')
    :param end_date: End date for fetching data (default: None for latest data)
    :return: DataFrame with historical data
    """
    data = yf.download(symbol, start=start_date, end=end_date)
    return data

# Calculate moving averages
def calculate_moving_averages(data, short_window=20, long_window=50):
    """
    Calculate short-term and long-term moving averages.
    :param data: DataFrame with historical data
    :param short_window: Window size for short-term moving average
    :param long_window: Window size for long-term moving average
    """
    data['Short_MA'] = data['Close'].rolling(window=short_window).mean()
    data['Long_MA'] = data['Close'].rolling(window=long_window).mean()

# Plot data with moving averages
def plot_data(data):
    """
    Plot the stock price along with moving averages.
    :param data: DataFrame with historical data
    """
    plt.figure(figsize=(12, 6))
    plt.plot(data.index, data['Close'], label='Close Price', color='blue', alpha=0.5)
    plt.plot(data.index, data['Short_MA'], label='20-day MA', color='green')
    plt.plot(data.index, data['Long_MA'], label='50-day MA', color='red')
    
    plt.xlabel('Date')
    plt.ylabel('Price')
    plt.title('Nifty 50 Stock Price Analysis')
    plt.legend()
    plt.grid(True)
    plt.show()

# Calculate and plot daily returns
def plot_daily_returns(data):
    """
    Calculate and plot daily returns.
    :param data: DataFrame with historical data
    """
    data['Daily_Return'] = data['Close'].pct_change()
    plt.figure(figsize=(12, 6))
    plt.plot(data.index, data['Daily_Return'], color='purple', alpha=0.6)
    plt.axhline(y=0, color='black', linestyle='--')
    plt.xlabel('Date')
    plt.ylabel('Daily Return')
    plt.title('Nifty 50 Daily Returns')
    plt.grid(True)
    plt.show()

# Calculate volatility
def plot_volatility(data, window=21):
    """
    Calculate and plot rolling volatility.
    :param data: DataFrame with historical data
    :param window: Rolling window size for volatility calculation
    """
    data['Volatility'] = data['Daily_Return'].rolling(window=window).std() * np.sqrt(252)
    plt.figure(figsize=(12, 6))
    plt.plot(data.index, data['Volatility'], color='orange')
    plt.xlabel('Date')
    plt.ylabel('Volatility')
    plt.title('Nifty 50 Volatility (21-day Rolling)')
    plt.grid(True)
    plt.show()

# Main function
def main():
    """
    Main function to fetch data, calculate metrics, and plot results.
    """
    # Fetch data for the last 20 years
    data = fetch_data(start_date='2005-03-31')
    calculate_moving_averages(data)
    plot_data(data)
    plot_daily_returns(data)
    plot_volatility(data)

if __name__ == '__main__':
    main()