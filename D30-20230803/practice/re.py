val=int(input("enter the value:"))
for i in range(val,0,-1):
    #   print(i)
      for j in range(i,0,-1):
       print(j,end=" ")
      print("")
    
val1=int(input("enter the value : "))
for i in range (0,val1):
    for j in range(i+1):
        print("*", end=" ")
    print("")
for i in range (1,val1):
    for j in range(val1-i):
        print("*", end=" ")
    print("")    

val2=int(input("enter the number :"))
for data in range (1,val2*2):
    if data<=val:
        data1=data
    else:
        data1=(val2*2)-data 
    for data in range(data1):
        print("~*",end=" ")
    print(" ")    
        


