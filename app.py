from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def home():
    # should change to home after done structuring
    return render_template("base.html", title="Mental Health")


if __name__ == "__main__":
    app.run()
