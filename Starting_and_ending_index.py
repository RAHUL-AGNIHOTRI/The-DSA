from re import *

String = "We need to inform him with the latest information."

for i in finditer('inform',String):
    loctup = i.start()
    print(loctup)

print('\n\n')

for i in finditer('inform',String):
    loctup = i.end()
    print(loctup)

print('\n\n')

for i in finditer('inform',String):
    loctup = i.span()
    print(loctup)