import os
import pandas as pd

from data_importer.api_data_downloader import GoogleNewsAPI
from data_analysis.chatgpt import StockSentimentAnalyzer


RAPIDAPI_KEY = os.environ.get("RAPIDAPI_KEY")
OPENAI_KEY = os.environ.get("OPENAI_KEY")


# global_market_api = GlobalStockMarketAPI(RAPIDAPI_KEY)
# stock_analysis = global_market_api.get_data()
# stock_analysis_df = pd.DataFrame(stock_analysis)

google_news_api = GoogleNewsAPI()
google_news_data = google_news_api.get_data("stock market")
google_news_df = pd.DataFrame(google_news_data)

###############################

text = " ".join(google_news_df["desc"])
stock_analyzer = StockSentimentAnalyzer(OPENAI_KEY)
res = stock_analyzer.analyze_stocks_sentiment(text)

print(text)
print("chatgpt: ")
print(res)