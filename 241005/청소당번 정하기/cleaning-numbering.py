#이런 유형은 긴 주기 부터

d = int(input())
cnt_c = 0
cnt_h = 0
cnt_t = 0


for i in range(1, d + 1):
    if i % 12 == 0:
        cnt_t += 1
    elif i % 3 == 0:
        cnt_h += 1
    elif i % 2 == 0:
        cnt_c += 1
print(cnt_c, cnt_h, cnt_t)