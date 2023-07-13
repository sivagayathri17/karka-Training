def num(a,opretor,b):
   if opretor=="+":
    return(a+b)
   elif opretor=="-":
    return(a-b)
   elif opretor=="*":
     return(a*b)
   else:
      return(a%b)
a=int(input("Ente the f_number :"))
opretor=input("Enter the opretor :")
b=int(input("Enter the s_number:" ))
check=num(a,opretor,b)
print(check)
