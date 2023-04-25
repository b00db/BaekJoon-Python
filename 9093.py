import sys

input = sys.stdin.readline
t = int(input())

s = [list(input().split()) for i in range(t)]
for i in range(t):
    for j in s[i]:
        print(''.join(reversed(list(j))), end=" ")
    print()