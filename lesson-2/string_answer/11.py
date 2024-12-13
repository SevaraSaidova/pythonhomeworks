a=str(input("So'z kiriting: "))
if any(str.isdigit() for str in a):
        print (f"Raqam bor!")
else:
        print (f'Raqam yo\'q!')