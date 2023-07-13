name=input("Hey,what is your name :")
age=int(20)
print(f"(sorry,I keep forgetting.){name} ok,{name},how old are you?{age}")
if age<16:
    print("you can't drive",name)
if(16<=age<=17):
   print("you can drive,but not vote",name)
if (18<age>24):
    print("you can vote  but not rent a car",name)
if (25>age):
    print("you can so pretty nmuch anything",name)


