import sys
from pathlib import Path

# Add parent directory to path if calculations module is there
sys.path.insert(0, str(Path(__file__).parent))
# from calculations import estimate_total_time, quarter_splits  # Uncomment once calculations.py exists
import streamlit as st

# --- Streamlit UI ---
st.title("Norwegian Foot March Speed Calculator")

# User input for 1.5 mile run time
mile_time_min = st.text_input(
    "Enter your 1.5 mile run time (minutes:seconds)", value="12:30"
)

def parse_time(time_str):
    try:
        min_part, sec_part = time_str.strip().split(":")
        return int(min_part) * 60 + int(sec_part)
    except Exception:
        return None

run_time_sec = parse_time(mile_time_min)
if run_time_sec is None:
    st.error("Invalid format. Please enter time as minutes:seconds (e.g., 12:30).")

# User input for ruck distance
distance_mi = st.number_input("Ruck distance (miles)", min_value=1.0, max_value=26.2, value=18.6, step=0.1)

# Weather label (optional, for future use)
weather = st.selectbox("Weather conditions", ["Normal", "Hot", "Cold"], index=0)

# Placeholder for calculations
def estimate_total_time(distance_mi, run_sec, weather_label="Normal"):
    # Placeholder logic: 18:00/mi pace baseline
    pace_sec_per_mi = 1080
    return distance_mi * pace_sec_per_mi

def quarter_splits(total_time_sec):
    q = total_time_sec / 4
    return [q, q, q, q]

NO_DATA_MSG = (
    "**No fresh ruck data yet**\n\n"
    "I can still show quarter splits using a temporary baseline, but once Spec Ops PT data is collected this will auto-calibrate and become personalized."
)

if st.button("Calculate Splits"):
    if run_time_sec is None:
        st.warning("Please enter a valid run time in minutes:seconds format.")
    else:
        try:
            # Uncomment below when real logic is available
            # total_time_sec = estimate_total_time(distance_mi, run_time_sec, weather_label=weather)
            # quarters = quarter_splits(total_time_sec)
            total_time_sec = estimate_total_time(distance_mi, run_time_sec, weather_label=weather)
            quarters = quarter_splits(total_time_sec)
            st.success(f"Estimated total time: {int(total_time_sec//60)}:{int(total_time_sec%60):02d}")
            for i, q in enumerate(quarters, 1):
                st.write(f"Quarter {i}: {int(q//60)}:{int(q%60):02d}")
        except ValueError as e:
            st.warning(NO_DATA_MSG)