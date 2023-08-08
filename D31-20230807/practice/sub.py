# num_list=[2,5,8,1,9,3,7]
# val=int(input("enter the value : "))
# for i in range(len(num_list)):
#     a=num_list[i]
#     for j in range(i+1,len(num_list)):
#         b=num_list[j]
#         c=a-b
#         if c==val:
#         #   print(f"{val}({num_list[i]}-{num_list[j]})")
#           print(f"{val}({a}-{b})")
# else:
#     print("not pair")  
       
num_list=[2,5,8,1,9,3,7]
max=0
for i in range(len(num_list)):
    a=num_list[i]
    for j in range(i+1,len(num_list)): 
        b= num_list[j]   
        if a>b: 
            max=a
            diff=a-b   
            # max=diff         
print(max)




