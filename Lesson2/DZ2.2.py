print ("Vedite 5-znachnoe chislo:")
num = int(input())
a = num//10000
b = num//1000%10
c = num//100%10
d = num//10%10
e = num%10
sum = a+b*10+c*100+d*1000+e*10000
print(sum)
