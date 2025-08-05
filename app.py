from flask import Flask
import sqlite3

app = Flask(__name__)

@app.route('/')
def home():
    return 'Welcome to the Cat App'

@app.route('/cats')
def get_cats():
    conn = sqlite3.connect('pet_database.db')
    cursor = conn.cursor()
    cursor.execute('SELECT name FROM cats WHERE owner_id = 1')
    cats = cursor.fetchall()
    conn.close()
    return {'cats': [cat[0] for cat in cats]}

if __name__ == '__main__':
    app.run(debug=True)