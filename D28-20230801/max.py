a=[1,2,7,3,10]
b=[3,4,6,1,20]
large=[]
for i in range(len(a)):
    if a[i]>b[i]:
        large+=[a[i]]
    else:
        large+=[b[i]]    
print(large)    

# a=[1,2,7,3,10,9,2]
# b=[3,4,6,1,20]
# large=[]
# for i in range(len(b)):
#     if a[i]>b[i]:
#         large+=[a[i]]
#     else:
#         large+=[b[i]]  
#         a=a[5:7]  
#         large+=[a]
# print(large)    