from flask import Flask
import sqlite3

app = Flask(__name__)

@app.route("/")
def request():
    conn = sqlite3.connect('Productinfo.db')
    cur = conn.cursor()
    cur.execute("SELECT * FROM PRODUCTINFO where ID = 2 ;")
    result = cur.fetchall()
    return f'<p> {result[0][1]} {int(result[0][0])} <p!>'
