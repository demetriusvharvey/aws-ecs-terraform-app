import os
from flask import Flask, jsonify
import psycopg2

app = Flask(__name__)


def get_db_connection():
    return psycopg2.connect(
        host=os.environ["DB_HOST"],
        database=os.environ["DB_NAME"],
        user=os.environ["DB_USER"],
        password=os.environ["DB_PASSWORD"],
        port=os.environ.get("DB_PORT", 5432),
    )


def initialize_database():
    conn = get_db_connection()
    cur = conn.cursor()

    cur.execute(
        """
        CREATE TABLE IF NOT EXISTS visits (
            id SERIAL PRIMARY KEY,
            message TEXT NOT NULL
        );
        """
    )

    conn.commit()
    cur.close()
    conn.close()


@app.route("/")
def home():
    conn = get_db_connection()
    cur = conn.cursor()

    cur.execute("INSERT INTO visits (message) VALUES (%s)", ("Visit recorded from ECS app",))
    conn.commit()

    cur.execute("SELECT COUNT(*) FROM visits;")
    visit_count = cur.fetchone()[0]

    cur.close()
    conn.close()

    return f"App is live with RDS! Total visits recorded: {visit_count}"


@app.route("/health")
def health():
    try:
        conn = get_db_connection()
        cur = conn.cursor()
        cur.execute("SELECT 1;")
        cur.fetchone()
        cur.close()
        conn.close()
        return jsonify({"status": "healthy", "database": "connected"}), 200
    except Exception as e:
        return jsonify({"status": "unhealthy", "error": str(e)}), 500


if __name__ == "__main__":
    initialize_database()
    app.run(host="0.0.0.0", port=5000)