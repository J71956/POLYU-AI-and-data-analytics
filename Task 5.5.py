n = int(input("Enter no of primes"))
x = 2
while n >0:
    for i in range(2, x - 1):
        if x % i == 0:
            x = x + 1
    else:
        print(x)
        x = x + 1
        n = n - 1

