lists=[1,2,3,4,5,2,5,6,1,3]
# new=list(set(lists))
# print(new)
original=[]
for list in lists:
    if list not in original:
     original.append(list)
print(original)
        



