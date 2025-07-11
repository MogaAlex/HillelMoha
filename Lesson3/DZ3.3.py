lst = [1,2,3,4,5,6]

lenght = len(lst)
halflength= int(len(lst)/2)
if lenght%2==0:
    a = lst[:halflength]
    b = lst[halflength:]
    c = [a] + [b]
    print(c)
else:
    a = lst[:halflength+1]
    b = lst[halflength+1:]
    c = [a] + [b]
    print(c)

