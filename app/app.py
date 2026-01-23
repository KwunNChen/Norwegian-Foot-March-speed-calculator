import calculations


#Placeholder inputs
loop = True
while loop == True:
    mile_time_min = input("Enter your 1.5 mile run time (minutes:seconds): ")
    loop = False
    try:
        min_part, sec_part = mile_time_min.split(":")
        run_time_sec = int(min_part) * 60 + int(sec_part)
    except:
        print("Invalid format. Please enter time as minutes:seconds (e.g., 12:30).")
        loop = True
#ruck distance (miles)

#When user clicks a button:
#convert run time to seconds
#call estimate_total_time(...)
#call quarter_splits(...)
#print Q1–Q4 to screen