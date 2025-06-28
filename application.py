from flask import Flask

application = Flask(__name__)
app = application

@app.route('/')
def index():
    return "Health OK", 200

if __name__ == "__main__":
    app.run(host="0.0.0.0")
