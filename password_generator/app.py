from flask import Flask, render_template, request
import random
import string

app = Flask(__name__)

password_history = []

def generate_password(length, numbers, symbols):

    characters = string.ascii_letters

    if numbers:
        characters += string.digits

    if symbols:
        characters += string.punctuation

    password = ''.join(random.choice(characters) for i in range(length))

    return password


@app.route("/", methods=["GET","POST"])
def home():

    password = ""

    if request.method == "POST":

        length = int(request.form["length"])
        numbers = "numbers" in request.form
        symbols = "symbols" in request.form

        password = generate_password(length,numbers,symbols)

        password_history.append(password)

    return render_template("index.html", password=password)


@app.route("/history")
def history():

    return render_template("history.html", history=password_history)


if __name__ == "__main__":
    app.run(debug=True)