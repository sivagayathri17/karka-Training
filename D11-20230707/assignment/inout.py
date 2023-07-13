print("""TWO MORE QUESTIONS !!!
         Thinks of sometheing and I'll try ti guess it! """)
Q1=input("1) does it stay inside or outside or both ?  ")
Q2=input("2) is is a living thing ?  ")
def ques(Q1,Q2):
    if Q1=="inside" and Q2=="alive":
        print("It is a living thing and It is living inside of home( houseplant)")

    if Q1=="inside" and Q2=="not alive":
        print("It is a not living thing and It is inside of home (shower curtain)")

    if Q1=="outside" and Q2=="alive":
        print("It is a living thing and It is living outside of home (bison)")

    if Q1=="outside" and Q2=="not alive":
        print("It is a not living thing and It is outside of home (billboard)")

    if Q1=="both" and Q2=="alive":
        print("It is a liveing thing and It is living both of home( dog)")  

    if Q1=="both" and Q2=="not alive":
        print("It is a not living thing and It is both of home (cell phone)") 
ques(Q1,Q2)