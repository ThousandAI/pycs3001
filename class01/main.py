# Author: Thousand AI

# 註解

# 變數 Variable
"""
x = 3 # assign 賦值
y = 2.5
z = "Hello Python"
a = True
b = False

# 原生型態 Primitive type
print(type(x))
print(type(y))
print(type(z))
print(type(a))
print(type(b))
"""

# Pass by reference
"""
x = 3
y = x
print(id(x), id(y))
x = x + 1
print(id(x), id(y))
z = 4
print(id(z))
"""

# 輸出 print
"""
print("Hello") # 自動換行
print("Python")

print("Hello", end=" ")
print("Python")

print("Hello", end=",")
print("Python")

print("Hello, Python.\nI'm Thousand.")
"""

# 輸出格式 (format)
"""
guest = "Allie"
host = "Thousand"

print("Hello, " + guest + ". My name is " + host + ".")
print(f"Hello, {guest}. My name is {host}.")
print("Hello, {}. My name is {}.".format(guest, host))

pi = 3.14159265
print(f"Pi is {pi:.3f}")
print("Pi is {:.3f}".format(pi))
"""

# 資料型態不同導致運算結果不同
"""
a = "123"
b = "456"
c = 123
d = 456
print(a+b)
print(c+d)
"""

# 輸入
"""
number = input("")
print(f"Your number is {number}")
print(type(number)) # string
number = int(number)
print(type(number))
"""

# 輸入時候就轉型
"""
number = int(input("Enter a number: "))
print(f"Your number is {number}")
print(type(number))
"""

# try except
try:
    number = int(input("Enter a number: "))
    print(f"Your number is: {number}")
except ValueError:
    print("輸入格式錯誤，請輸入數字")