n, k, t = map(int, input().split())
t=t/100
a=int(t*n)
for _ in range (a):
    print(k, end=" ")
if a!=n:
    print(int((t*n-a)*k), end=" ")
for _ in range (n-a-1):
    print(0, end=" ")
