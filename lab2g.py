#!/usr/bin/env python3
'''this is part f of lab 2 from samir thapa'''
#Author: Samir Thapa
#Author ID: 132019217
#Date Created: 2024/05/22

import sys
# timer = int(sys.argv[1])
# while timer != 0:
#     print(timer)
#     timer = timer - 1
# print('blast off!')

# timer = int(sys.argv[1])

if len(sys.argv) > 1:              #checking if the length oof argument is added 0 is taken by pathname
    timer = int(sys.argv[1])
else:
    timer = 3

while timer != 0:
    print(timer)
    timer = timer -1

print('blast off!')