import stock_yank
import dotenv
import os

dotenv.load_dotenv()

ticker = os.environ.get("ticker").upper().replace(" ", "").split(',')
api_key = os.environ.get("api_key")

stock_yank.close_yank(ticker, api_key)
