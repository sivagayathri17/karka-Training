marks=[{"name":"shiva",
        "mark":[1,2,3,4,5]},
        {"name":"ram",
        "mark":[2,4,3,5,6]},
        {"name":"gayathri",
         "mark":[8,3,6,2,9]}]
def tot_marks():
 for all in marks:
    mark_list=(all["mark"])
    name=all["name"]
    # print(mark_list)
    num1=mark_list[0]
    num2=mark_list[1]
    num3=mark_list[2]
    num4=mark_list[3]
    num5=mark_list[4]
    tot=num1+num2+num3+num4+num5
    # print(tot)
    print(f"name :{name}\n tot_mark:{tot}")


    # len_mark=len(mark_list)
    # print(len_mark)
    # tot=sum(mark_list)
    # print(tot)
# tot_marks()
add_marks=str(tot_marks())
print(add_marks) 

with open ("/home/siva/tot.txt","w") as file: 
  file.write(add_marks) 



