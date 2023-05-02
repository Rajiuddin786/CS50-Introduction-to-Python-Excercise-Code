date = input('Date: ').strip()
fix = ''
q = ''
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
            fix += t
    a_1 = fix.split(' ')
    mon = month.index(a_1[0])
    if mon+1 < 10:
        o = '0' + str(mon+1)
    else:
        o = str(mon+1)
    if int(a_1[1]) < 10:
        q = '0' + a_1[1]
    else:
        q = a_1[1]
    print(f"{a_1[2]}-{o}-{q}", end='')


except ValueError:
    u = ''
    t = ''
    a_2 = date.split('/')
    if int(a_2[0]) < 10:
        t = '0' + a_2[0]
    else:
        t = a_2[0]
    if int(a_2[1]) < 10:
        u = '0' + a_2[1]
    else:
        u = a_2[1]
    print(f"{a_2[2]}-{t}-{u}", end='')