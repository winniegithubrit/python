# name = "JOHN" 
# print(name)
# #creating user inputs in python
# namer = input("What is your name? ")
# print(namer)
# geans = "johney"
# print(geans)
# print(f"i want to see {geans}")
# #functions in python
# def player(number1,number2):
#   print(number1 * number2)
# player(23,66)
# def average(num1,num2):
#   addition = num1 + num2
#   return addition / 2

# #   print(addition / 2)
#   print(average(100,20))
#while loop
# loop = 10
# while loop <100:
#   print(loop)
#   print("Hello there!")
#   loop = loop + 1
#   #for loop
# i = 0 
# for i in range(10):
#   print(i)
programming_languages = ["Python","Java","JavaScript","Ruby"]
# for i in range(len(programming_languages)):
#    print(programming_languages[i])
# for  k in programming_languages:
#   print(k)
# thisdict = {
#   "brand": "Ford",
#   "electric": False,
#   "year": 1964,
#   "colors": ["red", "white", "blue"]
# }
# for key,value in thisdict.items():
#   print("name of book:" + key)
#   print(value)
#reverse looping
# persons  = [1, 2, 'Python', 'Program', 15.9]
# for people in reversed(persons):
#   print(people)
class Item:
  all = []
  rate = 0.8
  def __init__(self,name,price,quantity):
    self.name = name
    self.price = price
    self.quantity = quantity
    Item.all.append(self)
  def calculate(self):
    return self.price * self.quantity
# applying discount to our class
  def discount(self,price):
    self.price = price * Item.rate
  
item1 = Item("Clara",100,2)
item1.discount(100)
print(item1.name)
print(item1.price)
print(item1.quantity)
print(item1.calculate())
print(item1.price)
for instance in Item.all:
  print(instance.name)


# class Things:
#   def __init__(self,namer,quantifier):
#     self.namer =  namer
#     self.quantifier = quantifier
    
#     return self.namer * self.quantifier
#   item2 = Things(100,40)
#   print(item2.namer)
#   print(item2.quantifier)
    