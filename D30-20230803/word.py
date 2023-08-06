place=input("enter the word : ")
a=place.split()
num=0
word=""
for i in a:
    le=len(i)
    if le>num:
     num=le
     word=i
print(f" {word} is the longest word")


