N = int(input())
numbers = []

for _ in range(N):
    numbers.append(int(input()))

for num in numbers:
    if num % 2 == 1 and num % 3 == 0:
        print(num)