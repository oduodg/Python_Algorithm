import sys
input = sys.stdin.readline
n = int(input()) # nę°ė ė ė
arr = list(map(int, input().split()))
for num in sorted(set(arr)):
    print(num, end=" ")