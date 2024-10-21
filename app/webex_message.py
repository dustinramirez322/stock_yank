import requests
import dotenv
import os

dotenv.load_dotenv()

bot_token = os.environ.get("bot_token")
roomId = os.environ.get("roomId")


def send_message(message, bot_token=bot_token, roomId=roomId):
    url = 'https://api.ciscospark.com/v1/'
    headers = {'Authorization': 'Bearer ' + bot_token}

    # Message along with the room we want it posted in
    postData = {'roomId': roomId,
                'text': message}

    # Post a message to the selected room
    postMessage = requests.post(url + 'messages', json=postData, headers=headers).json()