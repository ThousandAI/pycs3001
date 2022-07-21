# 迴圈 + 串列 (練習2)
# 1.
"""
numbers = [3, 2, 7, 8, 1, 10, 15]
numbers.reverse()
for v in numbers:
    print(v,end=" ")
"""
"""
# 2.
numbers = [3, 2, 7, 8, 1, 10, 15]
for i in range(len(numbers)-1, -1, -1):
    print(numbers[i],end=" ")
"""

# 迴圈 + 串列 (練習 3)
"""
n = int(input())
ans = []
for i in range(n):
    ans.append(int(input()))
print(ans)
"""

# 迴圈 + 串列 (練習 4)
"""
n = int(input())
ans = []
for i in range(n):
    ans.append(int(input()))
print(f"總和: {sum(ans)} 最大值: {max(ans)} 最小值: {min(ans)}")
"""

# String
"""
name = "Thousand"
print(name[0])
print(len(name))
print(name.upper())
print(name.lower())
print(name[0].islower())
print(name[0].isupper())
"""

# 迴圈 + 字串 (練習 1)
"""
x = input()
ans = []
for v in x.split(): # 依照空格切
    ans.append(int(v))
print(ans)
"""

# 迴圈 + 字串 (練習 2)
"""
s = input()
count = 0
for v in s:
    if v == "a":
        count += 1
print(count)
"""

# list comprehension
"""
ans = [i for i in range(20)]
print(ans)
"""
"""
numbers = [30,80,61,52,67,100,35,98]
ans = [v for v in numbers if v > 70]
# for v in numbers:
#     if v > 70:
#         ans.append(v)
print(ans)
"""

# function y = 2x + 3
"""
def add_numbers(x1, x2):
    print(x1+x2)

add_numbers(x1 = 3, x2 = 7)
"""

"""
score = 10 # global variable
#
def add():
    score # local variable
    print(score)

def sub():
    print("sub")

add()
print(score)
"""
# return
"""
def get_means(numbers):
    total = 0
    for v in numbers:
        total += v
    return total/len(numbers)

ans1 = get_means(numbers = [12,34,56])
ans2 = get_means(numbers = [35,27,100])
if ans1 > ans2:
    print("Ans1")
else:
    print("Ans2")
"""

# import
# import random
# import random as r
"""
from random import randint
for i in range(100):
    print(randint(1,10),end=" ")
"""

n = int(input())
import random
ans = [random.randint(1,100) for i in range(n)]
print(ans)