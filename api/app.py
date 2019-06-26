#!flask/bin/python
from flask import Flask

from api.controllers.search_controller import searching, init_searching

class SearcherApiServer:
    def __init__(self, searcher_service):
        self._searcher_service = searcher_service
        self._app = Flask(__name__)
        self._init_routes()

    def _init_routes(self):
        self._app.register_blueprint(searching, url_prefix='/users')
        init_searching(self._searcher_service)

    def run(self):
        self._app.run()