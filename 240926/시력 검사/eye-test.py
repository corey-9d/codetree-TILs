r_eyes = float(input())
l_eyes = float(input())

if r_eyes and l_eyes >= 1.0:
    print("High")
elif r_eyes and l_eyes >= 0.5:
    print("Middle")
else:
    print("Low")