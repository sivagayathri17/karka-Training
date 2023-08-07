num=[1,2,5,3,4]
val=int(input("enter the number : "))
for i in range(len(num)-1):
    a=num[i]
    for j in range(i+1,len(num)):
        b=num[j]
        c=a+b
        if c== val:
        #  print([num[i],num[j]])  
         print(a,b)      