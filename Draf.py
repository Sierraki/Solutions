from collections import defaultdict, Counter
from math import sqrt, floor
import bisect

boxes = [4, 3, 4, 1]
warehouse = [5, 3, 3, 4, 1]

mi = float("inf")
for idx, i in enumerate(warehouse):
    mi = min(mi, i)
    warehouse[idx] = mi

print(warehouse)
boxes.sort()
print(boxes)
cnt = 0
top = len(warehouse) - 1
dow = 0
while dow < (len(boxes)) and top>=0:
    if boxes[dow] <= warehouse[top]:
        cnt += 1
        dow += 1
        top -= 1
    else:
        top -= 1
    print(cnt)
