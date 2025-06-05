from flask import Flask, jsonify, render_template, request, redirect, url_for
import json
from pymongo import MongoClient

app = Flask(__name__)

# MongoDB Atlas setup
client = MongoClient("mongodb+srv://<USERNAME>:<PASSWORD>@cluster0.ghfnzgu.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
db = client["flask_db"]
collection = db["submissions"]

@app.route('/api')
def api():
    with open("data.json") as f:
        data = json.load(f)
    return jsonify(data)

@app.route('/')
def form():
    return render_template('form.html')

@app.route('/submit', methods=['POST'])
def submit():
    try:
        name = request.form['name']
        email = request.form['email']
        collection.insert_one({'name': name, 'email': email})
        return redirect(url_for('success'))
    except Exception as e:
        return render_template('form.html', error=str(e))

@app.route('/success')
def success():
    return render_template('success.html')

if __name__ == '__main__':
    app.run(debug=True)
