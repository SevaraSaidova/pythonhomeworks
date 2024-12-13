a=str(input("so'z kiriting: "))
b="aoueiAOUEI"
c=''.join('*' if str in b else str for str in a)
print("natija: ", c)