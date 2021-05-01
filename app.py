# app.py
from typing import List

import jsons
from flask import Flask, Response

from utils import binding

app = Flask(__name__)


class Grault:
    def __init__(self, garply: str):
        self.garply = garply


class Quux:
    def __init__(self, corge: str):
        self.corge = corge


class Foo:
    def __init__(self, bar: str, baz: str, qux: List[str], quux: Quux, grault: List[Grault]):
        self.bar = bar
        self.baz = baz
        self.qux = qux
        self.quux = quux
        self.grault = grault


@app.route("/")
def hello():
    return "Hello, World!"


@app.route("/foo", methods=["GET"])
def get_foo():
    foo = Foo("bar", "baz", ["qux", "quux"], Quux("corge"), [Grault("garply"), Grault("walco")])
    return Response(jsons.dumps(foo), mimetype='application/json')


@app.route("/foo", methods=["POST"])
@binding(Foo)
def post_foo(foo: Foo):
    return Response(jsons.dumps(foo), mimetype='application/json')


if __name__ == '__main__':
    app.run()
