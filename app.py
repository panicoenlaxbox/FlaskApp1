from flask import Flask, request, make_response, url_for, redirect, abort, Response

# Every Flask application must have an instance of Flask class.
# The instance is actually a WSGI (Web Server Gateway Interface) application which simply means that the web server
# passes all the requests it receives to this instance for further processing

# Most of the time __name__ is the correct value.
# The name of the application package is used by Flask to find static assets, templates and so on.

print("Sergio")
from utils import requestdata_message

app = Flask(__name__)


# A Route is an act of binding a URL to a view function.
# A view function is simply a function which responds to the request.
@app.route('/')
def index():
    # The view function must return a string. Trying to return something else will result in 500 Internal Server Error.
    return 'Hello World'


# Alternative to @app.route
# The endpoint simply refers to the unique name given to the route,
# typically name of view function is used as an endpoint

# app.add_url_rule(rule='/', endpoint='index', view_func=index)

# Although it's not fail, the first registered route will win
# You can see registered routes with `app.url_map`
# Moreover, you will see an automatic route
#   <Rule '/static/<filename>' (GET, OPTIONS, HEAD) -> static>,
@app.route('/')
def home():
    # automatically converts the string into a response object ( using make_response() method ) with string as the
    # body of the response, HTTP status code of 200 and content-type header set to text/html
    return 'Home Page'


@app.route('/career')
def career():
    res = make_response("Career Page")
    res.headers['Content-Type'] = 'text/plain'
    return res


@app.route('/feedback')
def feedback():
    return 'Feedback Page'


@app.route('/user/<id_>')
def user_profile(id_):
    # Creating Response using Tuples
    # (response, status, headers)
    # (response, headers)
    # (response, status)
    return "Profile page of user #{}".format(id_), 200, {'Content-Type': 'text/markdown'}


@app.route("/redirect")
def a_redirect():
    # endpoint is the unique name given to URL and most of the time it is the name of the view function
    # url = url_for(endpoint="feedback")
    # url = url_for(endpoint="user_profile", id_=2)
    url = url_for(endpoint="user_profile", id_=2, a_param="a_value", _external=True)
    # generate the absolute URLs and with a extra param that will be appended to query string
    # http://127.0.0.1:5000/user/2?a_param=a_value
    return redirect(url)


@app.route("/abort")
def a_abort():
    # abort(500)  # @app.errorhandler(500) will be executed
    abort(Response(response="Sergio", status=500))  # @app.errorhandler(500) will not be executed
    print(i)  # this code will not be executed


@app.route('/orders/<int:id_>')
def order_details(id_: int):
    # Without type constraint, id_ will be str
    print(type(id_))
    return "Order details #{}".format(id_)


@app.route('/fail')
def fail():
    name = "Sergio"
    print(i)
    return f"Hello {name}"


@app.route('/requestdata')
def requestdata():
    return requestdata_message()


# it does not work if we have Debug = True
@app.errorhandler(500)
def http_500_handler(error):
    # error.code  # 500
    # error.description  # 'The server encountered an internal error and was unable to complete your request.
    #   Either the server is overloaded or there is an error in the application.'
    # error.name  # Internval Server Error
    # error.original_exception  # name 'i' is not defined
    return f"<p>A critical HTTP 500 Error encountered {error}</p>", 500


# Hook points

# registers a function to execute before the first request is handled
@app.before_first_request
def before_first_request():
    print("before_first_request() called")


# registers a function to execute before a request is handled
# if the function registered by before_request decorator returns a response then the request handler will not be called.
@app.before_request
def before_request():
    print("before_request() called")


# registers a function to execute after a request is handled. The registered function will not be called in case an
# unhandled exception occurred in the request handler. The function must accept a response object and return
# the same or new response
@app.after_request
def after_request(response):
    print("after_request() called")
    return response


# Similar to after_request decorator but the registered function will always execute regardless of whether
# the request handler throws an exception or not
@app.teardown_request
def teardown_request(response):
    print("teardown_request() called")
    return response


# end hook points

if __name__ == "__main__":
    print(app.url_map)
    app.run(debug=True)
