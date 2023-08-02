import datetime

def datetime_to_unix(year, month, day, time_in_seconds):

    dt_object = datetime.datetime(year, month, day, 0, 0, 0) + datetime.timedelta(seconds=time_in_seconds)

    # Calculate the timestamp
    unix_timestamp = int(dt_object.timestamp())
    return unix_timestamp

if __name__ == "__main__":
    try:
        # Input values
        year = int(input("Enter year (e.g., 2023): "))
        month = int(input("Enter month (1-12): "))
        day = int(input("Enter day (1-31): "))
        time_str = input("Enter time in seconds (in 24-hour format, e.g., 12:33:45): ")
        
        # Extract hours, minutes, and seconds from the given input
        hours, minutes, seconds = map(int, time_str.split(':'))
        
        # Convert it to seconds
        time_in_seconds = (hours * 3600) + (minutes * 60) + seconds
        
        # Convert to Unix timestamp
        unix_timestamp = datetime_to_unix(year, month, day, time_in_seconds)
        print("Unix timestamp:", unix_timestamp)
    
    except ValueError:
        print("Invalid input. Please follow the proper input format.")
