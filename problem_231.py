n = int(input())
matrix = []
for _ in range(n):
    row = list(map(int,input().split()))
    matrix.append(row)
val =0
for row in matrix:
    if sum(row) > 1:
        val = val + 1

print(val)
