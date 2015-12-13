from flask import Flask, render_template, request


app=Flask(__name__)

@app.route('/')
def home():
    return 'hello'

if __name__ == "__main__":
    app.debug = True
    #app.secret_key = "69cce1c1daa03989"
    app.run(host = '0.0.0.0', port = 8000)
