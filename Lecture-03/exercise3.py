hours_work = int(input("Enter the number of hours_worked"))
hourly_rate = float(input("Enter the hourly rate:"))
if hours_work <= 40 :
    tatal_pay = hours_work * hourly_rate
else:
    overtime_hour