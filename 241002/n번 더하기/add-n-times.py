inp = input().split(" ")
a = int(inp[0])
n = int(inp[1])
result = (a + n)

for _ in range(n):
    print(result)
    result += n