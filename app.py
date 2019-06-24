#!flask/bin/python
import flask

import searcher

app = flask.Flask(__name__)
linkedin_searcher = searcher.LinkedInSearcher()

@app.route('/users', methods=['GET', 'POST'])
def add_profile():
    linkedin_searcher.add_public_profile(flask.request.args)
    return "Successfully added user."

@app.route('/search', methods=['GET'])
def get_data():
    return flask.jsonify(linkedin_searcher.search_profiles(flask.request.args))

if __name__ == '__main__':
    app.run(debug=True)