password=input("enter the password : ")
len_pass=len(password)
a=password.isalnum()
def passw(len_pass):
    if len_pass<6:
        return("week")
    elif 6<len_pass<10:
        return("moderate")
    elif 11<len_pass<15:
        return("strong")
    elif len_pass>15:
        return("very strong")
    
output=passw (len_pass)
   
print(output)
for passwo in password:
        if passwo.isupper or passwo.islower or passwo.isdigit:
           passw(len_pass)
else:
     print("try anothor password")             

             


    
