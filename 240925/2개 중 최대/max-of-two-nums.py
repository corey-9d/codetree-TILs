inp = input().split(" ")
a = int(inp[0])
b = int(inp[1])

max = a if a > b else b
print(max)