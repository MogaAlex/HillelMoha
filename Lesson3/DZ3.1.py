a = int(input("Vedite pervoe zeloe chislo:"))
b = str(input("Vedite odin iz danih znakov '+', '-', '*', '/': "))
c = int(input("Vedite vtoroe zeloe chislo:"))
if b == "+":
    print(a+c)
elif b == "-":
    print(a-c)
elif b == "/" and c != 0:
    print (a/c)
elif b == "*":
    print(a*c)
elif b == "/" and c == 0:
    print("Na 0 ne delitsa")
else:
    print("Viberite pravilniy znak")
