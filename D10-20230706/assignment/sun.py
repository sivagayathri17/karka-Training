sum_list=[100,200,300,400,500]
sum=0
enum=enumerate(sum_list)
for i,num in enum:
    print(num)
    print("entering the process :"+str(i))
    print("before",sum)
    sum=sum+num
    print("after",sum)
    print("existing the process :"+str(i))
    print("\n")

avg=sum/len(sum_list)  
print(avg)
cost_list=[1,2,3,4,5]
emty=[]
for number in cost_list:
    inr=("INR"+str(number))
    emty.append(inr)

print(emty)  


    