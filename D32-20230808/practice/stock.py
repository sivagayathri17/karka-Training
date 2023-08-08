# n=int(input("enter the number :" ))
# emty=[]
# max=0
# min=0
# for  i in range(1,n+1):
#    stock=int(input("enter the stock :" ))
#    emty.append(stock)
#    print(emty)

# for j in range(len(emty)):
#     if emty[j]>max:
#         max=emty[j]
#         a=j
       

      
#     if emty[j]<max:
#         min=emty[j]
#         b=j     
# print(f"max_stock :{max}")     
# print(f"min_stock : {min}")
# # print(a,b)
# print(max-min)

n=int(input("enter the number :" ))
emty=[]
pro=0
for  i in range(1,n+1):
   stock=int(input("enter the stock :" ))
   emty.append(stock)
   print(emty)
for i in range(len(emty)):
    for j in range(i+1,len(emty)):

     a= emty[j]-emty[i]
     if a>pro:
        pro=a
        buy_day=i
        sale_day=j
print(pro)
print(buy_day,sale_day)
     
    
        
      




