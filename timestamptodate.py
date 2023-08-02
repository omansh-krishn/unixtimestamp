import datetime

timestamp = int(input("Enter the timestamp: "))

dt_object = datetime.datetime.fromtimestamp(timestamp)

formatted_date = dt_object.strftime('%Y-%m-%d %H:%M:%S')

print(formatted_date)