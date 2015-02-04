from datetime import datetime, timedelta
import math

def days_between_dates(date1, date2):
    time_delta = due_date - start_date
    total_seconds = time_delta.total_seconds()

    SECONDS_IN_A_DAY = 86400
    float_days = total_seconds / float(SECONDS_IN_A_DAY)
    return float_days

def int_ceil(num):
    return int(math.ceil(num))


print("\n-- Unit Scheduler for Small Projects --\n")

units = raw_input("Enter number of work units: ")
start_date_str = raw_input("(Optional) Enter start date (yyyy-mm-dd): ")
due_date_str = raw_input("Enter due date (yyyy-mm-dd): ")


due_date = datetime.strptime(due_date_str, "%Y-%m-%d")

if (start_date_str):
    start_date = datetime.strptime(start_date_str, "%Y-%m-%d")
else:
    start_date = datetime.now()

day_count = int_ceil(days_between_dates(due_date, start_date))

start_date_format_str = start_date.strftime("%B %d, %Y")
due_date_format_str = due_date.strftime("%B %d, %Y")
print("\nProject from %s to %s (%d days)" % (start_date_format_str, due_date_format_str, day_count))

units_per_day = float(units) / day_count

print("\n%.1f units per day\n" % (units_per_day))

# By default, includes start date but not due date
for day in range(0, day_count):

    current_date = start_date + timedelta(days=day)
    current_date_str = current_date.strftime("%Y-%m-%d")

    units_low = round(units_per_day * day)
    units_high = round(units_per_day * (day+1))

    print("%s Units %d - %d" % (current_date_str, units_low, units_high))

raw_input()
