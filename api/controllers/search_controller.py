from flask import Blueprint, abort, jsonify, request

searching = Blueprint('searching', __name__)
_searcher_service = None

add_user_attributes = [
    'username', 'name', 'title', 'position', 'summary', 
    'skills', 'experience', 'education'
]

searchable_attributes = [
    'name', 'title', 'position', 'summary', 'skills'
]

def init_searching(searcher_service):
    global _searcher_service
    _searcher_service = searcher_service

@searching.route('/', methods=['GET'])
def test():
    return "Hello world!"

@searching.route('/add', methods=['GET', 'POST'])
def add_profile():
    _validate_add_parameters(request.args)
    _searcher_service.add_public_profile(request.args)
    return "Successfully added user."

def _validate_add_parameters(parameters):
    if set(parameters) != set(add_user_attributes):
        abort(400, "Invalid parameters.")

@searching.route('/search', methods=['GET'])
def get_profiles():
    _validate_search_parameters(request.args)
    return jsonify(_searcher_service.search_profiles(request.args))

def _validate_search_parameters(parameters):
    for parameter in parameters:
        if parameter not in searchable_attributes:
            abort(400, "Invalid parameters.")
        