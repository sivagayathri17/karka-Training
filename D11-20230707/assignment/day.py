day=int(input("enter the date : "))
def week(day):
  if day==1:
     return("today is sunday")
  elif day==2:
     return("today is monday")
  elif day==3:
     return("today is tuesday") 
  elif day==4:
     return("today is wednesday")
  elif day==5:
     return("today is thursday") 
  elif day==6:
     return("today is friday")
  elif day==7 and day==0:
     return("today is saturday")   
  else:
     return("error")  
print(f"today is a {week(day)}")
