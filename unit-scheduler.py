from datetime import datetime

units = raw_input("Enter the number of work units in the project:")
start_date_str = raw_input("(Optional) Enter the start date for the project (yyyy/mm/dd):")
due_date_str = raw_input("Enter the due date for the project (yyyy/mm/dd):")

if (start_date_str):
    start_date = datetime.strptime(start_date_str, "%Y/%m/%d")
else:
    start_date = datetime.now()

due_date = datetime.strptime(due_date_str, "%Y/%m/%d")

print(start_date.strftime("%B %d, %Y") + " to " + due_date.strftime("%B %d, %Y"))

raw_input()