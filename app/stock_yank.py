import requests
import dotenv
import os
import time

dotenv.load_dotenv()

bot_token = os.environ.get("bot_token")
roomId = os.environ.get("roomId")

def close_yank(ticker, api_key):
    if len(ticker) > 4:
        delay = True
    else:
        delay = False
    for t in ticker:
        response = requests.get('https://api.polygon.io/v2/aggs/ticker/' + t + '/prev?adjusted=true&apiKey=' + api_key).json()
        open = response["results"][0]["o"]
        close = response["results"][0]["c"]
        change = close_diff(open, close)
        message = (f"{t} Open: {str(open)} Close: {str(close)} Change: {change}%")
        send_message(bot_token, message, roomId)
        if delay == True:
            time.sleep(15)


def close_diff(open, close):
    change = ((close-open)/open)*100
    change_percent = "{:.2f}".format(change)
    return change_percent


def send_message(bot_token, message, roomId):
    url = 'https://api.ciscospark.com/v1/'
    headers = {'Authorization': 'Bearer ' + bot_token}

    # Message along with the room we want it posted in
    postData = {'roomId': roomId,
                'text': message}

    # Post a message to the selected room
    postMessage = requests.post(url + 'messages', json=postData, headers=headers).json()

