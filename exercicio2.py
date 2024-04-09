from datetime import datetime

def dataPorExtensaoBrasileira(dataPorExtenso):
    meses = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho', 'julho', 'agosto', 'setembro', 'outubro', 'novembro', 'dezembro']

    dataPorExtenso = datetime.strptime(dataPorExtenso, '%d/%m/%Y')

    diaMesAno = f'{dataPorExtenso.day} de {meses[dataPorExtenso.month - 1]} de {dataPorExtenso.year}'

    return diaMesAno

print(dataPorExtensaoBrasileira('9/4/2024'))