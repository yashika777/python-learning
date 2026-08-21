def table(i,j):
    for m in range(i,j):
        for l in range(1,11):
            print(f'{m}*{l}',m*l)
        print()
table(1,5)
