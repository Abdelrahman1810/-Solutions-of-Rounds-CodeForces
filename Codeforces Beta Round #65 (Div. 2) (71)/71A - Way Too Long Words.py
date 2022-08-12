for i in [0]*int(input()):
    s=input()
    n=len(s)
    if n>10:
        l=str(n-2)
        print(s[0]+l+s[n-1])
    else:
        print(s)