from operator import *
from screen_support import *
from constans import *
def Calculator():
    while True:
        print("--"*20)
        print("Toplama :+ çıkartma :- \nÇarpmma :* Bölme :/ \nÜst alma:** Karekök :// \nÇıkış yapmak için q yada Q tuşuna basınız.")
        print("--"*20)
        choise = get_Choise()
        print("--"*20)
        if choise == exit or choise == Exit:
            print("Güle Güle")
            break
        a = get_number_a()
        if choise == Square_root:
            Square_root(a)
        b = get_number_b()
        if choise == Add:
            add(a,b)
        elif choise == Minus:
            (a,b)