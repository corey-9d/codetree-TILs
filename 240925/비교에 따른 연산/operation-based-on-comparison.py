inp = input().split(" ")
a = int(inp[0])
b = int(inp[1])
c = (a * b)
d = (b // a)

if a > b:
    print(c)
else:
    print(d)