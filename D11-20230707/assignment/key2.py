print("ye olde keychain shoppe")
num=0 
def add_key(num) :  
   a=int(input(f"you have {num} keychains . how many to add ? :"))
   add=num+a
   print (f"you have {add} keychains .") 
   return add

def remove_key(num): 
      r=int(input(f"you have {num} keychains . how many to remove ? :"))
      remove=num-r
      print(f"you have {remove} keychains .")  
      return remove

def view_key(num):
   print(f"you have {num} keychains .keychains cost $10 ")
   tot=10*num
   print(f"total cost is {tot}.")
   return tot

def checkout(tot):
   print("CHECKOUT")
   name=input("what is your name ?  ")
   print(f"you have {tot} keychains .") 
   print("keychains cost $10 each .")
   print(f"total cost is ${tot}")
   print(f"thanks for your order, {name}.")
 

while True:
    print("""1. add keychains to order
2. remove keychains from order
3. viw current order
4. checkout
""")
    want=int(input("please enter your choice :"))
    if want==1:
     num=add_key(num)
    elif want==2:
     num=remove_key(num)
    elif want==3:
      num=view_key(num)
    elif want==4:
     (checkout(num))
     break 