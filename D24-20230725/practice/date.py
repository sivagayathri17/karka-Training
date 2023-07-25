from datetime import date
current_date=date(2023,7,25)
print(current_date)
current_date1=date.today()
print(current_date1)
current_date2=date.today().year
print(current_date2)

from datetime import time
curr_time=time(12,16)
print(curr_time)
curr_time1=curr_time.minute
print(curr_time1)
      
from datetime import datetime
dt=datetime(2023,7,25,12,29,16)
print(dt)
dt1=datetime.now()
print(dt1)
dt2=dt1.strftime("%M")
dt3=dt1.strftime("%m")
print(dt2)
print(dt3)

from pytz import timezone
utc=datetime.now(timezone("UTC"))
year=utc.strftime("%y")
print(utc)
print(year)


