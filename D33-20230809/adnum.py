# num=[1,2,3]
# n=len(num)
# change=n-1
# if num[change]<9:
#     num[change]= num[change]+1 
#     print(num)

# num1=[4,3,2,1]
# n=len(num1)
# change=n-1
# if num1[change]<9:
#     num1[change]=num1[change]+1
#     print(num1)

# num2=[9]
# n=len(num)
# change=n-1
# if num[change]<9:
#     num[change]= num[change]+1
#     print(num)

num=[1,2,3,4,5]
em=[]
str_num=""
for i in num:
    str_num=str_num+str(i)
    a=int(str_num)+1
    b=str(a)
for j in b:
    em.append(int(j))
print(em)    























