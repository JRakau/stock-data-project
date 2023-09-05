import requests
import time

# dX4gER*E6GN!yEZ */


ticker = "AAPL"
api_key = "74fee5c279404d629efab122626502bb"


def get_stock_quote(ticker_symbol, api):
    """Get a quote for a given ticker symbol using API

    Args:
        ticker_symbol (String): AAPL Apple stocks or  MSFT Microsoft stocks
        api (_type_): API Key to access the API

    Returns:
        _type_: This request will return JSON with the following structure
        {
            "symbol": "AAPL",
            "name": "Apple Inc",
            "exchange": "NASDAQ",
            "mic_code": "XNAS",
            "currency": "USD",
            "datetime": "2021-09-16",
            "timestamp": 1631772000,
            "open": "148.44000",
            "high": "148.96840",
             "low": "147.22099",
            "close": "148.85001",
            "volume": "67903927",
            "previous_close": "149.09000",
            "change": "-0.23999",
            "percent_change": "-0.16097",
            "average_volume": "83571571",
            "rolling_1d_change": "123.123",
            "rolling_7d_change": "123.123",
            "rolling_period_change": "123.123"
            "is_market_open": false,
            "fifty_two_week": {
                "low": "103.10000",
                "high": "157.25999",
                "low_change": "45.75001",
                "high_change": "-8.40999",
                "low_change_percent": "44.37440",
                "high_change_percent": "-5.34782",
                "range": "103.099998 - 157.259995"
            },
            "extended_change": "0.09",
            "extended_percent_change": "0.05",
            "extended_price": "125.22",
            "extended_timestamp": 1649845281
            }
    """
    url = f"https://api.twelvedata.com/quote?symbol={ticker_symbol}&apikey={api}"
    response = requests.get(url).json()
    return response


def main():
    """
    Main routine for app
    It is responsable to run all program functions

    """

    print("\n#############################")
    print("#                           #")
    print("#  Welcome to Your Stocks   #")
    print("#                           #")
    print("#############################\n")
    ticker = input(
        "Enter your ticker symbol here: (Or enter \"quit\" to leave)\n")

    while ticker != "quit":
        stockdata = get_stock_quote(ticker, api_key)
        # print(stockdata)
        print("\n##########################################################")

        print(stockdata['symbol'], " ", stockdata['name'],
              " ", stockdata['open'])
        print("##########################################################\n")
        ticker = input(
            "Enter another ticker symbol here: (Or enter \"quit\" to leave)\n")


main()
