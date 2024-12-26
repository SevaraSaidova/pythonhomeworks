a=str(input("Gap kiriting: "))
b=a.split()
c=''.join(word[0].upper() for word in b)
print(c)