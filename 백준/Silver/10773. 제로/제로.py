import sys
input = sys.stdin.readline

K = int(input())

lst = []
for i in range(K):
    num = int(input())
    if num == 0:
        lst.pop()
    else:
        lst.append(num)

sum_ = 0
for i in lst:
    sum_ += i

print(sum_)