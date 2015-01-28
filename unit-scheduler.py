from datetime import datetime, timedelta

print("\n-- Unit Scheduler for Small Projects --\n")

units = raw_input("Enter number of work units: ")
start_date_str = raw_input("(Optional) Enter start date (yyyy-mm-dd): ")
due_date_str = raw_input("Enter due date (yyyy-mm-dd): ")

if (start_date_str):
    start_date = datetime.strptime(start_date_str, "%Y-%m-%d")
else:
    start_date = datetime.now()

due_date = datetime.strptime(due_date_str, "%Y-%m-%d")

# Testing
print(start_date.strftime("%B %d, %Y") + " to " + due_date.strftime("%B %d, %Y"))

days_between_dates = (due_date - start_date).days

# Testing
print(str(days_between_dates) + " days from start date to due date")

units_per_day = float(units) / days_between_dates

# Testing
print("%.1f units per day" % (units_per_day))

for day in range(1, days_between_dates+1):
    current_date = start_date + timedelta(days=day)
    current_date_str = current_date.strftime("%Y-%m-%d")

    units_low = units_per_day * (day-1)
    units_high = units_per_day * day

    print("%s Units %.1f - %.1f" % (current_date_str, units_low, units_high))

raw_input()
