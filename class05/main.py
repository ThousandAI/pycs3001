# Nested list
"""
numbers = [[3, 5], [7, 10], [12, 15]]
print(numbers)
print(numbers[0])
print(numbers[0][0])
print(numbers[0][1])
"""

# Nested Loop
"""
for i in range(3):
    print(f"{i}:",end=" ")
    for j in range(2):
        print(j,end=" ")
    print() 
"""
"""
for i in range(5):
    for j in range(3):
        print("*", end=" ")
    print()
"""
"""
n = int(input())
for i in range(n):
    for j in range(i+1):
        print("*",end="")
    print()
"""
"""
n = int(input())
for i in range(n):
    for j in range(n-i):
        print("*",end="")
    print()
"""
"""
n = int(input())
for i in range(n):
    for k in range(n-i-1):
        print(" ",end="")
    for j in range(i+1):
        print("*",end="")
    print()
"""
"""
matrix = [[32, 57, 89],
          [59, 20, 66],
          [66, 78, 82],
          [32, 89, 100],
          [70, 100, 30]]  # 5x3
row = len(matrix)
col = len(matrix[0])

for i in range(row):
    for j in range(col):
        print(matrix[i][j],end=" ")
    print()
"""
"""
matrix = [[32, 57, 89],
          [59, 20, 66],
          [66, 78, 82],
          [32, 89, 100],
          [70, 100, 30]]  # 5x3
row = len(matrix)
col = len(matrix[0])
row_sum = [0 for i in range(row)] # [178, 145, 226, 221, 200]
col_sum = [0 for j in range(col)] # [259, 344, 367]

for i in range(row):  # i = 1, j = 0
    for j in range(col):
        row_sum[i] = row_sum[i] + matrix[i][j]
        col_sum[j] = col_sum[j] + matrix[i][j]
print(row_sum)
print(col_sum)
"""
"""
def f(x):
    return x + 3
print(f(3))

print((lambda x: x + 3)(3))
"""
"""
numbers = [3, 50, 2, 80, 49, 10, 6]
print(list(filter(lambda x: x > 10, numbers)))
"""
"""
ans = []
for v in numbers:
    if v > 10:
        ans.append(v)
"""

scores = input().split() # ["3", "50", "100", "80", "90", "60"]
print(list(map(lambda x: int(x) * 0.8 + 20, scores)))

# ans = []
# for v in scores:
#     ans.append(int(v))