date = input('Date: ').strip()
try:
    month = [
        "January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December"]

    a_1 = date.split(' ')
    mon = month.index(a_1[0])
    print(f"{a_1[2]}-{mon + 1}-{a_1[1]}")


except ValueError:
    a_2 = date.split('/')
    print(f"{a_2[2]}-{a_2[1]}-{a_2[0]}",end='')