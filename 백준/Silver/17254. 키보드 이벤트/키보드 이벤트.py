import sys
input = lambda : sys.stdin.readline().rstrip()

N, M = map(int, input().split())
lst = [[] for _ in range(1000001)]
for _ in range(M):
    a,b,c = input().split()
    na, nb = int(a), int(b)
    lst[nb].append((na,c))

res = ''
for i in lst:
    if i:
        for trash, plus in sorted(i):
            res += plus

print(res)