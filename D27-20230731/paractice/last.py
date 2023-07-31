lists=[1,0,3,0,9,13]
for list in lists:
    if list==0:
         lists.remove(0)
     #     print(list)
         lists+=["*"]
print(lists)
lists=[1,0,0,3,0,9,0,0,13]
for i in range(len(lists)):
     for j in range(i+1):
          if lists[j]==0:
               lists.remove(0)
               lists+=[9]
print(lists)          
     
