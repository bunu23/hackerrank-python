from datetime import datetime, timedelta, timezone
import sys

def parse_timestamp(timestamp):
    
    dt = datetime.strptime(timestamp[:-6], '%a %d %b %Y %H:%M:%S')
  
    tz_str = timestamp[-5:]
    tz_sign = 1 if tz_str[0] == '+' else -1
    tz_hours = int(tz_str[1:3])
    tz_minutes = int(tz_str[3:5])
    tz_offset = timezone(timedelta(hours=tz_sign * tz_hours, minutes=tz_sign * tz_minutes))
    return dt.replace(tzinfo=tz_offset)

input_data = sys.stdin.read().strip().split("\n")


num_cases = int(input_data[0])
index = 1


for _ in range(num_cases):
   
    timestamp1 = input_data[index]
    timestamp2 = input_data[index + 1]
    index += 2


    dt1 = parse_timestamp(timestamp1)
    dt2 = parse_timestamp(timestamp2)

   
    difference = abs((dt2 - dt1).total_seconds())


    print(int(difference))
