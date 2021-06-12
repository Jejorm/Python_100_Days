from logging import debug
from flask import Flask
from random import randint

app = Flask(__name__)

random_number = randint(0, 9)
print(f"{str(random_number).center(20,'-')}")


def verify_number(function):

	def wrapper(number):

		user_number = function(number)

		if user_number == random_number:
			return f"<h1 style='color: #3A7D44; font-size: 30px;'>You found me!</h1>" \
					"<img src='https://media.giphy.com/media/lnlAifQdenMxW/giphy.gif' width=300>"
		elif user_number < random_number:
			return f"<h1 style='color: #AB2346; font-size: 30px;'>Too low try again!</h1>" \
					"<img src='https://media.giphy.com/media/Tqv9jzL5diPGtFi0JV/giphy.gif' width=300>"
		else:
			return f"<h1 style='color: #AB2346; font-size: 30px;'>Too high try again!</h1>" \
					"<img src='https://media.giphy.com/media/XcXXEEQxcPVmyP3PyF/giphy.gif' width=300>"

	return wrapper


@app.route("/")
def start():
    return "<h1 style='color: #283618; font-size: 30px;'>Guess a number between 0 and 9</h1>" \
		   "<img src='https://media.giphy.com/media/pejC6N6W5GLEPtA27w/giphy.gif' width=300>"


@app.route("/<int:number>")
@verify_number
def game(number):
	return number


if __name__ == '__main__':
	app.run(debug=True)
