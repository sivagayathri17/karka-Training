# from datetime import datetime,timedelta
# date_str="30 may 2023"
# strp_time=datetime.strptime(date_str,"%d %b %Y")
# print(type(strp_time))
# end_date=strp_time + timedelta(days=5)
# print(end_date)



lists=[1,2,3,4,5,2,5,6,1,3]
# new=list(set(lists))
# print(new)
original=[]
for list in lists:
    if list not in original:
     original.append(list)
original.insert(6,"-")
print(original)
        