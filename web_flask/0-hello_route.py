#!/usr/bin/python3
"""Flask Application for AirBnB_V2"""

from flask import Flask


app = Flask(__name)


@app.route("/", strict_slashes=False)
def hello_hbnb():
    """
    Route for URL, prints a welcome message
    """
    return "Hello HBNB!"

if __name__ == "__main__":
    app.run(host="0.0.0.", port=5000)
