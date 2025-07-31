# backtest.py
import pandas as pd
import matplotlib.pyplot as plt

def run_backtest(data, strategy_fn, initial_balance=10000):
    balance = initial_balance
    position = 0
    balance_history = []

    for i in range(len(data)):
        signal = strategy_fn(data.iloc[:i+1])
        price = data.iloc[i]["close"]

        if signal == "buy" and balance > 0:
            position = balance / price
            balance = 0
        elif signal == "sell" and position > 0:
            balance = position * price
            position = 0

        balance_history.append(balance + position * price)

    data["equity"] = balance_history
    return data

def load_historical_data(filepath):
    return pd.read_csv(filepath, parse_dates=["timestamp"])

def plot_equity_curve(data):
    plt.figure(figsize=(12,6))
    plt.plot(data["timestamp"], data["equity"], label="Equity Curve")
    plt.title("Backtest Equity Curve")
    plt.xlabel("Time")
    plt.ylabel("Portfolio Value")
    plt.legend()
    plt.grid()
    plt.tight_layout()
    st.pyplot(plt)
