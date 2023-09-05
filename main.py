import requests
import time

# dX4gER*E6GN!yEZ */


ticker = "AAPL"
api_key = "74fee5c279404d629efab122626502bb"


def get_stock_quote(ticker_symbol, api):

    url = f"https://api.twelvedata.com/quote?symbol={ticker_symbol}&apikey={api}"
    response = requests.get(url).json()
    return response


def main():
    """
    Main routine for app
    It is responsable to run all program functions

    """


ticker = input("Enter your ticker symbol here:\n")


stockdata = get_stock_quote(ticker, api_key)

print(stockdata)
print(stockdata['symbol'])

print("Welcome to Your Stocks")

main()
