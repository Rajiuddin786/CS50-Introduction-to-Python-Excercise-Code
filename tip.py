def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = (dollars * percent)/100
    print(f"Leave ${tip:.2f}")


def dollars_to_float(d):
    d_t_f=""
    for i in d:
        if i != "$":
            d_t_f+=i
    return float(d_t_f)

def percent_to_float(p):
    p_t_f=""
    for i in p:
        if i != "%":
            p_t_f+=i
    return float(p_t_f)

main()