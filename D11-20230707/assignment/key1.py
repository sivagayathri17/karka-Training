print("ye olde keychain shoppe")
print("""1. add keychains to order
2. remove keychains from order
3. viw current order
4. checkout
""")

def add_key() :
    print("add keychains") 

def remove_key()  :
    print("remove keychains") 

def view_key():
    print("view keychains")

def checkout():
    print("checkout")   
      
want=int(input("please enter your choice :"))        
if want==1:
    (add_key())
elif want==2:
    (remove_key())
elif want==3:
    (view_key())    
elif  want==4:
    checkout()