import sys
sys.stdin = open('2050_input.txt')
a = input()
for i in range(len(a)):
    print(ord(a[i])-64, end=' ')
