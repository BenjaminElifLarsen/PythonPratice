file = open("readme.txt", "rt")
print(file.read())
file.close()
file = open("readme.txt", "rb")
print(file.read())
file.close()
file = open("readme.txt", "rt")
print(file.read(5))
file.close()
createdFile = open("newFile.txt", "w")
createdFile.write("Hey there")
createdFile.close()
createdFile = open("newFile.txt", "rt")
print(createdFile.read())
createdFile.close()

import os
if os.path.exists("newFile.txt"):
    os.remove("newFile.txt")
