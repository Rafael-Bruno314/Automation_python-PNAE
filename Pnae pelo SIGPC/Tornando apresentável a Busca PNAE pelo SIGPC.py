# Adicionar nesta variável os dados brutos extraídos pelo Selenium
listao = ""

cidade = []
valor = []
centavos = []
porcentagem = []
ano_vigente = []

recorte = listao.split(',')

total = len(recorte)
giro = 0

for i in recorte:
    if giro % 5 == 0:
        cidade.append(i)

    if giro % 5 == 1:
        valor.append(i)

    if giro % 5 == 2:
        centavos.append(i)

    if giro % 5 == 3:
        porcentagem.append(i)

    if giro % 5 == 4:
        ano_vigente.append(i)

    giro += 1

#print(cidade)

"""
for i in cidade:
    print(i)

for i in valor:
    print(i)

for i in centavos:
    print(i)

for i in porcentagem:
    print(i)
"""

"""Refinando os valores"""
giro = 0
valor_puro = []

# print(valor[giro].split(':')[1])
for i in valor:
    valor_puro.append(valor[giro].split(':')[1])
    giro += 1

# print(valor_puro)
""""""

"""Juntando com os centavos"""

# print(centavos)

valor_completo = [0]    # Por algum motivo, não consegui criar essa lista vazia então ela tem um termo inicial 0, portanto não esquecer de retirá-lo quando colocar o resultado no excel.
giro = 0

for i in centavos:
    valor_completo.append(valor_puro[giro] + ',' + centavos[giro])
    giro += 1

#print(valor_completo)

""""""

"""Refinando a porcentagem"""
giro = 0
porcentagem_pura = []

for i in valor:
    porcentagem_pura.append(porcentagem[giro].split(':')[1])
    giro += 1

#print(porcentagem_pura)

"""Isolando o ano vigente"""

giro = 0
ano_vigente_puro = []

for i in ano_vigente:
    ano_vigente_puro.append(ano_vigente[giro][-4::])
    giro += 1

#print(ano_vigente_puro)

"""Imprimindo todos os valores para serem copiados para o excel"""

print("Cidades:")
for i in cidade:
    print(i)

print("="*60)

print("Valores:")
for i in valor_completo:
    print(i)

print("="*60)

print("Porcentagens:")
for i in porcentagem_pura:
    print(i)

print("="*60)

print("Ano vigente:")
for i in ano_vigente_puro:
    print(i)
