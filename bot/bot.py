"""
Quote bot
"""

import json
import os
import sys
import time

import requests

while True:
    try:
        response = requests.get("{}/messages".format(os.environ["MESSAGE_API_URL"]))
    except Exception as e:
        print("ERR:", e)
        time.sleep(1)
        continue

    last_message = response.json()["messages"][-1]["id"]

    break

while True:
    time.sleep(1)

    try:
        response = requests.get("{}/messages".format(os.environ["MESSAGE_API_URL"]))
    except Exception as e:
        print("ERR:", e)
        continue

    seen_last = False

    for row in response.json()["messages"]:
        if row["id"] == last_message:
            seen_last = True
            continue

        if not seen_last:
            continue

        if row["text"] == "!quote":
            try:
                quote = requests.get("{}/quote".format(os.environ["QUOTE_API_URL"]))
            except Exception as e:
                print("ERR:", e)
                continue

            try:
                post_response = requests.post("{}/messages".format(os.environ["MESSAGE_API_URL"]),
                    headers={
                        "Content-Type": "application/json",
                    },
                    data=json.dumps({
                        "user": os.environ["USER_ID"],
                        "room": row["room"],
                        "text": quote.text,
                    })
                )

                print(post_response, post_response.text)
                sys.stdout.flush()
            except Exception as e:
                print("ERR:", e)
                continue

    last_message = response.json()["messages"][-1]["id"]
