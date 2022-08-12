i=lambda:map(int,input().split())
n,k=i();l=list(i())
a=0
for _ in range (n):
    if l[_]>=l[k-1] and l[_]>0:
        a+=1
print(a)