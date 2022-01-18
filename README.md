# Pushnotif

Python cli to send push nofifications using [Pushover](https://pushover.net)

## Installation

This project uses python3+. Install dependences with

```
pip install -r requirements.txt
```

Create a `.env` file in this directory and add this info:
- USER_KEY=INSERTYOURUSERKEYHERE
- APP_KEY=INSERTYOURAPPKEYHERE

You can find your user key on the Pushover home page. To get an app key you'll need to [register an application](https://pushover.net/apps/build) with Pushover

## Sending a push notification
```
python push.py -mes "Hello world" -t "This is a terminal test" -p 1
```

- `-mes`: The body of the push notification
- `-t`: The title of the push notification
- `-p`: The push notification priority. (-1 to 2, with 2 being the highest priority)
