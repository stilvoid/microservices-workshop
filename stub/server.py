from bottle import *

@route("<path:path>")
def not_implemented(path):
    response.status = 501

    return "Not implemented"
