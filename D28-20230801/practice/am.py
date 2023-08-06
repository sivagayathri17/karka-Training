number=(input("enter the number :"))
count=(len(str(number)))
# print(count)
num=0
for i in range(count):
    # print(number[i])
    am=int(number[i])**count
    num=am+num
    # tot=num

    
    if number==num:
        print(f"{num} is armstrong number.")
    else:
        print(f"{num} is not armstrong number.")    


