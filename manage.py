from flask import Flask

app = Flask(__name__)


@app.route("/")
def index1():

    return "......22222"


if __name__ == '__main__':
    app.run(debug=True)




