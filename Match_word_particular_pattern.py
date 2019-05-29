from re import *

str = 'Sat Hat Mat Rat'

pat_mth = findall('[SHMR]at',str)

print(pat_mth)

pat_mth = findall('[H-Z]at',str)

print(pat_mth)

pat_mth = findall('[M-R]at',str)

print(pat_mth)

pat_mth = findall('[^M-R]at',str) # ^ acts as complement

print(pat_mth)