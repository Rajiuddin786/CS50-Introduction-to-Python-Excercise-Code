def main():
    print('Due Amount: 50')
    rr1 = 50
    while True:
        input_amount = int(input('Insert Coin: '))
        rr = check(input_amount, rr1)
        if rr != 1:
            if rr > 0:
                print('Amount Due:', rr)
                rr1 = rr
            if rr <= 0:
                rr2 = rr*(-1)
                print('Change Owed:', rr2)
                break
        else:
            print('Amount Due:', rr1)
            continue


def check(amo, r):
    if amo == 25 or amo == 20 or amo == 5 or amo == 10:
        while True:
            o = r - amo
            return o
    else:
        return 1


main()