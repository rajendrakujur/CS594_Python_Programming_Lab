with open("002_input.txt", "r") as m:
    a = [[int(num) for num in line.split(",")] for line in m]
m.close()
b = []
x = []
n = len(a)
c = len(a[0])
for i in range(n):
    b.append(a[i][c - 1])
    del a[i][c - 1]
for k in range(n - 1):
    for i in range(k + 1, n):
        if a[i][k] == 0:
            continue
        factor = a[k][k] / a[i][k]
        for j in range(k, n):
            a[i][j] = a[k][j] - a[i][j] * factor
        b[i] = b[k] - b[i] * factor
b[n - 1] = b[n - 1] / a[n - 1][n - 1]
for i in range(n - 2, -1, -1):
    sum_ax = 0
    for j in range(i + 1, n):
        sum_ax += a[i][j] * b[j]
    b[i] = (b[i] - sum_ax) / a[i][i]
with open("002_output.txt", "w") as f:
    for item in b:
        f.write("%s\n" % item)
f.close()
