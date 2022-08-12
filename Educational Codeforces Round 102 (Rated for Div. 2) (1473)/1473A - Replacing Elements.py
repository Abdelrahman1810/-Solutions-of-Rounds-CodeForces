for _ in range(int(input())):
    n, d = map(int, input().split())
    a=sorted(map(int, input().split()))
    if a[-1]<=d or a[0]+a[1]<=d :
        print("YES")
    else:
        print("NO")