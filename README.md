# 📈 Trading App: Stock Analysis, Prediction & CAPM

A multi-page **Streamlit** web app for analysing stocks, forecasting prices and estimating expected returns with the **Capital Asset Pricing Model (CAPM)**. Market data comes live from Yahoo Finance.

## 🔍 Features

### 1. Stock Analysis
- Interactive candlestick and line charts
- Technical indicators: **RSI**, **MACD**, **Moving Averages**
- Built with Plotly

### 2. Stock Prediction
- Forecasts future closing prices using a model trained in `model_train.py`
- Shows the forecast as an interactive chart

### 3. CAPM 
- Choose stocks (TSLA, AAPL, NFLX, MSFT, MGM, AMZN, NVDA, GOOGL) and the number of years (1-10)
- Downloads closing prices of the stocks and the **S&P 500 (^GSPC)** using `yfinance`
- Charts of raw prices and **normalized prices** (all start at 1) for fair comparison
- Calculates **daily returns** and **Beta** for each stock
- Computes the **expected return** with the CAPM formula:

```
Ri = Rf + β × (Rm − Rf)
```

| Symbol | Meaning |
|--------|---------|
| Ri | Expected return of the stock |
| Rf | Risk-free rate |
| β | Stock's sensitivity to the market (slope of stock returns vs S&P 500 returns) |
| Rm | Expected market return (average daily return × 252 trading days) |

## 🛠️ Tech Stack

Python · Streamlit · pandas · NumPy · yfinance · Plotly · pandas_ta · scikit-learn

## 📸 Screenshots

| Stock Analysis | CAPM | Stock Prediction | Trading Guide App   |
|---|---|---|---|
| ![Stock Analysis](screenshots/Stock_Analysis.png) | ![CAPM](screenshots/CAPM.png) |![Stock Prediction](screenshots/Stock_Prediction.png) | ![Trading Guide App](screenshots/Trading_Guide_App.png)

## 🚀 How to Run

1. **Clone the repository**
   ```bash
   git clone https://github.com/<your-username>/Trading_App.git
   cd Trading_App
   ```

2. **Install the requirements**
   ```bash
   python -m pip install -r requirements.txt
   ```

3. **Start the app**
   ```bash
   streamlit run Trading_App.py
   ```

4. Open `http://localhost:8501` in your browser.

## 📁 Project Structure

```
Trading_App/
├── Trading_App.py          # Home page
├── model_train.py          # Model training for prediction
├── requirements.txt
└── pages/
    ├── Stock_Analysis.py   # Charts and technical indicators
    ├── Stock_Prediction.py # Price forecasting
    ├── CAPM_Return.py      # Beta and CAPM expected return
    └── utils/
        └── plotly_figure.py  # RSI, MACD, Moving Average chart functions
```

## 📝 Notes

- Data is fetched from Yahoo Finance via `yfinance`, so an internet connection is required.
- The S&P 500 data comes from `yfinance` (`^GSPC`) instead of `pandas_datareader`, which is outdated and breaks on newer Python versions.
- The risk-free rate is set to 0 by default; change `rf` in `CAPM.py` to use a realistic value.
- This project is for **learning purposes only** and is not financial advice.

## 👩‍💻 Author

**Riya Patra**
B.Tech CSE | Data Analyst

🔗 LinkedIn: <https://www.linkedin.com/in/riya-patra-95310b332>

📧 Email: <riyapatra368@gmail.com>
