def z1():
    l = [1, 2, 3, 4, 5]
    x =int(input('vvedite chislo'))
    if x in l:
        print('vi ugadali')
        print(l)
    else:
        print('net,vi ne ugadali')
        print(l)
z1()

def z2():
    d = []
    s = [1, 3, 5, 3, 5, 2, 6, 8, 9]
    for x in s:
        if s.count(x) > 1:
            d.append(x)
    print(*d)
z2()


