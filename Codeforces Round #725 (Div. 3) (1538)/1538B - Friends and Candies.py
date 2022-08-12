for _ in range(int(input())):
    n=int(input())
    a=sorted(map(int, input().split()))
    b=sum(a)
    if b%n: print(-1)   
    else:
        b/=n
        ans=0
        for __ in range(n):
            if a[__]>b:
                ans+=1
        print(ans)