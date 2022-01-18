import os
from dotenv import load_dotenv
import requests
import argparse

load_dotenv()
USER_KEY = os.environ.get("USER_KEY")
APP_KEY = os.environ.get("APP_KEY")

parser = argparse.ArgumentParser(description='Send a push notification using the pushover service')
parser.add_argument('-mes', '--message', type=str, required=True, help='Push notification body')
parser.add_argument('-t','--title', type=str, required=True, help="Title  of push notification")
parser.add_argument('-p','--priority', type=str, required=False, help="Message priority, -1, 0, 1, 2")
parser.add_argument('-url','--push_url', type=str, required=False, help="Push notification url")
args = parser.parse_args()

def send_push(args): 
    headers={
        'Content-Type': 'application/x-www-form-urlencoded',
        'Content-Length': 180
    }
    data = {
        "token": APP_KEY,
        "user": USER_KEY,
        "message": args.message,
        "title": args.title,
        "priority": args.priority
    }
    r = requests.post('https://api.pushover.net/1/messages.json', data=data)
    print(r.text)


send_push(args)
# .text
# print(r)
