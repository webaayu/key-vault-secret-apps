from flask import Flask, render_template, request, redirect
import psycopg2
import os

app = Flask(__name__)

# Fetch PostgreSQL credentials from environment variables
db_user = os.getenv('POSTGRES_USER')
db_password = os.getenv('POSTGRES_PASSWORD')
db_name = os.getenv('POSTGRES_DB')
#db_host = os.getenv('POSTGRES_HOST', 'postgres-service')
#db_port = os.getenv('POSTGRES_PORT', '5432')  # Set the default port to 5432

# PostgreSQL connection
def get_db_connection():
    try:
        conn = psycopg2.connect(
            host='postgres',
            database=db_name,
            user=db_user,
            password=db_password,
           # port='5432'
        )
        return conn
    except Exception as e:
        print(f"Error connecting to the database: {e}")
        return None

@app.route('/')
def home():
    conn = get_db_connection()
    if conn is None:
        return "Could not connect to the database", 500

    cursor = conn.cursor()
    cursor.execute('SELECT * FROM ratings')
    ratings = cursor.fetchall()
    cursor.close()
    conn.close()
    return render_template('index.html', ratings=ratings)

@app.route('/add', methods=['POST'])
def add_rating():
    name = request.form['name']
    rating = request.form['rating']
    conn = get_db_connection()
    if conn is None:
        return "Could not connect to the database", 500
    
    cursor = conn.cursor()
    cursor.execute('INSERT INTO ratings (name, rating) VALUES (%s, %s)', (name, rating))
    conn.commit()
    cursor.close()
    conn.close()
    return redirect('/')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
