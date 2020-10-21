from flask import Flask, render_template
import os
import socket

app = Flask(__name__)


@app.route("/")
def main():
    return render_template("index.html", text_color=os.getenv("TEXT_COLOR", "white"), name=os.getenv("NAME", "world"), hostname=socket.gethostname())


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
