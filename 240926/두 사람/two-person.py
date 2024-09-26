A_inp = input().split(" ")
B_inp = input().split(" ")

A_old = int(A_inp[0])
A_gen = A_inp[1]

B_old = int(B_inp[0])
B_gen = B_inp[1]

if (A_old >= 19 and A_gen == "M") or (B_old >= 19 and B_gen == "M"):
    print(1)
else:
    print(0)