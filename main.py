import requests
import time
from typing import List

# dX4gER*E6GN!yEZ */


api_key = "74fee5c279404d629efab122626502bb"


class MyStock:
    """
    My Stock class
    """

    def __init__(self, symbol, name, high_price):
        # instance attribute
        self.symbol = symbol
        self.name = name
        self.high_price = high_price


def equal_MyStock(a: MyStock, b: MyStock):
    return a.symbol == b.symbol and a.symbol == b.symbol


def remove_object_for(myStocks: List[MyStock]):
    result: List[MyStock] = []
    for current in myStocks:
        found = False
        for stored in result:
            if equal_MyStock(current, stored):
                found = True
        if found is False:
            result.append(current)
    return result


def get_stock_quote(ticker, key):
    """Get a quote for a given ticker symbol using API

    Args:
        ticker (String): AAPL Apple stocks or  MSFT Microsoft stocks
        key (String): API Key to access the API

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
    url = f"https://api.twelvedata.com/quote?symbol={ticker}&apikey={key}"
    response = 0
    try:
        response = requests.get(url).json()
    except Exception as err:
        print(f"Unexpected on get_stock_quote() {err=}, {type(err)=}")
        print("Oops! Try again...")

    return response


def main():
    """
    Main routine for app
    It is responsable to run all program functions

    """
    list_stocks = 0
    ojt_list_stock = 0
    list_stocks = []
    list_stocks2 = []
    ticker_input = 0

    ticker_input = input(
        "Enter your ticker symbol here: (Or enter \"quit(q)\" to leave)\n")

    while ticker_input != "quit" and ticker_input != "q":
        try:
            stockdata = 0
            ojt_list_stock = 0

            stockdata = get_stock_quote(ticker_input, api_key)

            # if (list_stocks.index(stockdata['symbol'])):
            # ß    print("item ja registrado...")

            # list_stocks.insert(stockdata['symbol'], MyStock(
            #    stockdata['symbol'], stockdata['name'], stockdata['high']))
            is_duplicate = 0
            if list_stocks:
                for ojt_list_stock in list_stocks:
                    if ojt_list_stock.symbol not in stockdata['symbol']:
                        print("Not duplicated")
                    else:
                        print("Duplicate symbol")
                        is_duplicate += 1

                    print(
                        f"old {ojt_list_stock.symbol} new {stockdata['symbol']} {is_duplicate}")

                if not is_duplicate:
                    list_stocks.append(
                        MyStock(stockdata['symbol'], stockdata['name'], stockdata['high']))
                    print("Stock added")
            else:
                list_stocks.append(
                    MyStock(stockdata['symbol'], stockdata['name'], stockdata['high']))
                print("Stock added")

            print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
            print("\n##########################################################")

            for ojt_list_stock in list_stocks:
                print(ojt_list_stock.symbol, ojt_list_stock.high_price,
                      ojt_list_stock.name, sep=' ')

            print("##########################################################\n")
            ticker_input = input(
                "Enter another ticker symbol here: (Or enter \"quit(q)\" to leave)\n")

        except OSError as err:
            print("OS error:", err)
            break
        except ValueError:
            print("Could not convert data to an integer.")
            break
        except Exception as err:
            print(f"Unexpected {err=}, {type(err)=}")
            print("Oops!  That was no valid number.  Try again...")
            break


"""
Call Main function
"""
print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
print("#############################")
print("#                           #")
print("#  Welcome to My Stocks     #")
print("#                           #")
print("#############################")
print("\n\n\n")
main()
