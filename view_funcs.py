from flask import request, current_app

# https://stackoverflow.com/questions/11994325/how-to-divide-flask-app-into-multiple-py-files
# https://www.reddit.com/r/learnpython/comments/27ejz5/from_main_import/
# __main__ is the script where the program was initiated, not necessarily the calling script
from __main__ import app

# from app import app


print(app.name)


@app.route('/books/<genre>')
def books(genre):
    return "All Books in {} category from {} with urls {}".format(genre, request.remote_addr, current_app.url_map)
