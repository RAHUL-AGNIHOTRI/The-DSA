from re import *


str='''
Keep the blue flag 
flying high 
Chelsea'''

print(str)

x=compile('\n')

str=x.sub("\f",str)

print(str)

# \b:backspace
# \f:formfeed
# \r:carriage return
# \t:tab
# \v:vertical tab