# reverse without method

name=["shiva","abi","gayathri"]
em=[]
n=-1
while n>=-len(name):
    print(name[n])
    em+=[name[n]]
    n=n+-1
print(em)

num_val=[10,5,3,6]
num=-1
while num>=-len(num_val):
    print(num_val[num]) 
    num=num+-1
     
name1=["shiva","abi","ram","gayathri"]
na=name1.sort()
print(name1)

# sort the list without method
num=[1,10,7,4,3,8]
for i in range(len(num)):
    for j in range(i+1,len(num)):
        if num[i]>num[j]:
            temp=num[i]
            num[i]=num[j]
            num[j]=temp
print(num)  

# sort the list without mehtod
name=["shiva","abi","ram","gayathri"] 
for i in range(len(name)):
    for j in range(i+1,len(name)):
        if name[i]>name[j]:
            temp=name[i]
            name[i]=name[j]
            name[j]=temp
print(name)            


list1=[2,3,3,4,2,3]
r_val=int(input("remove value:"))

for num in list1:
    if num ==r_val:
        list1 += ["*"]
        list1 = list1[:list1.index(num)] + list1[list1.index(num)+1:]
print(list1)

