from flask import jsonify


def generic_error(error):
    return jsonify(
        msg=error.description,
        code=error.code), error.code
