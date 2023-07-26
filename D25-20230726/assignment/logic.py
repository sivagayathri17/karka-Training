# print("x"*5,)
# num=5
# abcd=("x"*num)
# # print(abcd*5) 
# for abc in num:
#     print(abcd)

vals=int(input("enter the num :"))
for num in range(vals):
    print("x"*vals)

for num in range(vals):
    for nums in range(vals):
        print("*",end=" ")
    print(" ")    

