from flask import Flask, render_template

app = Flask(__name__)


@app.route("/")
def index():
    firstname = "Jon"
    stuff = "This is bold text"
    fav_pizza = ["Pepperoni", "Cheese", "Mushrooms", 33]
    return render_template(
        "index.html",
        firstname=firstname,
        stuff=stuff,
        fav_pizza=fav_pizza,
    )


# Custom error pages


# Invalid url
@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404


# Internal server error
@app.errorhandler(500)
def page_not_found(e):
    return render_template("500.html"), 500


if __name__ == "__main__":
    app.run(debug=True)
