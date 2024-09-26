inp_A = input().split(" ")
inp_B = input().split(" ")

A_math = int(inp_A[0])
A_eng = int(inp_A[1])

B_math = int(inp_B[0])
B_eng = int(inp_B[1])

if A_math > B_math:
    print("A")
elif B_math > A_math:
    print("B")
else:
    if A_eng > B_eng:
        print("A")
    elif B_eng > A_eng:
        print("B")