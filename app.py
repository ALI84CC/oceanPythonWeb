from flask import Flask

app = Flask("Hello")

@app.route('/')
def Hello():
    return"<h1>Hello World</h1>"