lists=[1,5,3,7,9,13]
num=10
for i in range(len(lists)-1):
    a=lists[i]
    for j in range((i+1),len(lists)):
        b=lists[j]
        c=a+b
        if c==num:
         print([i,j])
            