a, b = map(int, input().split())
b = b - 45

if b < 0:
    a = a - 1
    if a < 0:
        a = a + 24
        print(a, b + 60)
    else:
        print(a, b + 60)
else:
    print(a, b)