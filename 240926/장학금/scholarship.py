inp = input().split(" ")
m_score = int(inp[0])
l_score = int(inp[1])

if 90 <= m_score and 95 <= l_score <= 100:
    print(100000)
elif 90 <= m_score and 90 <= l_score:
    print(50000)
else:
    print(0)