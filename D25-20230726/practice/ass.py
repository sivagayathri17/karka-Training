# lists=[1,2,3,4,5,2,5,6,1,3]
# # new=list(set(lists))
# # print(new)
# original=[]
# for list in lists:
#     if list not in original:
#      original.append(list)
# print(original)

# saree=int(input("Enter the price of saree :"))
# kurthi=int(input("Enter the price of kurthi :"))
# top=int(input("Enter the price of tops :"))
# gown=int(input("Enter the price of gown :"))
# total=(saree+kurthi+top+gown)
# print(total)
# if total>=500 and total<=1000:
#     print("you have owned a gold token")
# else:
#     print("You have owned a dimond token")


# name_list=["shiva","gayathri","ram","sree"]
# name_list1=["Shiva","Gayathri","Ram","Sree"]
# name_list2=["my name is shiva"]
# for name in name_list:
#   print(name.capitalize())
#    print(name.casefold())
#    print(name.center(10))
    #  print(name.count("ram"))
    #  print(name.encode()) 
#    print(name.endswith("a"))
#    print(name.startswith("r"))
#    print(name.find("a"))
    # print(name.index("ram"))
    # print(name.lower())
#    print(name.upper())
#    print(name.join("hello"))
#    print(name.replace("shiva","ram"))
#    print(name.title())
#   print("hi".join(name))   

# sum_list=[100,200,300,400,500]
# sum=0
# enum=enumerate(sum_list)
# for i,num in enum:
#     print(num)
#     # print("entering the process :"+str(i))
#     print("before",sum)
#     sum=sum+num
#     print("after",sum)
#     # print("existing the process :"+str(i))
#     print("\n")

# avg=sum/len(sum_list)  
# print(avg)
# cost_list=[1,2,3,4,5]
# emty=[]
# for number in cost_list:
#     inr=("INR"+str(number))
#     emty.append(inr)

# print(emty)  
names=["siva",'ram',"gayathri","sree"]
x=names.sort()
print(names)