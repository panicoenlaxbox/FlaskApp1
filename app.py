# app.py
import logging
from typing import List

import jsons
import werkzeug
from flask import Flask, Response, request, url_for, render_template, session, render_template_string
from werkzeug.utils import redirect

from utils import binding

app = Flask(__name__)

app.secret_key = 'BAD_SECRET_KEY'

logger = logging.getLogger(__name__)


# class Grault:
#     def __init__(self, garply: str):
#         self.garply = garply
#
#
# class Quux:
#     def __init__(self, corge: str):
#         self.corge = corge
#
#
# class Foo:
#     def __init__(self, bar: str, baz: str, qux: List[str], quux: Quux, grault: List[Grault]):
#         self.bar = bar
#         self.baz = baz
#         self.qux = qux
#         self.quux = quux
#         self.grault = grault
#

@app.route("/")
def hello():
    return render_template_string("<h1>{{ session['name'] }}!</h1>")


@app.route("/goodbye", methods=["GET", "POST"])
def goodbye():
    args: werkzeug.datastructures.ImmutableMultiDict = request.args
    # str if type is not specified
    # None if key is not found and not default value is supplied
    id_ = args.get("id", type=int)
    code = args.get("code", "unknown", type=str)

    if request.method == "GET":
        return "Bye, World! from GET"
    elif request.method == "POST":
        name = request.form["name"]
        return f"Bye, World! from POST, id {id_} and name {name}"


# greet/sergio
@app.route("/greet/<name>")
def greet(name: str):
    # Save name to the session object
    session['name'] = name
    return render_template("sergio.html", name=name)


# @app.route("/say/")
def say():
    url = url_for('greet', name="Carmen")
    logger.warning(url)
    return redirect(url)


app.add_url_rule("/say", view_func=say)

# @app.route("/foo", methods=["GET"])
# def get_foo():
#     foo = Foo("bar", "baz", ["qux", "quux"], Quux("corge"), [Grault("garply"), Grault("walco")])
#     return Response(jsons.dumps(foo), mimetype='application/json')
#
#
# @app.route("/foo", methods=["POST"])
# @binding(Foo)
# def post_foo(foo: Foo):
#     return Response(jsons.dumps(foo), mimetype='application/json')


if __name__ == '__main__':
    app.run(debug=True)
