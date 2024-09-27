a_inp = input().split(" ")
b_inp = input().split(" ")
c_inp = input().split(" ")

a_inp_st = str(a_inp[0])
b_inp_st = str(b_inp[0])
c_inp_st = str(c_inp[0])

a_inp_num = int(a_inp[1])
b_inp_num = int(b_inp[1])
c_inp_num = int(c_inp[1])

A_count = 0  # 

#첫번째
if a_inp_st == "Y" and a_inp_num >= 37:
    A_count += 1
    print(end="")
elif a_inp_st == "N" and a_inp_num >= 37:
    print(end="")
elif a_inp_st == "Y" and a_inp_num == 36:
    print(end="")
else:
    print(end="")


#두번째
if b_inp_st == "Y" and b_inp_num >= 37:
    A_count += 1
    print(end="")
elif b_inp_st == "N" and b_inp_num >= 37:
    print(end="")
elif b_inp_st == "Y" and b_inp_num == 36:
    print(end="")
else:
    print(end="")


#세번째
if c_inp_st == "Y" and c_inp_num >= 37:
    A_count += 1
    print(end="")
elif c_inp_st == "N" and c_inp_num >= 37:
    print(end="")
elif c_inp_st == "Y" and c_inp_num == 36:
    print(end="")
else:
    print(end="")


# A 분류 2명
    
if A_count >= 2:
    print("E")
else:
    print("N")