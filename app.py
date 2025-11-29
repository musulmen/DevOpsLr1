from flask import Flask
import psycopg2
import os

app = Flask(__name__)

def get_db_connection():
    conn = psycopg2.connect(
        host=os.getenv('POSTGRES_HOST', 'localhost'),
        port=os.getenv('POSTGRES_PORT', 5432),
        database=os.getenv('POSTGRES_DB', 'postgres'),
        user=os.getenv('POSTGRES_USER', 'postgres'),
        password=os.getenv('POSTGRES_PASSWORD', '883762')
    )
    return conn

@app.route('/')
def hello():
    try:
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute('SELECT 1')
        cur.close()
        conn.close()
        return "Hello docker and postgres!"
    except Exception:
        return "Sorry, but db is not connected:("

if __name__ == '__main__':
    app_port = int(os.getenv('APP_PORT', 1234))
    app.run(host='0.0.0.0', port=app_port)
