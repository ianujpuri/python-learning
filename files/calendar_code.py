
import calendar

def print_calendar_months():
    # cal = calendar.Calendar(calendar.SUNDAY)
    for c in calendar.month_name:
        print(c)

def print_calendar_days():
    for c in calendar.day_name:
        print(c)

    c = calendar.TextCalendar(calendar.SUNDAY)
    print(c.formatmonth(2024, 6, 0, 0))


print_calendar_months()
print_calendar_days()