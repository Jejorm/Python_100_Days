from flask import Flask

def make_bold(function):
    def wrapper():
        return f"<b style='font-size:50px;'>{function()}</b>"
    return wrapper

def make_emphasis(function):
    def wrapper():
        return f"<em>{function()}</em>"
    return wrapper

def make_underline(function):
    def wrapper():
        return f"<u>{function()}</u>"
    return wrapper

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "<h1 style='text-align: center'>Hello, World</h1>" \
           "<p>This is a paragraph.</p>" \
           "<img src='https://media.giphy.com/media/l0MYEw3Rjka9yuWTS/giphy.gif' width=200>"


@app.route("/bye")
@make_underline
@make_emphasis
@make_bold
def bye():
    return "Bye!"


@app.route("/username/<name>/<int:number>")
def greet(name, number):
    return f"Hello there {name}, your are {number} years old!"


if __name__ == '__main__':
    # Run the app in debug mode to auto-reload.
    app.run(debug=True)