import requests
import utilities


def open_yank(ticker, api_key):
    response = requests.get('https://api.polygon.io/v2/aggs/ticker/' + ticker + '/prev?adjusted=true&apiKey=' + api_key).json()
    open = response["results"][0]["o"]
    return open


# Get the market close for a specific ticker
def last_close_yank(ticker, api_key):
    date = utilities.determine_date()
    delta = 1
    response = requests.get('https://api.polygon.io/v1/open-close/' + ticker + '/' + date + '?adjusted=true&apiKey=' + api_key).json()
    if response['status'] != 'OK':
        delta += 1
        date = utilities.determine_date(delta)
        last_close_yank(ticker, api_key)
    else:
        previous_close = response['close']
        return previous_close
