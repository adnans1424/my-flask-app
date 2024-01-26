from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
	return "Hello World!"

@app.route("/callAdnan")
def call():
    return "Adnan is not answering..."