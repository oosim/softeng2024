from ppp.hol_jjak import is_even

def main():
    total = 0

    #total = [i for i in range(1, 101) if is_even(i)]

    for i in range(1, 101):
        if is_even(i):
            total += i
    print(f"1부터 100까지 짝수 합은 {total}")

if __name__ == '__main__':
    main()