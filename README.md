# PUSHNOTIF

Python cli to send push nofifications using (Pushover)[https://pushover.net]

## Installation

This project uses python3+. Install dependences with

```
pip install -r requirements.txt
```

## Sending a push notification
python push.py -mes "Hello world" -t "This is a terminal test" -p 1
```

`-mes`: The body of the push notification
`-t`: The title of the push notification
`-p`: The push notification priority. (-1 to 2, with 2 being the highest priority)
