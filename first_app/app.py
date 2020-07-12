from flask import Flask

app = Flask(__name__)


@app.route("/")  # http://localhost/
def home():
    return "Hello, World!"


app.run()

# To startup app on other port:
# app.run(port=4444)
