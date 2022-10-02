def topla():
    print(x,"+",y,"=",x+y)

def cikart():
    print(x,"-",y,"=",x-y)

def carp():
    print(x,"x",y,"=",x*y)

def bol():
    print(x,":",y,"=",x/y)

def hesapla():
    global x
    global y
    global islem
    x = float(input("1. sayı = "))
    y = float(input("2. sayı = "))
    islem = input("işlemi girin = ")
    if islem is "+":
        topla()
    elif islem is "-":
        cikart()
    elif islem is "x":
        carp()
    elif islem is "/":
        bol()

hesapla()