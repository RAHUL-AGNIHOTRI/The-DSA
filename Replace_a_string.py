from re import *

str="Rahul and Rahul are good friends."
x = compile("[R]ahul")
str = x.sub('ishi',str)
print(str)

str="Rahul and Rahul are good friends."
x = compile("ahul")
str = x.sub('ishi',str)
print(str)

str="Rahul and Rahul are good friends."
print(str.replace('ahul','Rishi'))

str="Rahul and Rahul are good friends."
x = compile("ahul\s")
str = x.sub('ishi',str)
print(str)
