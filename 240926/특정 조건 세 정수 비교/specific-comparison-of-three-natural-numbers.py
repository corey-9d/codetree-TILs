inp = input().split(" ")
a = int(inp[0])
b = int(inp[1])
c = int(inp[2])


if a <= b and a <= c:
    print(1, end=" ")
else:
    print(0, end=" ")

if a == b == c:
    print(1)
else:
    print(0)