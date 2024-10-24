import stock_yank
import dotenv
import os
import utilities
import webex_message
import time
import sys

dotenv.load_dotenv(sys.path[0] + ".env")

ticker = os.environ.get("ticker").upper().replace(" ", "").split(',')
api_key = os.environ.get("api_key")

#stock_yank.close_yank(ticker, api_key)
date = utilities.determine_date()

for t in ticker:
    if len(ticker) > 4:
        delay = True
    else:
        delay = False
    open = stock_yank.last_close_yank(t, api_key)
    close = stock_yank.close_yank(t, api_key)
    change = utilities.close_diff(open, close)
    message = (f"{t} Open: {str(open)} Close: {str(close)} Change: {change}%")
    webex_message.send_message(message)
    if delay == True:
        time.sleep(15)
