from datetime import datetime
from dateutil import parser


def should_run_cron_job(cron_expression):
    cron_parts = cron_expression.split(" ")
    if len(cron_parts) != 5:
        raise ValueError("Invalid cron expression")

    minute, hour, day_of_month, month, day_of_week = cron_parts

    now = datetime.now()
    current_minute = now.minute
    current_hour = now.hour
    current_day_of_month = now.day
    current_month = now.month
    current_day_of_week = now.weekday() + 1

    # print(now.weekday())
    # print(now.strftime("%A"))

    if (minute == "*" or int(minute) == current_minute) and \
            (hour == "*" or int(hour) == current_hour) and \
            (day_of_month == "*" or int(day_of_month) == current_day_of_month) and \
            (month == "*" or int(month) == current_month) and \
            (day_of_week == "*" or int(day_of_week) == current_day_of_week):

        return True
    else:
        return False


print(should_run_cron_job("* * * * *"))
