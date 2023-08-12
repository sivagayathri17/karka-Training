s="abcabcbb"
em=""
for i in s:
    if i not in em:
        em=em+i
print(f"the ans is {em},with the length{len(em)}")
    