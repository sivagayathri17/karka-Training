weight=int(input("please,enter your current earth weight : "))
print("I have information for the following planets :\n 1.vrnus \t 2.mars \t 3.jupite \n 4.saturn \t 5.uranum \t 6.neptune")
planet=(int(input("whice planet are you visiting ?")))
def gravity(planet):
    if planet==1:
        return(weight*0.78)
    elif planet==2:
        return(weight*0.39)
    elif planet==3:
        return(weight*2.65)
    elif planet==4:
        return(weight*1.17)
    elif planet==5:
        return(weight*1.05)
    elif planet==6:
        return(weight*1.23)
check=gravity(planet)   

print(f"your weight would be {check} pounds on that planet")