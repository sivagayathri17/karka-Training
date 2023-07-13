# lists=[1,2,10,4,5]
# max=0
# for list in lists:
#    if list>max:
#        max=list
# print("large number is :",max) 

def large_list(lists):
   max=0
   for list in lists :
        if list>max:
            max=list
   return(max)
lists=[1,2,10,4,5]
print("large num is :",large_list(lists))


   