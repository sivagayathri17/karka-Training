marks=[{"name":"shiva",
        "mark":[1,2,3,4,5]},
        {"name":"ram",
        "mark":[2,4,3,10,1]},
        {"name":"gayathri",
         "mark":[8,3,6,2,9]}]
def tot_marks(): 
 marks1=marks[0]["mark"]
 marks2=marks[1]["mark"]
 marks3=marks[2]["mark"]
 
 num=0
 for mark1 in marks1:  
     if mark1 >num:
      num=mark1
      name=marks[0]["name"]
      
 print(f"{name}\n total high mark:{num}")

 num=0
 for mark2 in marks2: 
  if mark2>num:
    num=mark2
    name=marks[1]["name"]
 print((f"{name}\n total high mark:{num}"))

 num=0
 for mark3 in marks3:
   if mark3 >num:
     num=mark3
     name=marks[2]["name"]
 print((f"{name}\n total high mark:{num}")) 
tot_marks()     
