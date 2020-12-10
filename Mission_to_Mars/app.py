from flask import Flask, render_template, jsonify, redirect
from scrape_mars import myScrape
import pymongo

app = Flask(__name__)

conn = "mongodb://localhost:27017"
client = pymongo.MongoClient(conn) 
db = client.mars_db

@app.route('/')
def index():
    data = list(db.mars.find())
    print(teams)
    return render_template("index.html", data=data)

@app.route('/scrape')
def scrape():
    db.mars.insert_many([myScrape()])
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)