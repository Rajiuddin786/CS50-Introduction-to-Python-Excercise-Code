date = input('Date: ').strip()
fix = ' '
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

    for t in date:
        if t != ',':
            fix+=t

    a_1 = fix.split(' ')
    mon = month.index(a_1[0])
    print(f"{a_1[2]}-0{mon + 1}-0{a_1[1]}",end='')


except ValueError:
    a_2 = fix.split('/')
    print(f"{a_2[2]}-0{a_2[0]}-0{a_2[1]}",end='')