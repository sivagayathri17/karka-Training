password=input("enter the password : ")
len_pass=len(password)
def passw(len_pass):
    if len_pass<6:
        return("week")
    elif 6<len_pass<10:
        return("moderate")
    elif 11<len_pass<15:
        return("strong")
    elif len_pass>15:
        return("very strong")
    
upper=False
lower=False
digit=False
for passwo in password:
        if passwo.isupper():
            upper=True
        elif passwo.islower():
            lower=True
        elif passwo.isdigit():
           digit=True
if upper==True and lower==True and digit==True:
    output=passw (len_pass)
    print(output)
else:
     print("try anothor password")   
               

             


    
