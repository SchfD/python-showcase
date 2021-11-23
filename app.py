from flask import Flask, request
from server_controller import server_api
import server_service as service

app = Flask(__name__)
app.register_blueprint(server_api)


@app.route("/", methods=["GET"])
def print_welcome_message():
    return "<h1>Homepage! Greenhouse System</h1>"


app.run()
