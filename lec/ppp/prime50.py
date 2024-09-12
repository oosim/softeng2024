from ppp.prime import is_prime


def main():
    primes = []
    for i in range(2, 50):
        if is prime(i):
            primes.append(i)
    print(primes)

    print([i for i in range(2, 51) if is_prime()])

if __name__ == '__main__':
    main()