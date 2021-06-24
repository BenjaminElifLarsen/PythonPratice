class TestingClass: 
 __privateValue = 4
 _protectedValue = 3
 def __init__(self):
     self.__number = 5
 def GetValue(self):
     return self.__privateValue
 def SetValue(self,value):
     self.__privateValue = value
 
 @property
 def value(self):
     return self.__number
 @value.setter
 def value(self, value):
     self.__number = value


class Person:
 something = "old"
 def __init__(self, name, age):
     self.name = name
     self.age = age
 def sayMyName(self):
     return self.name
 def testing(self):
     return self.sayMyName() + " 2"

class Kid(Person):
 kidStuff = "bugs"
 def __init__(self, firstName, lastName, age):
     super().__init__(firstName + " " + lastName, age)
 def nestedFunction(self):
     print("Outer")
     def innerFunction():
         print("Inner")
     innerFunction()

p1 = TestingClass()
try:
 print(p1.__number)
 p1.__number = 2
 p1.__number = 15
 print(p1.__number)
except Exception:
    print("did not work")
try:
    print(p1.value)
    p1.value = 223
    print(p1.value)
except:
    print("did not work")
p2 = Person("Bob",1223)
print(p2.name + " " + str(p2.age) + " is " + p2.something)
print(p2.sayMyName())
print(p2.testing())
k1 = Kid("Kid", "Ding",5)
print(k1.sayMyName())
print(k1.kidStuff)
k1.nestedFunction()