# #create a car class with attribute like brand and model.then create an instance of this class
# class Car:
#     total_car=0
#     def __init__(self,brand,model):
#           self.__brand=brand     #__brand now this is private attribute to use this variable we need getter method
#           self.model=model
#           Car.total_car+=1
#     @property
#     def brand(self):
#          return self.__brand+'!'
         
#     ##add another method in class which prints full name brand and model
#     def full_name(self):
#          return f'{self.brand} have {self.model}'
#     #polymoephism
#     def fuel_type(self):
#          return 'diesel or petrol'
#     @staticmethod
#     def description():
#          return 'Heloo new buyer'
#     ##inherit a new class electric car from car class and in thia class give an attribute battery_size.
# class Electric_car(Car):
#      def __init__(self,brand,model,battery_size):
#         super().__init__(brand,model)
#         self.batterysize=battery_size
#      @property
#      def batterysize(self):
#           return self._batterysize

#      @batterysize.setter
#      def batterysize(self, value):
#            if value > 65:
#                 self._batterysize = value
#            else:
#                 print("Invalid size")
#      def fuel_type(self):
#          return 'Electric supply '

# my_electriccar=Electric_car('Tesla','Model S5',85 )
# my_car=Car('Toyota','corolla')
# my_new_car=Car('Hyundai','Creta')
# print(my_car.description())
def sum(a=12,b=10):
    return a+b
print(sum(2))