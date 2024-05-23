#!/usr/bin/env python3
'''lab 2 from samir thapa'''

import sys
if len(sys.argv) != 3:
    print(f'Usage: {sys.argv[0]} name age')    # many hit and trial still confused
    sys.exit()

name = sys.argv[1]
age = sys.argv[2]

print('Hi ' + name + ', you are ' + str(age) + ' years old.')