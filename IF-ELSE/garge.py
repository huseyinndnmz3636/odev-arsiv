my_car = "BMW"

def paintgaraga(car):
    modifiye_car = "dark blue" + car
    return modifiye_car

#1 usage
def showroom(car):
    print("-----------")
    print(car)
    print("------------")
    
    #1 usage
    my_car = paintgaraga (my_car)
    showroom(my_car)