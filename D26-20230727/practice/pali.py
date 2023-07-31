# pali=input("enter the palindrome :")
# re_pali=[]
# index=-1
# for i in pali:
#    re_pali.append(pali[index])
#    index-=1 
# print(re_pali)
# if pali==str(re_pali):
#     print("yes, this word is palindrome")
# else:
#      print("this word is not palindrome")



name=input("enter the pali : ")
re_name=name[::-1]
print(re_name)
if name==re_name:
    print("yes,pali")
else:
    print("no,pali")    
    


