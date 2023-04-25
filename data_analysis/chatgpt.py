import openai
import json


class ChatGPT:
    def __init__(self, api_key):
        # set up OpenAI API credentials
        openai.api_key = api_key

    def generate_response(self, prompt):
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=prompt,
            max_tokens=1000,
            temperature=0
        )
        return response.choices[0].message.content.strip()


class StockSentimentAnalyzer(ChatGPT):
    def __init__(self, api_key):
        super().__init__(api_key)

    def analyze_stocks_sentiment(self, text):
        prompt = f"""
        Prompt: Read the given text and identify the stocks that are discussed within it. For each stock, analyze the discourse and rate its sentiment on a scale of -5 (strongly negative) to 5 (strongly positive). Additionally, provide the reasons behind your sentiment assessment for each stock. Please return the data in the following JSON format:
        {{
          "stocks": [
            {{
              "stock_symbol": "EXAMPLE",
              "sentiment_rating": 0,
              "reasons": [
                "reason 1",
                "reason 2"
              ]
            }},
            ...
          ]
        }}
        """
        messages = [
            {"role": "system", "content": prompt},
            {"role": "user", "content": text},
        ]
        response = self.generate_response(messages)
        response_dict = json.loads(response)
        return response_dict
