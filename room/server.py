from bottle import *

@get("/rooms")
def get_rooms(mongodb):
    return {
        "rooms": [
            {
                "id": "room id 1",
                "name": "room name 1",
                "title": "room title 1"
            },
            {
                "id": "room id 2",
                "name": "room name 2",
                "title": "room title 2"
            }
        ]
    }

@post("/rooms")
def create_room(mongodb):
    return {
        "id": "new room id",
        "name": "new room name",
        "title": "new room title"
    }

@get("/users")
def get_users(mongodb):
    return {
        "users": [
            {
                "id": "user id 1",
                "name": "user name 1"
            },
            {
                "id": "user id 2",
                "name": "user name 2"
            }
        ]
    }

@post("/users")
def create_user(mongodb):
    return {
        "id": "new user id",
        "name": "new user name"
    }
