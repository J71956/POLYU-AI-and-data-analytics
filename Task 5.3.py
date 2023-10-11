n = int(input("input a number"))
for i in range(2, int(n/2) + 1):
    if n % i == 0:
        print("is not a prime number")
        break
    else:
        print("is prime")
        break
