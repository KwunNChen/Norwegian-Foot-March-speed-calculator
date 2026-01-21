import sqlite3
from pathlib import Path

DB_PATH = Path("data/training_set.db")
DB_PATH.parent.mkdir(exist_ok=True)

conn = sqlite3.connect(DB_PATH)
cur = conn.cursor()
#This doesn't execute at all if 
cur.execute("""
CREATE TABLE IF NOT EXISTS ruck_tests (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT,
    run_1p5_sec INTEGER,
    ruck_distance_mi REAL,
    ruck_time_sec INTEGER,
    ruck_weight_lb REAL,
    terrain TEXT,
    test_date TEXT,
    is_fresh INTEGER
);
""")

conn.commit()
conn.close()

print("Database initialized at data/training_set.db")
