string1=str(input("1-so'zni kiriting: "))
string2=str(input("2-so'zni kiriting: "))
if string2 in string1:
    print(f'{string2} {string1} da topildi!')
else:
    print(f'{string2} {string1} da topilmadi!')