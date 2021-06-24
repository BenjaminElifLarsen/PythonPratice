#import matplotlib.pyplot as plt
#import numpy as np
import datetime
import json
import re as regex

msg = "hello"
print(msg)

#x = np.linspace(0,20,100)
#plt.plot(x,np.sin(x))
#plt.show()
if 5 > 2: 
    print("Five")
numberValue = int(3)
stringValue = str(3)
floatValue = float(3)
unknownValue = 3
print(type(numberValue))
print(type(stringValue))
print(type(floatValue))
print(type(unknownValue))

x,y,z = 1,"2", float(3)
print(x)
print(y)
print(z)

objects = ["Lumix G Vario lens 45-200mm","Lumix G X Vario II lens 14-42mm","m.zuiko digital ed 60mm f2.8 macro"]
x,y,z = objects
print(x)
print(y)
print(z)
print(objects[0:2])

multiLine = """this
is
on
multiple
lines
"""
print(multiLine)
print(len(multiLine))
print("is" in multiLine)
print("is" not in multiLine)
print("This is a test with a {0} with {1} pictures".format(objects[-2],2))

byte = 1
print(byte)
byte <<=1
print(byte)
byte <<=3
print(byte)
byte >>=2
print(byte)

print(~byte)

listOfData = ["1","2","3"]
print(listOfData)
del listOfData[2]
print(listOfData)
print(listOfData.clear())

newList = [x for x in objects if "." in x]
print(newList)

valuesTuple = (12,3,5,12,3)
(first,second,*rest) = valuesTuple
print(first)
print(second)
print(rest)

setOfData = {1,2,3,4,5,6,7,8}
print(setOfData)

dictionaryOfData = {
    "test" : "value",
    "testValue" : 2
}
print(dictionaryOfData)
print(dictionaryOfData["test"])

nestedData = {
    "Panasonic" : ["Lumix G Vario lens 45-200mm","Lumix G X Vario II lens 14-42mm"],
    "Olympus" : ["m.zuiko digital ed 60mm f2.8 macro"]
}
print(nestedData)
print(nestedData["Panasonic"][1])

print("a") if 2 > 5 else print("B")
print("a") if 2 < 5 else print("B") 

print(datetime.datetime.now())

jsonData = '{"name": "bob", "age": 1221}'
print(json.loads(jsonData)["name"])

print(json.dumps(nestedData, indent=1, sort_keys=True )) #separators=(". "," = ")

try:
    print(doesExist)
except NameError as e:
    print(e)
except:
    print("did not work")
else:
    print("Else is run if nothing went wrong")
finally:
    print("Finally done")
x = 6
if x < 5:
    raise Exception("Cannot be below 5")
if not type(x) is int:
    raise TypeError("Only integers are permitted")

print("Name is " + input("Enter name: "))


