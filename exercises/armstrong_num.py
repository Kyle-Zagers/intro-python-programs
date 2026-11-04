a, b = input().split()
a = int(a)
b = int(b)
armstrong_output = 0

for i in range(a, b):
    armstrong_output = 0
    j = i
    while j > 0:
        armstrong_output += (j % 10) ** len(str(i))
        j //= 10
    if armstrong_output == i:
        print(armstrong_output)
