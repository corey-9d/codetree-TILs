inp =input().split(" ")
a = int(inp[0])
b = int(inp[1])

if a > b:
    result = a - b
else:
    result = b - a

print(result)