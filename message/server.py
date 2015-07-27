from bottle import *

@get("/messages")
def get_messages(mongodb):
    return {
        "messages": [
            {
                "id": "message id 1",
                "user": "user id 1",
                "room": "room id 1",
                "text": "message text 1"
            },
            {
                "id": "message id 2",
                "user": "user id 2",
                "room": "room id 2",
                "text": "message text 2"
            }
        ]
    }

@post("/messages")
def create_message(mongodb):
    return {
        "id": "room id",
        "user": "user id",
        "room": "room id",
        "text": "message text"
    }
