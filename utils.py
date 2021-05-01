from functools import wraps
from typing import Any

import jsons
from flask import request


def binding(class_):
    """https://stackoverflow.com/a/30721433"""

    def outer_wrapper(func):
        @wraps(func)
        def inner_wrappper(*args, **kwargs):
            json_data = request.get_json()
            obj = None
            if json_data is not None:
                obj = jsons.load(json_data, class_)
            return func(obj, *args, **kwargs)
        return inner_wrappper
    return outer_wrapper
