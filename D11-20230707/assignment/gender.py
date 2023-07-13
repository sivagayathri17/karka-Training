gen=input("What is your gender (M or F): ")
f_name=input("first name :")
l_name=input("last name :")
age=int(input("age :" ))
yn=input(f"Are you married,{f_name} (y or n) ?  ")
 
if age>20 and gen=="f":
    print(f"Then I shall call you Ms. {l_name}")
elif age>20 and gen=="m":
    print(f"Then I shall call you Mrs. {l_name}")
elif yn=="n" and gen=="m":
    print(f"Then I shall call you Mr. {l_name}")
