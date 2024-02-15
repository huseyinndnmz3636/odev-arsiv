from math import sqrt
def add(a,b):
    total = a+b
    print("Sonuç : ",total)
    print("--"*20)
def milus(a,b):
    total = a-b
    print("Sonuç : ",total)
    print("--"*20)
def mult(a,b):
    total = a*b
    print("Sonuç : ",total)
    print("--"*20)
def divide(a,b):
    if b == 0:
        print("0 hiç bir sayıyı bölünemez")
    else:
        total = a/b
        print("Sonuç : ",total)
    print("--"*20)
def taking_top(a,b):
    total = a**b
    print("Sonuç : ",total)
    print("--"*20)
def square_root(a,):
    total = sqrt(a)
    print("Sonuç : ",total)
    print("--"*20)