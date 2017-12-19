#Classes and Inheritance
#With Arguments and Keyword Arguments
#arg = Positional Arguments
#kwarg= keyword argument
#Note
#instance of car is also a object of car
#if you change the name field in the obj it would not affect the nane in the instance both have the different copies of the class to themseleves
#self argumnet is built in argument of the class

class Automobile():
    name="Ferrari"
    wheels="Four"
    Class="Sedan"
    color="Black"
    def get_color(self,model):
        return self.color
    def get_wheels(self):
        return self.wheels
model="911 or i8"
BMW = Automobile()
BMW.get_color(model)
BMW.Class="SUV"

def some_func(arg1,arg2,kwarg1=None,kwarg2=None):
    pass
    print(arg1,arg2)
    if kwarg1 != None:
        print(kwarg1)

some_func("Ferrari","Car",kwarg1="$2000000")


class Car(Automobile):
    name = "Porche"
    color = "White"
Porche=Car()
Porche.color="Blue"
Porche.Class="SUV"


