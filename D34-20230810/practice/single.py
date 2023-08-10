list=[1,2,2,3]
dic={}
for i in list:
    if i not in dic:
     dic[i]=1
    else:
     dic[i]=dic[i]+1  
  
for j in dic:
  if dic[j]==1:
   print(j)



     