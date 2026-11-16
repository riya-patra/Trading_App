import streamlit as st

st.set_page_config(
    page_title = "Trading_App",
            page_icon = ":chart_with_downwards_trend:",
            layout = "wide"
        )
st.title("Trading Guide App :bar_chart:")
st.header("We provide the greatest platform for you to collect all information prior to investing in stocks.")
st.image("C:\cover image\Cover-Image.jpg")
    
st.markdown("## We provide the following services:")

st.markdown("## :one: Stock Information")
st.write("Through this page, you can see all the information about stock.")

st.markdown("## :two: Stock Prediction")
st.write("You can explore predicted closing prices for the next 30 days based on historical stock data advanced forecasting models. Use this tool to gain valuable insights into market trends" \
"and make trends and make informed investment decisions")

st.markdown("## :three: CAPM")
st.write("Discover how the Capital asset Pricing model(CAPM) calculates the expected return of different stocks asset based on its risk and market performance.Calculates Beta and Expected Return individual Stocks.")


