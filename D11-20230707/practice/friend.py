names=["abi","shunmu","gayathri","bindhu","maha"]  
def bfrient(names):
  for i,name in enumerate(names):
    if name=="gayathri":
     return i
print("Your best friend name index is :" ,bfrient(names))

def len_bfname():
 lists= ["gayathri","shiva","shalu","vinusha"]
 for list in lists:
  a=len(list)
  my_bfname="gayathri"
  b=len(my_bfname)
  if a==b:
   print(b)
len_bfname()   


