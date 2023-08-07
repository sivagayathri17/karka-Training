word="the quick brown fox jumps over the lazy dog the quick brown fox"
a=word.split()
dic={}
for i in a:
   if i in dic:
      dic[i]=dic[i]+1     
   else:
    dic[i]=1
print(dic)        






    
    
