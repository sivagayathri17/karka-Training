name_list=["shiva","salini","vinusha","vijay","abi","peru"]
# print(name_list)

name_set={"shiva","salini","vinusha","vijay","abi","peru"}
# print(name_set)

my_name=name_list[0]
print(my_name)
# n=n+n-1
friends=name_list[1:3] 
print(friends)
boys=name_list[3:7]
print(boys)

# my_name=name_set[0]
# print(my_name) // error:set is a unordered 
# sliceing
four_name=name_list[0:4]
print(four_name)

# string
string="shiva"
two_num=string[0:2]
print(two_num)

print(name_list[0])
print(name_list[1])
print(name_list[2])
print(name_list[3])
print(name_list[4])
print(name_list[5])

number_list=["one","two"]
for name in name_list:
    # upper->caps ; capitalize ->first letter change caps
    print(name.upper())
    print(name.capitalize())
    print (f"my name is :{name}")
