from flask import Flask, render_template, request
import data_fetch
import json

app=Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/update')
def update():
    print 'boutta fetch'
    infos=data_fetch.get_new_albums()
    print 'jus fetchd'
    return json.dumps(infos)

if __name__ == "__main__":
    app.debug = True
    app.secret_key = "69cce1c1daa03989"
    app.run(host = '0.0.0.0', port = 8000)
