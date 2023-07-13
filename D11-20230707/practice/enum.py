lists=[1,2,3,4,5,45,18,20]
def find(lists):
 for i,list in  enumerate(lists):
    if list==45:
      return i
print(find(lists))    
    
