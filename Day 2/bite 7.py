# In this bite we will look at this small server log finding the first and last system shutdown events:

# INFO 2014-07-03T23:27:51 supybot Shutdown initiated.
# ...
# INFO 2014-07-03T23:31:22 supybot Shutdown initiated.
# You need to calculate the time between these two events. First extract the timestamps from the log entries and convert them to datetime objects. Then use datetime.timedelta to calculate the time difference between them.

# You can assume the logs are sorted in ascending order. Check out the docstrings and the TESTS for more info.

# Good luck and keep calm and code in Python!






from datetime import datetime
import re
import os
import urllib.request

SHUTDOWN_EVENT = 'Shutdown initiated'

# prep: read in the logfile
tmp = os.getenv("TMP", "/tmp")
logfile = os.path.join(tmp, 'log')
urllib.request.urlretrieve(
    'https://bites-data.s3.us-east-2.amazonaws.com/messages.log',
    logfile
)

with open(logfile) as f:
    loglines = f.readlines()


# for you to code:

def convert_to_datetime(line):
    """TODO 1:
       Extract timestamp from logline and convert it to a datetime object.
       For example calling the function with:
       INFO 2014-07-03T23:27:51 supybot Shutdown complete.
       returns:
       datetime(2014, 7, 3, 23, 27, 51)
       
       %Y-%m-%dT%H::%M::%S.%f  ----- year,month,day,hour,min,sec,microsec
    """
    str_timestamp = re.findall(r'\d{4}-\d{2}-\d{2}T\d{2}:\d{2}:\d{2}',line)
    dt = datetime.strptime(str_timestamp[0], '%Y-%m-%dT%H:%M:%S')
    return dt


def time_between_shutdowns(loglines):
    """TODO 2:
       Extract shutdown events ("Shutdown initiated") from loglines and
       calculate the timedelta between the first and last one.
       Return this datetime.timedelta object.
    """
    my_list = []
    converted_into_time_list = []
    for line in loglines:
        if SHUTDOWN_EVENT in line:
            my_list.append(line)
    for line in my_list:
        converted_into_time_list.append(convert_to_datetime(line))
    
    time_diff = max(converted_into_time_list) - min(converted_into_time_list)
    return time_diff
