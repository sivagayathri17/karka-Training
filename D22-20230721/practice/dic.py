import json
bio={"name":"shiva",
       "age":20,
       "about":"lazy girl"}
def bio_json():
 d_json=json.dumps(bio)
 # print(str(d_json))
#  new=json.load(d_json)
 # print(new)
 data=input("enter:")
 if data=="dumps":
    print(d_json)
 # elif data=="load":
 #     print(new)   
bio_json() 


