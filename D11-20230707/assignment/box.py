print("""TWO QUESTION! 
          Think of an object,and I,ll try to gyess it.""")
avm=(input("Question 1) Is it animal,vegetable,or mineral? \n"))
b=(input("Question 2) Is it bigger than a box ?\n"))

def object(avm):
    if avm=="animal" and b=="no":
         return("squrial")
    elif avm=="animal" and b=="yes":
         return("moose")
    
      
    if avm=="vegetable" and b=="no":
       return("carrot")
    elif avm=="vegetable" and b== "yes":
        return("watermelon")
    
    
    if avm=="mineral" and b=="no":
        return("paper clip")
    elif avm=="mineral" and b=="yes":
        return("camara")
      
         
check=object(avm)  
print(f"My guess is that you are thinking of a  {check}. \n I would ask you if I'm right ,but I son't actually care" )   
