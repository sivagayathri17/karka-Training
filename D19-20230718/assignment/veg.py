lists=[{"name":"apple",
       "category":"fruits"},
      {"name":"carrot",
       "category":"vegitable"},
        {"name":"banana",
       "category":"fruits"},
        {"name":"broccoli",
       "category":"vegitable"},]
fruits=[]
vegitables=[]
for list in lists:
  cat=list["category"]
  if cat=="fruits":
    fruits.append(list["name"]) 
  if cat=="vegitable": 
   vegitables.append(list["name"])
 
print(fruits) 
print(vegitables)

fv_list={"fruits":fruits,
         "vegitables":vegitables}
print(fv_list)

    