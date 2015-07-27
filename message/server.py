from bottle import *

@get("/messages")
def get_messages(mongodb):
    if request.query.get("room"):
        messages = mongodb["messages"].find({
            "room": request.query.get("room")
        })
    else:
        messages = mongodb["messages"].find()

    return {
        "messages": list(messages)
    }

@post("/messages")
def create_message(mongodb):
    new_id = mongodb["messages"].insert(request.json)

    return mongodb["messages"].find_one(new_id)
