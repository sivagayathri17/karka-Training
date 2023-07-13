def quice( ):
 ready=input("Are you ready for a quiz ?")
 if ready=="y":
    print("Okay,here it come !")
 else:
    return ("thankyou")
sum=0


print("Q1) What is tha capital of alaska ?")
a=int(input("1) Melbourne \n 2)Anchorage \n 3)juneau \n ANS :"))
if a==3:
    print("that's right")
    sum=sum+1
else:
    print("wrong")
    
    

print("Q2) can you store the value cat in a variable of type int ?")
b=int(input("1)yes \n 2)no \n ANS :"))
if b==1:
    print("sorry,cat is a string. ints can only store numbers.")

else:
    print("a,is the correct ans")   
    sum=sum+1

print("Q3) what is the result if 9+6/3 ?") 
c=int(input("1)5 \n 2)11 \n 15/3 \n ANS :")) 
if c==2:
    print("that is correct")
    sum=sum+1
else:
    print("worng")
print(f"overall,you got {sum} out of 3 correct. \n thanksyou")





   


