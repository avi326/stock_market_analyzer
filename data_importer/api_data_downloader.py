import os
import requests
import pandas as pd
from GoogleNews import GoogleNews


class StockAPI:
    def __init__(self, rapidapi_key):
        self.rapidapi_key = rapidapi_key

    def get_data(self, **kwargs):
        raise NotImplementedError


class YahooFinanceAPI(StockAPI):
    def __init__(self, rapidapi_key):
        super().__init__(rapidapi_key)
        self.url = "https://apidojo-yahoo-finance-v1.p.rapidapi.com/stock/v2/get-summary"
        self.headers = {
            'X-RapidAPI-Host': "apidojo-yahoo-finance-v1.p.rapidapi.com",
            'X-RapidAPI-Key': self.rapidapi_key
        }

    def get_data(self, stock_symbol):
        params = {'symbol': stock_symbol, 'region': 'US'}
        response = requests.get(self.url, headers=self.headers, params=params)
        return response.json()


class BloombergAPI(StockAPI):
    def __init__(self, rapidapi_key):
        super().__init__(rapidapi_key)
        self.url = "https://bloomberg-market-and-financial-news.p.rapidapi.com/news/list"
        self.headers = {
            'X-RapidAPI-Host': "bloomberg-market-and-financial-news.p.rapidapi.com",
            'X-RapidAPI-Key': self.rapidapi_key
        }

    def get_data(self, stock_symbol):
        params = {'tickers': stock_symbol}
        response = requests.get(self.url, headers=self.headers, params=params)
        return response.json()


class GlobalStockMarketAPI(StockAPI):
    def __init__(self, rapidapi_key):
        super().__init__(rapidapi_key)
        self.url = "https://global-stock-market-api-data.p.rapidapi.com/news/latest_news"
        self.headers = {
            'X-RapidAPI-Host': "global-stock-market-api-data.p.rapidapi.com",
            'X-RapidAPI-Key': self.rapidapi_key
        }

    def get_data(self):
        response = requests.get(self.url, headers=self.headers)
        return response.json()

class GoogleNewsAPI(StockAPI):
    def __init__(self):
        super().__init__(None)
        self.googlenews = GoogleNews(lang='en', period='7d')

    def get_data(self, stock_symbol, query=None):
        if query:
            self.googlenews.search(query)
        else:
            self.googlenews.search(stock_symbol)

        return self.googlenews.results()

if __name__ == "__main__":

    yahoo_finance_api = YahooFinanceAPI(RAPIDAPI_KEY)
    yahoo_finance_data = yahoo_finance_api.get_data("AAPL")
    print("Yahoo Finance API Data:")
    df = pd.DataFrame(yahoo_finance_data)
    print(df)

    bloomberg_api = BloombergAPI(RAPIDAPI_KEY)
    bloomberg_data = bloomberg_api.get_data("AAPL")
    print("Bloomberg API Data:")
    df = pd.DataFrame(bloomberg_data)
    print(df)

    global_stock_api = GlobalStockMarketAPI(RAPIDAPI_KEY)
    global_stock_data = global_stock_api.get_data()
    print("Global Stock Market API Data:")
    df = pd.DataFrame(global_stock_data)
    print(df)
    google_news_api = GoogleNewsAPI()
    google_news_data = google_news_api.get_data("AAPL")
    print("Google News API Data:")
    df = pd.DataFrame(google_news_data)
    print(df)