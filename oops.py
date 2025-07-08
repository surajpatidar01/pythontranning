#--Basic Class and objects (Create a car class with attributes like brand and model then crete an instance of this class.

# class Car:
#     def __init__(self,brand,model):
#         self.brand = brand
#         self.model = model
#
# my_car = Car("TaTa","Safari")
# print(my_car.brand)
# print(my_car.model)
#
# my_new_car = Car("Mahindra","Scorpio")
# print(my_new_car.brand)
# print(my_new_car.model)


#-Class method and self(add a method to the Car class that displays the full name of the car (brand and model).

# class Car:
#     def __init__(self,brand,model):
#         self.brand = brand
#         self.model = model
#
#     def full_name(self):
#         return f"{self.brand} {self.model}"
#
# my_car = Car("Toyota","corolla")
# print(my_car.brand)
# print(my_car.model)
#
# #full name uses
# print(my_car.full_name())




#-inheritance(Create an ElectricCar class the inherits from the Car class and has an additional attribute Battery size:

# class Car:
#     def __init__(self,brand,model):
#         self.brand = brand
#         self.model = model
#
#     def full_name(self):
#         return f"{self.brand} {self.model}"
#
# class ElectricCar(Car):
#     def __init__(self,brand,model,battery_size):
#         super().__init__(brand,model)
#         self.battery_size = battery_size
#
# my_car = Car("Toyota","Corolla")
# print(my_car.brand)
# print(my_car.model)
#
# my_new_car = Car("mahindra","Scorpio")
# print(my_new_car.brand)
# print(my_new_car.model)
#
# my_tesla = ElectricCar("Tesla","model S","85 KWh")
# print(my_tesla.full_name())



#-Encapsulation(Modify the Car class to encapsulate the brand attribute, making it private, and provide  getter method for it:

'''
class Car:
    def __init__(self,brand,model):
        self.__brand = brand
        self.model = model

    def get_brand(self):
        return self.__brand + " !"


    def full_name(self):
        return f"{self.__brand} {self.model}"

class ElectricCar(Car):
    def __init__(self,brand,model,battery_size):
        super().__init__(brand,model)
        self.battery_size = battery_size

# my_car = Car("Toyota","Corolla")
# print(my_car.__brand)
# print(my_car.model)
#
# my_new_car = Car("mahindra","Scorpio")
# print(my_new_car.__brand)
# print(my_new_car.model)
#
# my_tesla = ElectricCar("Tesla","model S","85 KWh")
# print(my_tesla.full_name())
my_tesla =  ElectricCar("Tesla","model S","85 KWh")
print(my_tesla.get_brand())
'''



#---Polymorphism(Demonstrate polymorphism by defining a method fuel_type in oth Car and ElectricCar classes ,but with different behaviors:)


# class Car:
#     def __init__(self,brand,model):
#         self.__brand = brand
#         self.model = model
#
#     def get_brand(self):
#         return self.__brand + " !"
#
#
#     def full_name(self):
#         return f"{self.__brand} {self.model}"
#
#     def fuel_type(self):
#         return "petrol or diesel"
#
# class ElectricCar(Car):
#     def __init__(self,brand,model,battery_size):
#         super().__init__(brand,model)
#         self.battery_size = battery_size
#
#     def fuel_type(self):
#         return "Electric charge"
#
#
# my_car = Car("Toyota","Corolla")
# print(my_car.fuel_type())
#
# my_tesla =  ElectricCar("Tesla","model S","85 KWh")
# print(my_tesla.fuel_type())




#--Class variables (Add a class variable to car that Keeps track of the number of cars created.)

# class Car:
#     total_car = 0
#     def __init__(self,brand,model):
#         self.__brand = brand
#         self.model = model
#         Car.total_car += 1
#
#
#     def get_brand(self):
#         return self.__brand + " !"
#
#
#     def full_name(self):
#         return f"{self.__brand} {self.model}"
#
# class ElectricCar(Car):
#     def __init__(self,brand,model,battery_size):
#         super().__init__(brand,model)
#         self.battery_size = battery_size
#
# my_car = Car("Toyota","Corolla")
# #print(my_car.__brand)
# print(my_car.model)
#
# my_new_car = Car("mahindra","Scorpio")
# #print(my_new_car.__brand)
# print(my_new_car.model)
#
# my_tesla = ElectricCar("Tesla","model S","85 KWh")
# print(my_tesla.full_name())
# my_tesla =  ElectricCar("Tesla","model S","85 KWh")
# print(my_tesla.get_brand())
#
# print(Car.total_car)




#--Static method (Add a Static method to the car class that return a general description of  a car .)


















