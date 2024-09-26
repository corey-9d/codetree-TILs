inp = input().split(" ")
a = int(inp[0])
b = int(inp[1])
c = int(inp[2])

if a <= b:
    if b <= c:
        print(c)
    elif a <= c:
        print(c)
    else:
        print(b)
elif a <= c:
    print(c)
else:
    print(a)