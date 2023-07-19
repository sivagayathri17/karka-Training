
bios=[{"name" : "shiva",
      "age" : 10,
      "place" : "kottar"},

      {"name" : "ram",
       "age" : 22,
       "place" : "thamaraikulam",},

       {"name" : "gayathri",
        "age" : 25,
        "place" : "nagercoil",},

        {"name" : "sree",
         "age" : 30,
         "place" : "putheri"}]

def bio_nap(bios):
 for bio in bios:
    name=bio["name"]
    age=bio["age"]
    place=bio["place"]
    print(f"I am {name}, I am  {age} , I am form {place}\n")
# (bio_nap(bios))

def age_above_21(bios): 
 for bio in bios:
   name=bio["name"]
   age=bio["age"]
   place=bio["place"]
   if bio["age"]>21:
    print(f"I am  {name},I am {age},I am form {place}") 
# age_above_21(bios) 
if bio_nap(bios):
    (bio_nap(bios))
elif age_above_21(bios):
      age_above_21(bios) 