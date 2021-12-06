from flask import Flask
from server_controller import server_api

app = Flask(__name__)
app.register_blueprint(server_api)


@app.route("/")
def print_welcome_message():
    return "<h1>Homepage! Greenhouse System</h1>"


if __name__ == "__main__":
    print("Hello")

app.run(port=5000, debug=False)
