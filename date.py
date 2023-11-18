from datetime import datetime, timedelta

# Creating datetime objects
start_date = datetime(2023, 11, 1, 10, 0, 0)  # Year, month, day, hour, minute, second
end_date = datetime(2023, 11, 10, 15, 30, 0)

# Calculating the difference
time_difference = end_date - start_date

# Printing the difference in days and seconds
print(f"Difference in days: {time_difference.days}")
print(f"Difference in seconds: {time_difference.total_seconds()}")
