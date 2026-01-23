import sqlite3
from pathlib import Path

DB_PATH = Path("data/training_set.db")
DB_PATH.parent.mkdir(exist_ok=True)

conn = sqlite3.connect(DB_PATH)
cur = conn.cursor()

cur.execute("""
CREATE TABLE IF NOT EXISTS ruck_tests (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,

    run_1p5_sec INTEGER NOT NULL,
    lap_time_sec INTEGER,

    ruck_distance_mi REAL NOT NULL,
    ruck_time_sec INTEGER NOT NULL,
    ruck_weight_lb REAL,

    test_date TEXT,
    weather_label TEXT,
    is_fresh INTEGER
);
""")

conn.commit()
conn.close()

print("Database initialized at data/training_set.db")
