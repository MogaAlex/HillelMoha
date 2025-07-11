lst = [12,3,4,10,8]
lenght = len(lst)
if lenght == 0:
    print(lst)
else:
    v = lst[-1]
    lst.insert(0,v)
    lst.pop(-1)
    print(lst)
