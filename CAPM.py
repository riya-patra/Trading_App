# importing libraries

import streamlit as st
import pandas as pd
import numpy as np
import yfinance as yf
import plotly.express as px

st.set_page_config(page_title="CAPM",
    page_icon="chart_with_upwards_trend",
    layout='wide')

st.title("Capital Asset Pricing Model")

# getting input from user

col1, col2 = st.columns([1, 1])
with col1:
    stocks_list = st.multiselect(
        "Choose 4 stocks",
        ('TSLA', 'AAPL', 'NFLX', 'MSFT', 'MGM', 'AMZN', 'NVDA', 'GOOGL'),
        ['TSLA', 'AAPL', 'AMZN', 'GOOGL']
    )
with col2:
    year = int(st.number_input("Number of years", 1, 10))

if not stocks_list:
    st.warning("Please select at least one stock.")
    st.stop()

# ---------- helper functions ----------

def get_close(ticker, years):
    """Download closing prices of one ticker from Yahoo Finance."""
    data = yf.download(ticker, period=f'{years}y', auto_adjust=True, progress=False)
    close = data['Close']
    if isinstance(close, pd.DataFrame):      # newer yfinance returns a DataFrame
        close = close.iloc[:, 0]
    close.index = pd.to_datetime(close.index).tz_localize(None).normalize()
    return close

def interactive_plot(df):
    fig = px.line()
    for col in df.columns[1:]:               # skip the 'Date' column
        fig.add_scatter(x=df['Date'], y=df[col], name=col)
    fig.update_layout(margin=dict(l=20, r=20, t=50, b=20),
                      legend=dict(orientation='h', yanchor='bottom',
                                  y=1.02, xanchor='right', x=1))
    return fig

def normalize(df):
    df = df.copy()
    for col in df.columns[1:]:
        df[col] = df[col] / df[col].iloc[0]  # every series starts at 1
    return df

def daily_return(df):
    df_daily = df.copy()
    for col in df.columns[1:]:
        df_daily[col] = df[col].pct_change() * 100   # % change from previous day
    df_daily.iloc[0, 1:] = 0                         # first day has no previous day
    return df_daily

def calculate_beta(df, stock):
    b, a = np.polyfit(df['sp500'], df[stock], 1)     # slope = beta, intercept = alpha
    return b, a

# ---------- downloading data ----------

# SP500 (replaces pandas_datareader / FRED)
SP500 = get_close('^GSPC', year).to_frame('sp500')

# selected stocks
stocks_df = pd.DataFrame()
for stock in stocks_list:
    stocks_df[stock] = get_close(stock, year)

# make 'Date' a normal column and merge stocks with SP500
stocks_df.reset_index(inplace=True)
SP500.reset_index(inplace=True)
stocks_df.columns = ['Date'] + list(stocks_df.columns[1:])
SP500.columns = ['Date', 'sp500']

stocks_df = pd.merge(stocks_df, SP500, on='Date', how='inner')

# ---------- showing head and tail ----------

col1, col2 = st.columns([1, 1])
with col1:
    st.markdown("### Dataframe head")
    st.dataframe(stocks_df.head())
with col2:
    st.markdown("### Dataframe tail")
    st.dataframe(stocks_df.tail())

# ---------- price charts ----------

st.markdown("### Price of all the Stocks")
st.plotly_chart(interactive_plot(stocks_df))

st.markdown("### Price of all the Stocks (After Normalizing)")
st.plotly_chart(interactive_plot(normalize(stocks_df)))

# ---------- daily returns and beta ----------

stocks_daily_return = daily_return(stocks_df)

beta = {}
for stock in stocks_list:
    b, a = calculate_beta(stocks_daily_return, stock)
    beta[stock] = b

beta_df = pd.DataFrame({
    'Stock': list(beta.keys()),
    'Beta Value': [round(v, 2) for v in beta.values()]
})

# ---------- CAPM expected return:  Ri = Rf + Beta * (Rm - Rf) ----------

rf = 0                                              # risk-free rate (same as the tutorial)
rm = stocks_daily_return['sp500'].mean() * 252      # market return per year (252 trading days)

return_df = pd.DataFrame({
    'Stock': list(beta.keys()),
    'Return Value (%)': [round(rf + v * (rm - rf), 2) for v in beta.values()]
})

c1, c2 = st.columns([1, 1])
with c1:
    st.markdown("### Calculated Beta Value")
    st.dataframe(beta_df)
with c2:
    st.markdown("### Calculated Return using CAPM")
    st.dataframe(return_df)