# while 無窮迴圈
"""
i = 0
while True:
    x = input()
    if x == 'Q':
        break
    print(x)
"""

# break vs. continue
"""
x = 0
while x <= 10:
    x = x + 1
    if x == 3:
        continue   # break
    print(x)
"""

# for

# i = 0
# while i < 6:
#     print(i,end=" ")
#     i = i+1

# for 迴圈解答 (1)
"""
n = int(input())
for i in range(1, n+1, 1):
    print(i,end=" ")
"""

# for 迴圈解答 (2)
"""
n = int(input())
for i in range(n, -1, -1):
    print(i,end=" ")
"""

# for 迴圈解答 (3)
"""
n = int(input())
ans = 0
for i in range(1, n+1, 1):
    ans = ans + i   # ans += i
print(ans)
"""

# for 迴圈解答 (4)
"""
n = int(input())
ans = 0
for i in range(0, n, 1):
    temp = int(input()) # temporary
    ans = ans + temp
print(ans)
"""

# while
"""
ans = 0
while True:
    temp = input()
    if temp == 'Q':
        break
    ans = ans + int(temp)
print(ans)
"""

# 1+2+3+4+5+6+7+8+9+10=55
"""
num = int(input())
ans = 0
for i in range(1, num+1, 1):
    if i == num:
        print(i,end="=")
    else:
        print(i,end="+")
    ans = ans + i
print(ans)
"""

# 串列
"""
numbers = [3, 5, 6, 10, 2, 8]
print(numbers[0])
print(numbers[3])
print(len(numbers))
print(numbers[-1])
print(numbers[1:3])
print(numbers[:3])
print(numbers[3:])
print(numbers[-3:])
"""

# 串列 methods
"""
numbers = [3, 5, 6, 10, 2, 8]
numbers.insert(2, 12)
print(numbers)
numbers.append(5)
print(numbers)
numbers.remove(5)
print(numbers)
numbers.pop()
print(numbers)
numbers.pop(0)
print(numbers)
numbers.reverse()
print(numbers)
numbers.sort()
print(numbers)
"""

# 串列 assign
"""
num1 = [1, 2, 3, 4, 5]
num2 = num1
num1.append(6)
print(f"num1: {num1}")
print(f"num2: {num2}")
num3 = num1.copy()
num4 = num1[:]
num3.append(7)
num4.append(8)
print(f"num1: {num1}")
print(f"num2: {num2}")
print(f"num3: {num3}")
print(f"num4: {num4}")
"""

# for + 迴圈 (解答1)
numbers = [3, 2, 7, 8, 1, 10, 15]

# 1.
# for i in range(len(numbers)):
#     print(numbers[i])

# 2.
for value in numbers: # iterable (迭代)
    print(value)
