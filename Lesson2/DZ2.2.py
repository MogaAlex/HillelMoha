print ("Vedite 5-znachnoe chislo:")
num = int(input())
a = num//10000
b = num//1000%10
c = num//100%10
d = num//10%10
e = num%10
print(str(e)+str(d)+str(c)+str(b)+str(a))