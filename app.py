from flask import Flask, render_template, request
import data_fetch
import json
import cgi

app=Flask(__name__)

@app.route('/')
def home():
    return render_template('indexboot.html')

@app.route('/search', methods=['GET'])
def search():
    #print request.form
    #name=request.args.get('toSearch')
    #print name
    #form = cgi.FieldStorage()
    #searcher = form["search"]
    #print searcher
    #lyricinfos=data_fetch.get_lyrics('we are the champions')
    print 'qqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqqq'
    print request.args.get("searchKey")
    lyricinfos=data_fetch.get_lyrics(searcher)
    return json.dumps(lyricinfos)

@app.route('/update')
def update():
    print 'boutta fetch'
    albuminfos=data_fetch.get_new_albums()
    
    print 'jus fetchd'
    return json.dumps(albuminfos)

if __name__ == "__main__":
    app.debug = True
    app.secret_key = "69cce1c1daa03989"
    app.run(host = '0.0.0.0', port = 8000)
