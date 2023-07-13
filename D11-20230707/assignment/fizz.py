for num in range(1,101):
    print(num)
    three=num%3
    five=num%5

    if three==0 :
        print("chikku")
    elif five==0:
        print("bakku")  
    elif three==0 and five==0:
        print("chikku bakku")
