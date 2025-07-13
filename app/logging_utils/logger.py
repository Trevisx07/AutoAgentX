import sqlite3
import os
import time
from datetime import datetime

LOG_DB = os.path.join(os.path.dirname(__file__), "logs.db")

def init_db():
    with sqlite3.connect(LOG_DB) as conn:
        c = conn.cursor()
        c.execute("""
        CREATE TABLE IF NOT EXISTS logs (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            task_type TEXT,
            user_input TEXT,
            ai_response TEXT,
            timestamp TEXT,
            exec_time REAL
        )
        """)
        conn.commit()

init_db()

def log_task(task_type: str, user_input: str, ai_response: str, exec_time: float):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    with sqlite3.connect(LOG_DB) as conn:
        c = conn.cursor()
        c.execute("""
        INSERT INTO logs (task_type, user_input, ai_response, timestamp, exec_time)
        VALUES (?, ?, ?, ?, ?)
        """, (task_type, user_input[:500], ai_response[:1000], timestamp, exec_time))
        conn.commit()
