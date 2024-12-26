a=str(input("So'z kiriting: "))
b="aoueiAOUEI"
i=0

for str  in a:
    if str in b:
        i=i+1
print (f"Unli harflari {i} ta.")
print(f"Undosh harflari {len(a)-i} ta.")