from bottle import *

@get("/quote")
def get_messages():
    return "A random quote"
