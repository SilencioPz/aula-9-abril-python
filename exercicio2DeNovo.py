#Biblioteca específica para esta função
import dateparser

def dataBemEscrita(data):
    data = dateparser.parse(data)

    if data is not None:
        dataBemEditada = data.strftime('%d/%m/%Y')
        print(f'A data formatada é: {dataBemEditada}')
    else:
        print('Não foi possível analisar a data.')

dataBemEscrita('4 de setembro de 2024')