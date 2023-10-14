import string


def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    e = ''
    y = 0
    my_list = []
    leng = len(s)
    if 1 < leng < 7:

        for i in s:
            if i == '1' or i == '2' or i == '3' or i == '4' or i == '5' or i == '6' or i == '7' or i == '8' or i == '9' or i == '0':
                a = int(i)
                my_list.append(a)
            else:
                my_list.append(i)
        for a in s:
            if a in string.punctuation:
                return False

        if type(my_list[0]) == str and type(my_list[1]) == str:
            for u in range(0, leng):
                if u != 0 and u != 1:
                    if type(my_list[u]) == int:
                        if my_list[u] == 0:
                            return False  # OK

                        else:
                            f = leng - u
                            for q in range(1, f+1):
                                if type(my_list[-q]) == int:
                                    y += 1
                                else:
                                    return False
                            if y == (leng - u):
                                return True
                            else:
                                return False

                    else:
                        e = e + my_list[u]
            if (my_list[0] + my_list[1] + e) == s:
                return True
    else:
        return False

if __name__=="__main__":
    main()