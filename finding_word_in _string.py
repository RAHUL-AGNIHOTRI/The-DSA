from re import *

String = "We need to inform him with the latest information."

x = search('inform',String)

if x:
    print("inform found")
else:
    print("inform not present")

y = findall('inform',String)

[print(i) for i in y]