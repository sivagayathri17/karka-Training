from datetime import datetime,timedelta
date_str="30 may 2023"
strp_time=datetime.strptime(date_str,"%d %b %Y")
print(type(strp_time))
end_date=strp_time +timedelta(days=5)
print(end_date)
