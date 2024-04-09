def separador(lista):
    positivos = [num for num in lista if num >= 0]
    negativos = [num for num in lista if num < 0]

    print(f'Positivos: {positivos}')
    print(f'Negativos: {negativos}')

separador([1, -2, 3, -4, 5, -6])