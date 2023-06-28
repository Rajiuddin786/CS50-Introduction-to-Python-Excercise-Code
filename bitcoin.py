import json
import sys
import requests

def price_calculator(price):
    a,b = price.split(',')
    a = int(a)
    x,y = b.split('.')
    x = int(x)
    y = int(y)
    x1 = x
    y1 = y
    count = 0
    count1 = 0
    while int(x1) != 0:
        count+=1
        x1=x1/10
    while int(y1) != 0:
        count1+=1
        y1/=10

    multiple = 1
    divider = 1
    for i in range(count):
        multiple*=10
    a1 = a*multiple
    for i in range(count1):
        divider*=10
    deci = y/divider
    price_in_float = a1+x+deci
    return price_in_float

def main():
    try:
        if len(sys.argv) != 2:
            sys.exit("Give Input")

        n = float(sys.argv[1])
        price_api = requests.get("https://api.coindesk.com/v1/bpi/currentprice.json")
        p = price_api.json()
        price  = p["bpi"]["USD"]["rate"]
        price_in_calculatable_form = price_calculator(price)
        bitcoin_price = n*price_in_calculatable_form
        print(f"${bitcoin_price:,.4f}")
    except ValueError:
        sys.exit("Invalid Input")

if __name__ == "__main__":
    main()