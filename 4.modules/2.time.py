# epoch time : a date and time from which a computer measures system time

import time
epoch = time.ctime(0)
seconds_from_epoch = time.ctime(10000000000)
current_sec_since_epoch = time.time()
current_date = time.ctime(time.time())
current_time_obj = time.localtime()
current_utc_time = time.gmtime()
# current_formated_time = time.strftime("%B %d %Y %H:%M:%S",current_time_obj)
# string_to_time_obj = time.strptime("20 April, 2020", "%d %B %Y")
time_tuple = (2020, 4, 20, 4, 20, 0, 0, 0, 0)
# (year, month, day, hours, minutes, secs, #day of the week, #day off the year , dst)
asctime_string = time.asctime(time_tuple)
to_seconds = time.mktime(time_tuple)

print(to_seconds) # epoch in python
