saree=int(input("Enter the price of saree :"))
kurthi=int(input("Enter the price of kurthi :"))
top=int(input("Enter the price of tops :"))
gown=int(input("Enter the price of gown :"))
total=(saree+kurthi+top+gown)
if total>=500 and total<=1000:
    print("you have owned a gold token")
else:
    print("You have owned a dimond token")

