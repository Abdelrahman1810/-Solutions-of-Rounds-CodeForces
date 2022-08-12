a=input()
print(sum(a.count(_)**2 for _ in set(a)))