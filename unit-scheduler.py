from datetime import datetime

print("\n-- Unit Scheduler for Small Projects --\n")

units = raw_input("Enter the number of work units: ")
start_date_str = raw_input("(Optional) Enter the start date (yyyy/mm/dd): ")
due_date_str = raw_input("Enter the due date (yyyy/mm/dd): ")

if (start_date_str):
    start_date = datetime.strptime(start_date_str, "%Y/%m/%d")
else:
    start_date = datetime.now()

due_date = datetime.strptime(due_date_str, "%Y/%m/%d")

# Testing
print(start_date.strftime("%B %d, %Y") + " to " + due_date.strftime("%B %d, %Y"))

days_between_dates = (due_date - start_date).days

# Testing
print(str(days_between_dates) + " days from start date to due date")

raw_input()