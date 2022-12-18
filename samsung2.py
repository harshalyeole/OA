# samsung2.py

import copy
l1 = [1,3, [9,4], 6,8]
l2 = copy.copy(l1)
l2[2][0] = 5

print(l1)
print(l2)