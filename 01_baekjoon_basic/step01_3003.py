#k, q, l, b, n, p = map(int, input().split())
#print(1-k, 1-q, 2-l, 2-b, 2-n, 8-p)

[print(y-x) for x, y in zip(list(map(int, input().split())), [1, 1, 2, 2, 2, 8])]
