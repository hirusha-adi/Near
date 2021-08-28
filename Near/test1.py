import os, sys

file = open("pwds2.txt", "r")
lines = file.readlines()

pwds = []
for line in lines:
    data = line.split()
    for item in data:
        pwds.append(item)

if "password5" + "\n" in lines:
    print(True)
else:
    print(False)




