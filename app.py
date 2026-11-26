from flask import Flask
import psycopg2
import os
import time

app = Flask(__name__)

@app.route('/health')
def health():
    return 'OK'

@app.route('/api/items/count')
def count():
    time.sleep(1)
    conn = psycopg2.connect(
        host=os.environ.get('DB_HOST', 'db'),
        database=os.environ.get('DB_NAME', 'myapp'),
        user=os.environ.get('DB_USER', 'postgres'),
        password=os.environ.get('DB_PASSWORD', 'supersecret')
    )
    cur = conn.cursor()
    cur.execute('SELECT COUNT(*) FROM items;')
    res = cur.fetchone()[0]
    conn.close()
    return str(res)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)