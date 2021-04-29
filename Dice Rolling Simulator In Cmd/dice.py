import random

one = """
-----------
|         |
|         |
|         |
|    0    |
|         |
|         |
-----------
"""

two = """
-----------
|         |
|         |
|         |
|   0 0   |
|         |
|         |
-----------
"""

three = """
-----------
|         |
|  0      |
|         |
|    0    |
|         |
|      0  |
-----------
"""

four = """
-----------
|         |
|  0   0  |
|         |
|         |
|  0   0  |
|         |
-----------
"""

five = """
-----------
|         |
|         |
|  0   0  |
|    0    |
|  0   0  |
|         |
-----------
"""

six = """
-----------
|         |
|  0   0  |
|  0   0  |
|  0   0  |
|         |
|         |
-----------
"""


numbers = [one,two,three,four,five,six]
while 1:
    print(random.choice(numbers))
    ins = input("Enter y if you want to roll dice again else n to stop.")
    if ins == 'y':
        continue
    else:
        break