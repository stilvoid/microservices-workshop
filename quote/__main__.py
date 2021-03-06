from bottle import hook, install, response, route, run
from bottle.ext.mongo import MongoPlugin

import server

# Borrowed from https://gist.github.com/richard-flosi/3789163
@hook('after_request')
def enable_cors():
    """
    You need to add some headers to each request.
    Don't use the wildcard '*' for Access-Control-Allow-Origin in production.
    """
    response.headers['Access-Control-Allow-Origin'] = '*'
    response.headers['Access-Control-Allow-Methods'] = 'PUT, GET, POST, DELETE, OPTIONS'
    response.headers['Access-Control-Allow-Headers'] = 'Origin, Accept, Content-Type, X-Requested-With, X-CSRF-Token'

@route("<path:path>", method=["OPTIONS"])
def options(path):
    return "Yeah it's fine mate."

install(MongoPlugin(uri="mongodb://db", db="quotes", json_mongo=True))
run(host="0.0.0.0", port=8000, reloader=True, debug=True)
