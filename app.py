from flask import Flask

app = Flask(__name__)

@app.route('/',methods = ["GET","POST"])
def index():
    return "Hello My Name is Abhishek Nagpal.This is my first deployed app."

if __name__ == '__main__':
    app.run(debug=True)
