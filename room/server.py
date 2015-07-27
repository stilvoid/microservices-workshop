from bottle import *

@get("/rooms")
def get_rooms(mongodb):
    return {
        "rooms": list(mongodb["rooms"].find())
    }

@post("/rooms")
def create_room(mongodb):
    new_id = mongodb["rooms"].insert(request.json)

    return mongodb["rooms"].find_one(new_id)

@get("/users")
def get_users(mongodb):
    return {
        "users": list(mongodb["users"].find())
    }

@post("/users")
def create_user(mongodb):
    new_id = mongodb["users"].insert(request.json)

    return mongodb["users"].find_one(new_id)
