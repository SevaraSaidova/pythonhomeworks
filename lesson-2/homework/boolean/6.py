a=float(input("Son kiriting:"))
b=a%3
c=a%5
if b==0 and c==0:
    print("3 ga ham 5 ga ham bo'linadi")
else:
    if c==0:
        print("5 ga bo'linadi")
    else:
        print("3 ga ham 5 ga ham bo'linmaydi!")

