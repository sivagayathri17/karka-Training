# lists=[1,2,3,4,5,2,5,6,1,3]
# # new=list(set(lists))
# # print(new)
# original=[]
# for list in lists:
#     if list not in original:
#      original.append(list)

# # original.insert(6,"-")
# original.append("-")
# print(original)    

# # remove
# name=["shiva","ram","gayu","sree"]
# name.remove("shiva")
# print(name)
# # append
# name1=["shiva","ram","gayu","sree"]
# name1.append("abi")
# print(name1)
# # pop
# name2=["shiva","ram","gayu","sree"]
# name2.pop()
# print(name2)
# # len
# name3=["shiva","ram","gayu","sree"]
# len=len(name3)
# print(len)
# # count
# name4=["shiva","ram","gayu","sree"]
# count=name4.count("ram")
# print(count)
# # reverse
# name5=["shiva","ram","gayu","sree"]
# name5.reverse()
# print(name5)
 

list=[3,2,2,3]
add_list=[]
r_val=int(input("remove value:"))

for num in list:
    if num!=r_val:
     add_list+=[num]
add_list+=["*"]
print(add_list)
    