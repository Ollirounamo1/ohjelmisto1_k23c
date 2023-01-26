def parilliset(lukulista):
    parilliset = []
    for luku in lukulista:
        if luku % 2 == 0:
            parilliset.append(luku)
    return parilliset


luvut = [1,2,3,4,5,6,7,8,9,10]
print(luvut)
print (parilliset(luvut))