# print("hello World")


# for i in "hello World":
#     if i == "o":
#         continue
#     print(i)


# word_list = list("hello world")
# lengh = len(word_list)

# while 0 < lengh:

# list = []
# for i in range(1 ,11):
#     list.append(i**2)

# value = [i**2 for i in range(1,11)]
# print(value)

import random
number = random.randint(1 ,999)
print(number)

if number%15 == 0:
    print("fizzbazz")
elif number%5 == 0:
    print("bazz")
elif number%3 == 0:
    print("fizz")
