from flask import Flask
import sqlite3

app = Flask(__name__)

@app.route('/')
def request():
    conn = sqlite3.connect('Productinfo.db')
    cur = conn.cursor()
    cur.execute("SELECT * FROM PRODUCTINFO;")
    results = cur.fetchall()
    return results
