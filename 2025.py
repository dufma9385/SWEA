import sys
sys.stdin = open('2025_input.txt')

n = int(input())
a = 0
for i in range(1,n+1):
    a += i
print(a)
