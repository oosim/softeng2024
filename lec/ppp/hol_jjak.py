def is_even(n):
    return n % 2 == 0

def main():
    n = int(input("정수 입력 : "))

    if is_even(n):
        print(f"{n} -> 짝수")
    else:
        print(f"{n} -> 홀수")


if __name__ == '__main__':
    main()