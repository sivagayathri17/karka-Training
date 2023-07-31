days = ["monday", "tuesday", "wednesday", "thursday", "friday", "saturday", "sunday"]
tot_days = 30
list=[]
for i in range(len(days)):
    x=[]
    for j in range(i+1,tot_days+1,len(days)):
     # print(j)
     x.append(j)

    week={"day":days[i] , "total days in month:":x}
    list.append(week)
print(list)    



      
