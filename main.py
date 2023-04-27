import os
import pandas as pd
import streamlit as st
from dotenv import dotenv_values

from data_importer.api_data_downloader import GoogleNewsAPI
from data_analysis.chatgpt import StockSentimentAnalyzer


def main():
    config = dotenv_values(".env")

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

    # Display reasons in a table
    st.subheader("Reasons for Sentiment")

    # Create two columns with equal width
    col1, col2 = st.columns(2)

    # Display the bar chart in the first column
    with col1:
        st.bar_chart(chart_data)

    # Loop through the DataFrame and display the reasons table in the second column
    with col2:
        for _, row in df.iterrows():
            st.write(f"{row['stock_symbol']} Reasons:")
            reason_data = pd.DataFrame(row["reasons"], columns=["Reasons"])
            st.table(reason_data)


if __name__ == "__main__":
    main()
