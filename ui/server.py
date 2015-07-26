"""
UI Service
"""

import os

from bottle import get, template, run

@get("/")
def index():
    return template("page", {
        "room": os.environ.get("ROOM_API_URL"),
        "message": os.environ.get("MESSAGE_API_URL"),
    })

if __name__ == "__main__":
    run(host="0.0.0.0", port=8000, debug=True)
