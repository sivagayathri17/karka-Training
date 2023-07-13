name=input("Hey,what is your name:")
old=int(input("ok , how old are you :"))
# print(f"{name},how old are you? {old}")
if old<16:
    print("you can't drive",name)
if old<18:
    print("you can't vote",name)  
if old<25:
    print("you can't rent a car",name)
if old>=25:
    print("you can do any thing that's legal",name)   
     


