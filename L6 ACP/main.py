# Printing all the moonths
import calendar

# Loop through the month_name starting from index 1 to 12
for month in calendar.month_name:
    if month:  # Skip the empty string at index 0
        print(month)
