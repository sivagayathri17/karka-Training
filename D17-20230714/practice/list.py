# names=["shalu","shiva","vinu","abi","vijay"]
# for name in names:
    # print(name)
name_place=[{"name" : "shalu", 
             "place":"vdaseri",
             "hobbies" :["songs","friends chat","music"],
             },
             {"name" : "shiva", 
              "place":"kotter",
              "hobbeis" :["dance","music","drawing"],
              },
             {"name" : "abi", 
              "place": "kotter",
              "hobbies" :["music","browising","movie"],
             },
             {"name" : "vijay" ,
             "place":"marthandam",
             "hobbies" :["music","movie","cricket"],
            }]
for name in name_place:
 print(name)

hobbies=[{"name" : "shalu", 
             "place":"vdaseri",
             "hobbies" :["songs","friends chat","music"],
            } ]
for hobbie in hobbies:
  print(hobbie["name"]) 
  print(hobbie["hobbies"][1])