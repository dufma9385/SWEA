import sys
sys.stdin = open('1936_input.txt')

a, b = map(int, input().split())
winner=''
if a==1:
    if b==2:
        winner = 'b'
    else:
        winner = 'a'
elif a==2:
    if b==1:
        winner='a'
    else:
        winner='b'
else:
    if b==1:
        winner='b'
    else:
        winner='a'
print(winner)
