from bottle import install, run
from bottle.ext.mongo import MongoPlugin

import server

install(MongoPlugin(uri="mongodb://db", db="quotes", json_mongo=True))
run(host="0.0.0.0", port=8000, reloader=True, debug=True)
