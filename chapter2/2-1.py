import random
import sys
import os
import subprocess
import shutil
import glob
import re
import math
from datetime import date
import time
import zlib
import numpy as np

# value = random.randint(1, 6)
# print(value)

# print(sys.platform)

# args = sys.argv

# sys.stdout.write("This is stdout text\n")
# sys.stderr.write("This is stderr text\n")
# hoge = list(sys.stdin.readlines())
# print(hoge)

# #print(args[0])
# # print(args[2])
# # print(args[3])

# # os.system("dir")

# # for i in range(100):
# #     #Import only if not previously imported
# #     # import cv2
# #     # VariableName = cv2.imread("Address",1)     #(flag = 0 or 1 or -1)
# #     print(i)
# #     if i == 10:
# #         sys.exit()

# currentDir = os.getcwd()
# print(currentDir)



# # os.system("ls")

# # os.mkdir("newDir")

# glob.glob("*.py")

# try:
#     subprocess.check_call("ls", shell=True)
# except:
#     print("sbustprocess error")


# print(re.findall(r"\bf[a-z]*", "which foot or hand fell fastest"))
# print(re.findall(r"\bw[a-z]*", "which foot or hand fell fastest which foot or hand fell fastest"))
# print(re.findall(r"\Bo[a-z]*", "which foot or hand fell fastest which foot or hand fell fastest"))
# print(re.findall(r"\Ba[a-z]*", "which foot or hand fell fastest which foot or hand fell fastest"))

# p = re.compile(r'([a-z]+)@([a-z]+)\.com')
# print(p, type(p))

# m = p.match("which foot or hand fell fastest which foot or hand fell fastest")
# print(m, type(m))

# #print(m.group(0))


# print(math.sqrt(2),
# math.sin(2*math.pi/180),
# math.cos(math.pi/2),
# math.log(1024, 2))

# now = date.today()
# print(now)

# print(now.strftime("%m-%d-%y. %d %b %Y is a %A on the %d day of %B."))

# s = b'where what who when why how'

# arr = np.array([1,2,3,4,5])
# print(arr)
# print(type(arr))

# arr2 = np.array([[1,2,3,4,5],[6,7,8,9,10]])
# print(arr2)

# # arr2.shape = (5,2) # 5行2列
# arr2.shape = (5,2)
# print(arr2)

# # print(arr2[0,1])
# # print(arr2[1,1])
# # print(arr2[2,1])
# print(arr2[1,0:])

# arr3 = np.array([1,2,3,4,5])

# print(arr3.sum())

arr4 = np.arange(10)
print(arr4)

arr5 = np.arange(10).reshape(2,5)
print(arr5)