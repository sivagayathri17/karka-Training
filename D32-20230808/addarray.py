nums=[[1,2],[3,4]]
em_list=[]
add=0
action=input("enter the operator :" )
for num in nums:
    for j in range(len(nums)):
        if action=="add":
            add=add+num[j]
            
        elif action =="string":
            em_list+=[num[j]]
           
if action=="add":
    print(add)
elif action =="string":               
    print(em_list)   

