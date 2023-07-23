bio={"name":"shiva",
     "age":20}
bio["dob"]=26_4_2003
print(bio)
my_resume={"Name" :"Siva Gayathri.V",
            "E-mail":"ggayathri4142@gmail.com",
            "Mobile-No":7904695594,
            "Soft_Skills" : "coding",
            "Hard_Skills" : ["dance","singing"],
            "Educational_Qualification" :[{"level":"SSLC",
                                           "instution":"st.joseph convent hir sec school",
                                          "passed":2018,
                                          "percetage":88,} ,
                                          {"level":"HSC",
                                           "instution":"st.joseph convent hir sec school",
                                            "passed":2020,
                                            "percetage":80} ,
                                          {"level":"collage",
                                           "instution":"st.hindu collage",
                                            "passed":2023,
                                            "percetage":90} ],
            "Project" : "Android Development-News Headline App",
            "Experience":[{"company_name":"TCS",
                          "role":"developer",
                          "duration":2} ,
                          {"company_name":"ralaventz",
                          "role":"developer",
                          "duration":1},
                          {"company_name":"flow",
                          "role":"developer",
                          "duration":1}],
            "Hobbies" : ["Dance","Music","Drawing"],
            "Personal_Details": {"Fathers name" :"Veera Lekshmanan.K",
                                 "Father's Occupation" :"Tailor",
                                 "Languages Known" :["Tamil","English"],
                                 "DOB" :26-4-2003 ,
                                 "Genter":"Female",
                                 "Martial Status" :"Not Married",
                                 "Address" : {"Door_No":"21-25",
                                              "Street Name" :"Veeraputhiran Street,Kottar",
                                              "District" :"kanyakumari",
                                              "pincode":160091}}, 
            }
# add country
my_resume["Personal_Details"]["Address"]["country"]="tamilnadu"
# add=my_resume["Personal_Details"]["Address"]
print(my_resume["Personal_Details"]["Address"])

# del country
del my_resume["Personal_Details"]["Address"]["country"]
print(my_resume["Personal_Details"]["Address"])

# update
name1={"name":"shiva",
       "age":20}
name2={"dob":26_4_2003,
       "blood":"o"}
name1.update(name2)
print(name1)
# keys() .values() items()
print(name1.keys())
print(name1.values())
print(name1.items())

list=dict(name="shiva",age=20)
print(list)

