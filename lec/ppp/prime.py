def is_prime(n: int) -> bool:
    if n < 2:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False

    return True

def main():
    n = 7

    if is_prime(n):
        print(f'{n} -> 소수')
    else:
        print(f'{n} -> 소수 아님')
