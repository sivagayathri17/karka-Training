marks=[{"name":"shiva",
        "mark":[1,2,3,4,5]},
        {"name":"ram",
        "mark":[2,4,3,5,6]},
        {"name":"gayathri",
         "mark":[8,3,6,2,9]}]
def tot_marks():
 num=0
 for all in marks:
    mark_lists=(all["mark"])
    print(mark_lists)
    for mark_list in mark_lists:
      
      marks_li=mark_list  
      add_mark=marks_li+num
      num=add_mark
    
    print(num)

    name=all["name"]
add_marks=str(tot_marks())
print(add_marks) 

# with open ("/home/siva/tot.txt","w") as file: 
#   file.write(add_marks) 



