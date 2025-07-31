# -*- coding: utf-8 -*-
# dashboard.py
import streamlit as st
from live_trader import LiveTrader
from backtest import run_backtest, load_historical_data, plot_equity_curve
from optimizer import optimize_strategy
from training import train_model, engineer_features
import pandas as pd

def launch_dashboard():
    st.set_page_config(page_title="Kronos AI Dashboard", layout="wide")
    st.title("Kronos AI Quant Trading System")

    tab1, tab2, tab3, tab4 = st.tabs(["Live Trading", "Backtesting", "Optimization", "Training"])

    with tab1:
        st.header("Live Trading")
        if st.button("Start Live Trader"):
            trader = LiveTrader()
            trader.trade()  # runs in loop; should be async or subprocess in production

    with tab2:
        st.header("Backtest Strategy")
        file = st.file_uploader("Upload historical CSV", type=["csv"])
        if file:
            df = pd.read_csv(file, parse_dates=["timestamp"])
            from strategies import get_strategy
            strat = get_strategy("macd_rsi")
            result = run_backtest(df, strat)
            plot_equity_curve(result)

    with tab3:
        st.header("Optimize Strategy Parameters")
        file = st.file_uploader("Upload CSV for Optimization", type=["csv"], key="opt")
        if file:
            df = pd.read_csv(file, parse_dates=["timestamp"])
            param_grid = [
                {"macd_fast": 12, "macd_slow": 26, "rsi_period": 14},
                {"macd_fast": 8, "macd_slow": 21, "rsi_period": 10},
                {"macd_fast": 5, "macd_slow": 20, "rsi_period": 8},
            ]
            best_params, best_score, _ = optimize_strategy(df, "macd_rsi", param_grid)
            st.success(f"Best Params: {best_params} | Final Equity: {best_score:.2f}")

    with tab4:
        st.header("Train Strategy Model")
        file = st.file_uploader("Upload Historical CSV for Training", type=["csv"], key="train")
        if file:
            df = pd.read_csv(file, parse_dates=["timestamp"])
            df = engineer_features(df)
            train_model(df)
            st.success("Model trained and saved!")

if __name__ == "__main__":
    launch_dashboard()
