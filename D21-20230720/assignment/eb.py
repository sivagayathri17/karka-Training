calculate_electricity_bills={"name":"shiva",
                            "reading":[1420,1530,1650,1789,1864]}
reads=calculate_electricity_bills["reading"]
def bill():
 list=[]
 tot=0
 for read in range(len(reads)-1):
    #  print(read)
     dic={}
     month=read+1
     unit1=reads[read]
     unit2=reads[read+1]
     diff=unit2-unit1

     if diff<100:
          rs=0
     elif 100<diff<200:
          rs=diff*2
     elif 200<diff<500:         
          rs=diff*5
     elif 500<diff<1000:
          rs=diff*10
     elif 1000<diff:
          rs=diff*14
     tot=tot+rs     
     dic["month"]=month
     dic["units_consumed"]=diff
     dic["bill_amount"]=rs
     print(dic)
     list.append(dic)
 return list  
str_bills=str(bill())
str_eb_bills=str_bills
print(str_eb_bills)
# print(bill())  
# eb_bills=bill()
# print(eb_bills)

# with open("/home/siva/karka.txt","w") as file:
#   for eb_bill in eb_bills:
#    str_eb=f"month:{eb_bill['month']}\n units_consumed: {eb_bill['units_consumed']} \nbill_amount:{eb_bill['bill_amount']}\n"
#    file.write(str_eb)
with open("/home/siva/karka.txt","w") as file:  
   file.write(str_eb_bills)