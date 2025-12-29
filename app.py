from flask import Flask, jsonify, render_template, request, redirect, url_for
import mysql.connector
import os
import time

app = Flask(__name__)

db_config = {
    "host": os.environ.get("DB_HOST"),   # IMPORTANT
    "user": "root",
    "password": "root",
    "database": "testdb"
}

def init_db():
    retries = 10
    for i in range(retries):
        try:
            conn = mysql.connector.connect(**db_config)
            cursor = conn.cursor()
            # Ensure table exists with basic structure
            cursor.execute("""
            CREATE TABLE IF NOT EXISTS users (
                id INT AUTO_INCREMENT PRIMARY KEY,
                name VARCHAR(255)
            )
            """)
            # Add columns if not exist
            columns_to_add = [
                ("phone_number", "VARCHAR(20)"),
                ("email", "VARCHAR(255)"),
                ("age", "INT"),
                ("sex", "VARCHAR(10)")
            ]
            for col, typ in columns_to_add:
                cursor.execute(f"SELECT COLUMN_NAME FROM INFORMATION_SCHEMA.COLUMNS WHERE TABLE_NAME = 'users' AND COLUMN_NAME = '{col}'")
                if not cursor.fetchone():
                    cursor.execute(f"ALTER TABLE users ADD COLUMN {col} {typ}")
            conn.commit()
            conn.close()
            print("Database initialized successfully")
            return
        except mysql.connector.Error as err:
            print(f"Database connection failed (attempt {i+1}/{retries}): {err}")
            time.sleep(5)
    raise Exception("Failed to connect to database after retries")

# Don't call init_db here, call it in a route or use app context

@app.before_request
def initialize_database():
    if not hasattr(app, 'db_initialized'):
        init_db()
        app.db_initialized = True

@app.route("/")
def home():
    return "Flask + MySQL via Docker Network "

@app.route("/form")
def form():
    return render_template('form.html')

@app.route('/save', methods=['POST'])
def save():
    name = request.form['name']
    number = request.form['number']
    email = request.form['email']
    age = request.form['age']
    sex = request.form['sex']
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO users (name, phone_number, email, age, sex) VALUES (%s, %s, %s, %s, %s)", (name, number, email, age, sex))
    conn.commit()
    conn.close()
    return redirect(url_for('form'))

@app.route("/users")
def users():
    conn = mysql.connector.connect(**db_config)
    cursor = conn.cursor()
    cursor.execute("SELECT id, name, phone_number, email, age, sex FROM users")
    data = cursor.fetchall()
    conn.close()
    return jsonify(data)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
