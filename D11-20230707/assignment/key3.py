print("ye olde keychain shoppe")
tax=8.25
shipping_cost_per_order=5.00
addtional_cost=1.00
price=10
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

def view_key(num,price,shipping_cost_per_order,tax,addtional_cost):
   v_k=float(num*price*shipping_cost_per_order*(tax*addtional_cost))
   print(f"you have {num} keychains .Each keychains cost ${price} ")
   tot=(v_k/100)
   print(f"total cost is {tot}.")
   return tot

def checkout(tot,price):
   print("CHECKOUT")
   name=input("what is your name ?  ")
   print(f"you have {tot} keychains .") 
   print(f"keychains cost ${price} each .")
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
      num=view_key(num,price,shipping_cost_per_order,tax,addtional_cost)
    elif want==4:
     (checkout(num,price))
     break 