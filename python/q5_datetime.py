# Hint:  use Google to find python function
from datetime import datetime as dt

#function to convert to datetime.date and calculate difference
def date_diff(date_start, date_stop, date_format):
    dt_start = dt.strptime(date_start, date_format)
    dt_stop = dt.strptime(date_stop, date_format)
    diff = dt_stop - dt_start
    return diff.days

####a)
date_format = '%m-%d-%Y'
date_start = '01-02-2013'
date_stop = '07-28-2015'
print 'a.', date_diff(date_start, date_stop, date_format)

####b)
date_format = '%m%d%Y'
date_start = '12312013'
date_stop = '05282015'
date_diff(date_start, date_stop, date_format)
print 'b.', date_diff(date_start, date_stop, date_format)

####c)
date_format = '%d-%b-%Y'
date_start = '15-Jan-1994'
date_stop = '14-Jul-2015'
date_diff(date_start, date_stop, date_format)
print 'c.', date_diff(date_start, date_stop, date_format)
