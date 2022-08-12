t=int(input())
s=""; A=0; G=0
for _ in range(t):
    a,g=map(int, input().split())
    if A+a-G>500:
        s+="G"
        G+=g
    else:
        s+="A"
        A+=a
print(s)
