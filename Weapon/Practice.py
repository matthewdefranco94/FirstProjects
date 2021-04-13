# #practice follow along

# #use classes to define new types
# class Point:
#     def __init__(self , x , y):
#         self.x = x
#         self.y = y
#     #defines methods and functions
#     def move(self):
#         print("move")
    
#     def draw(self):
#         print("draw")

# #to create an object and to have attributes
# # point1 = Point()
# # point1.x = 10
# # point1.y = 20
# # print(point1.x)
# # print(point1.y)
# # point1.draw()

# # point2 = Point()
# # point2.x = 1
# # print(point2.x)

# ########################################



# class Person:
#     #this method is a contructor
#     def __init__(self , name):
#         self.name = name

#     #creates a method
#     def talk(self):
#         print(f"Hi, i am {self.name}")

# john = Person("John Smith")
# john.talk()

# bob = Person("Bob Smith")
# bob.talk()


##################################################
 
#Inheritance
# class Mammal():
#     def walk(self):
#         print("Walks")

# class Dog(Mammal):
#     def bark(self):
#         print("the dog barks")

    
# class Cat(Mammal):
#     def be_annoying(self):
#         print("the cat is annoying")


# dog1 = Dog()
# dog1.walk()
# dog1.bark()
# cat1 = Cat()
# cat1.walk()
# cat1.be_annoying()


######################################

#Modules
# #should contain related functions and modules

# import converters
# from converters import kg_to_lbs

# print(kg_to_lbs(100))
# print(converters.kg_to_lbs(70))



import Utils
from Utils import find_max

numbers = [10 , 3 , 6 , 20]
maximum = find_max(numbers)
print(maximum(numbers))

