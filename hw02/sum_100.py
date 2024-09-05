from hw02.hol_jjak import is_even

def main():
    total = 0

    # total = sum([i for i in range(1, 101) if is_even(i)])

    for i in range(1, 101):
        if is_even(i):
            total += i
    print(f"1에서 100까지의 짝수 총합은 {total}입니다.")

if __name__ == '__main__':
    main()