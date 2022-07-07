# 算術運算子
"""
x = 5
y = 3
print(x+y)
print(x-y)
print(x*y)
print(x/y)
print(x//y) # 取整數除法
print(x**y) # 5^3 = 125
print(25**(1/2))
print(x%y) # mod
"""

# 餘數應用
"""
n = int(input())
print(f"百位數字: {n//100}")
print(f"十位數字: {(n//10)%10}")
print(f"個位數字: {n%10}")
"""

# 交換數值
"""
x = int(input("x: ")) # x: 10
y = int(input("y: ")) # y: 8


temp = x  # temporary
x = y
y = temp

x, y = y, x

print(f"x: {x}")
print(f"y: {y}")
"""

# 控制流程
"""
num = int(input())
if num > 200:
    print(f"{num} > 200")
else:
    print(f"{num} <= 200")
"""

# if/else，非 0 => True， 0 => False
"""
if 3:
    print("This is True.")
else:
    print("This is False")
"""

# if/elif/else
"""
num = int(input())
if num > 200:
    print(f"{num} > 200")
elif 200 >= num >= 100:
    print(f"100 <= {num} <= 200")
else:
    print(f"{num} < 100")
"""

# 最大值練習
"""
x = int(input())
y = int(input())
z = int(input())

if x > y:
    ans = x
else:
    ans = y

if z > ans:
    ans = z

print(ans)
"""

# while 迴圈
i = 0
while i < 10:
    if i % 2 == 0:
        print(i)
    i = i + 1






