def prime_checker(number):
    check_prime = True
    for prime in range(2, number):
        if (number % prime) == 0:
            check_prime = False
    if check_prime:
        print("It's a prime number.")
    else:
        print("It's not a prime number.")


n = int(input("Check this number: "))
prime_checker(n)