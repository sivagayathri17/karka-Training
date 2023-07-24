val1=int(input("enter the number :"))
# print(val1)
val2=int(input("enter the number :"))
# print(val2)
val3=int(input("enter the number :"))
# print(val3)
# num=0
# if val1>num:
#     num=val1
#     # print(num)

# if val2>num: 
#     num=val2
#     #   print(num)
      

# if val3>num:
#     num=val3
#     #    print(num) 
# print(f"{num} is big")        
if val1>val2:
    if val1>val3:
        print(f"{val1} is big")
    else:
        print(f"{val2} is big")
elif  val2>val3:
    if val2>val1:
        print(f"{val2} is big")
    else:
        print(f"{val3} is big")   
elif  val3>val2:
    if val3>val1:
        print(f"{val3}is big")
    else:
        print(f"{val1} is big")    
            
