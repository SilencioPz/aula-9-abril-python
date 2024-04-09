def divisores(primeiro):
    print(f'Os divisores de {primeiro} são:')
    for segundo in range(1, primeiro + 1):
        if primeiro % segundo == 0:
            print(segundo)

divisores(8)