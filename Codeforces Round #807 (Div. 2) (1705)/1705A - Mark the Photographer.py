for _ in range(int(input())):
    n,x=map(int, input().split()); f=1
    a=sorted(map(int, input().split()))
    for i in range (n): 
        if a[i+n]-a[i]<x: f=0
    if f: print("YES")
    else: print("NO")