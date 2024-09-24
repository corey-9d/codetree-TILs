inp = input().split(" ")
h = int(inp[0])
w = int(inp[1])
b = ((10000 * w) // (h * h))

if b > 25:
    print(b) 
    print("Obesity")
else:
    print(b)