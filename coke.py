def main():
    print('Due Amount: 50')
    rr1 = 50
    while True:
        input_amount = int(input('Insert Coin: '))
        rr = check(input_amount, rr1)
        if rr != 1:
            if rr > 0:
                print('Due Amount:', rr)
                rr1 = rr
            if rr <= 0:
                rr2 = rr*(-1)
                print('Changed Owned:', rr2)
                break
        else:
            print('Due Amount:', rr1)
            continue


def check(amo, r):
    if amo == 25 or amo == 20 or amo == 5:
        while True:
            o = r - amo
            return o
    else:
        return 1


main()