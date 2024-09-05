def factorial(n):
    if n <= 0:
        return 1
    total = 1
    for i in range(1, n + 1):
        total = total * i
    return total

def main():
    num = int(input("숫자를 입력하세요: "))

    print(factorial(num))

if __name__ == '__main__':
    main()