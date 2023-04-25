def main():
    w = 0
    g = []
    c = 0
    pos = 0
    try:
        while True:
            i = input().strip().upper()
            g = g + [i]
    except EOFError:
        a = len(g)
        for j in g:
            if j != ' ':
                for u in g:
                    if j == u:
                        c = c + 1
                        g[pos] = ' '
                    pos += 1

            if c != 0:
                print(f"{c} {j}")
            c = 0
            pos = 0
            for q in range(a):

                if g[q] == ' ':
                    w += 1
            if w != a:
                w = 0
            else:
                break


main()