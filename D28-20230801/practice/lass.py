details=[{"name":"shiva",
          "email":"ggayathri4142@gmail.com",
          "password":"ram123",
          "hobbies":["dance","coding","music"],
          "friends_list":["gayathri","abi","ram"]},
          {"name":"ram",
          "email":"sreeram17@gmail.com",
          "password":"shiva123",
          "hobbies":["pleanding","art","music"],
          "friends_list":["abisha","rose","shiva"]},
          {"name":"abi",
          "email":"ab12345@gmail.com",
          "password":"abirose",
          "hobbies":["writing","dance","music"],
          "friends_list":["gayathri","abi","ram"]},]
user_m=input("enter the mail id : ")
user_p=input("enter the password : ")
for detail in details:
    user_mail=(detail["email"])
    user_pass=(detail["password"])

    if user_mail==user_m and user_pass==user_p:
         print("your hobbies are:",detail["hobbies"])
         print("your friend list is :",detail["friends_list"])
         detail["login"]="True"
        #  print(detail["login"])
        #  detail.update({"login":"true"})
    else:
            detail["login"]="False"
            # print(detail["login"])  
            # detail.update({"login":"false"})         
              
print(details)