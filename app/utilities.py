from datetime import date, datetime, timedelta

def close_diff(open, close):
    change = ((close-open)/open)*100
    change_percent = "{:.2f}".format(change)
    return change_percent

# determine what day to check for last close
# if T-S(1-5), chose yesterday
# if M(0), chose F
good_days = [1, 2, 3, 4, 5]

def determine_date(delta=1):
    today = datetime.now()
    if today.weekday() == 0:
        # is today Monday?
        # If so return Friday's closing price
        last_day = today - timedelta(days=3)
        formatted_last_day = last_day.strftime('%Y-%m-%d')
        return formatted_last_day
    else:
        # is today Tuesday - Saturday?
        # or was the market closed due to holidays
        # If so return yesterday's closing price by default
        # or return with a set delta
        yesterday = today - timedelta(days=delta)
        formatted_yesterday = yesterday.strftime('%Y-%m-%d')
        return formatted_yesterday

