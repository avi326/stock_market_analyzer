# Stock Market Sentiment Dashboard

This is a Streamlit app that provides an overview of the stock market sentiment based on recent Google News articles. The app analyzes the sentiment of stock market-related news articles, and displays a bar chart to visualize the sentiment ratings for each stock, as well as a table with reasons behind each sentiment.

![Dashboard Screenshot](a.png)

## Dependencies

The app requires the following Python packages:

- pandas
- streamlit
- python-dotenv
- google_news_python
- openai

Install the dependencies with the following command:


## Configuration

The app requires a `.env` file in the project root directory with the following keys:

- `RAPIDAPI_KEY`: Your RapidAPI key for accessing Global Stock Market API.
- `OPENAI_KEY`: Your OpenAI API key for using the ChatGPT language model.

## Usage

To run the Streamlit app, navigate to the project directory and execute the following command:


## Code Overview

The app performs the following tasks:

1. Imports necessary modules and packages.
2. Loads the API keys from the `.env` file.
3. Retrieves stock market-related news articles using the `GoogleNewsAPI` class.
4. Performs sentiment analysis on the collected news articles using the `StockSentimentAnalyzer` class.
5. Displays the Google News Data in a table.
6. Displays a bar chart of sentiment ratings for each stock.
7. Displays a table with reasons behind each sentiment.

## Customization

To analyze a different set of news articles or change the search query, update the argument passed to the `get_data()` method in the `GoogleNewsAPI` class instantiation:

```python
google_news_data = google_news_api.get_data("<your-search-query>")