import numpy as np
import pandas as pd
import sys

lines = sys.stdin.readlines()
print(lines)

line_n = lines[0]
line_m = lines[1]

print(line_n, line_m)

count = 0
index = 0
for i in line_m:
    index += 1
    for j in line_n:
        if i == j:
            count += 1
            break

print(count)