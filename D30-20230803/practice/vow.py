ch=input("enter the char :")
vowel=["a","e","i","o","u","A","E","I","O","U"]
a=ch.split()
count=0
max_c=0
word=""
for i in a:
    for j in i:
       if j in vowel:
          count=count+1
    if count>max_c:
      max_c=count
      word=i

print(f"{word} large vowel of the word")