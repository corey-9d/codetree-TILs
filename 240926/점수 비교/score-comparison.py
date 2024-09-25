inp = input().split(" ")
a_math = int(inp[0])
a_eng = int(inp[1])

inp_1 = input().split(" ")
b_math = int(inp_1[0])
b_eng = int(inp_1[1])




if a_math > b_math and a_eng > b_eng:
    print(1)
else:
    print(0)