from flask import Flask, render_template
from scrape_mars import scrape as myscrape

import pymongo
app = Flask(__name__)

conn = 
client = 
db = client.mars_db

#scrape route
@app.route('/')
def index():
    data = list(db.data.find())[0]
    data = list(db.data.find())
return render_template('index.html', data = data)

@app.route('/scrape')
def scrape():
    db.data.insert(data())
    return redirect("/")

if__name__=="__main__"
    app.run(__debug__)
