for num in range(1,101):
    print(num)
    three=num%3
    five=num%5

    if three==0 and five==0:
        print("chikku bukku")
    elif five==0:
        print("bukku")  
    elif three==0 :
        print("chikku")
