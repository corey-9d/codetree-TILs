n = int(input())
n_month_31 = [1, 3, 5, 7, 8, 10, 12]

year = 2023



if year % 4 != 0:
    if year % 100 != 0:
        if year % 400 != 0:
            if n in n_month_31:
                print(31)
            elif n == 2:
                print(28)
            else:
                print(30)