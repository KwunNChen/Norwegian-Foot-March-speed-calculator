import sqlite3
from pathlib import Path
from statistics import mean

DB_PATH = Path("data/training_set.db")

def fetch_fresh_rows():
    conn = sqlite3.connect(DB_PATH)
    #wtf does cursor do again?
    cur = conn.cursor()
    cur.execute("""SELECT run_1p5_sec, lap_time_sec, ruck_distance_mi, ruck_time_sec, weather_label 
                FROM ruck_tests 
                WHERE is_fresh = 1""")

    rows = cur.fetchall()
    conn.close()
    return rows

def compute_slopes(rows):
    slopes = []
    for run_sec, dist, ruck_sec in rows:
        pace = ruck_sec / dist  # sec/mi
        fitness = run_sec / (1.5 * 60)
        slopes.append(pace * fitness)
    return slopes

def average_slope():
    rows = fetch_fresh_rows()
    if not rows:
        raise ValueError("No fresh ruck data available")
    return mean(compute_slopes(rows))

def estimate_total_time(distance_mi, run_sec):
    k = average_slope()
    fitness = run_sec / (1.5 * 60)
    return distance_mi * k * fitness

def quarter_splits(total_time_sec):
    """
    Split total ruck time into 4 quarters with pacing multipliers.
    Returns list of 4 quarter times (seconds).
    """
    multipliers = [1.02, 1.00, 1.01, 0.97]
    avg_quarter = total_time_sec / 4
    quarters = []

    for m in multipliers:
        q_time = avg_quarter * m
        quarters.append(q_time)
    return quarters
