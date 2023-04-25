import os
import pandas as pd
import streamlit as st
from dotenv import dotenv_values
import json

from data_importer.api_data_downloader import GoogleNewsAPI
from data_analysis.chatgpt import StockSentimentAnalyzer

config = dotenv_values(".env")  # config = {"USER": "foo", "EMAIL": "foo@example.org"}

# RAPIDAPI_KEY = os.environ.get("RAPIDAPI_KEY")
# OPENAI_KEY = os.environ.get("OPENAI_KEY")

# global_market_api = GlobalStockMarketAPI(config["RAPIDAPI_KEY"])
# stock_analysis = global_market_api.get_data()
# stock_analysis_df = pd.DataFrame(stock_analysis)

google_news_api = GoogleNewsAPI()
google_news_data = google_news_api.get_data("stock market")
google_news_df = pd.DataFrame(google_news_data)

text = " ".join(google_news_df["desc"])
stock_analyzer = StockSentimentAnalyzer(config["OPENAI_KEY"])
res = stock_analyzer.analyze_stocks_sentiment(text)

# Streamlit app
st.title("Stock Market Sentiment Dashboard")
st.write("## Google News Data")
st.dataframe(google_news_df)

df = pd.DataFrame(res["stocks"])

st.title("Stock Sentiment Analysis")

# Create a bar chart for sentiment ratings
st.subheader("Sentiment Ratings")
chart_data = df[["stock_symbol", "sentiment_rating"]].set_index("stock_symbol")
st.bar_chart(chart_data)

# Display reasons in a table
st.subheader("Reasons for Sentiment")
for _, row in df.iterrows():
    st.write(f"{row['stock_symbol']} Reasons:")
    reason_data = pd.DataFrame(row["reasons"], columns=["Reasons"])
    st.table(reason_data)