# Algoritmo de distribuição/ciclo do Pica-Pau e do lobo

# Suponha que temos uma lista de itens a serem distribuídos
itens = ["maçã", "banana", "laranja", "pera", "uva", "mamão", "abacaxi", "melancia"]

# Suponha que temos duas variáveis para armazenar os itens de cada um
pica_pau = []
lobo = []

# Inicialize um contador para controlar o ciclo
contador = 0

# Enquanto houver itens na lista, faça o ciclo
while itens:
  # Se o contador for par, é a vez do Pica-Pau
  if contador % 2 == 0:
    # O Pica-Pau pega um item para ele
    pica_pau.append(itens.pop(0))
    # E dá um item para o lobo
    lobo.append(itens.pop(0))
  # Se o contador for ímpar, é a vez do lobo
  else:
    # O lobo pega dois itens para ele
    lobo.append(itens.pop(0))
    lobo.append(itens.pop(0))
    # Mas só dá um item para o Pica-Pau
    pica_pau.append(lobo.pop())
  # Incremente o contador
  contador += 1

# Mostre os itens de cada um
print("Pica-Pau:", pica_pau)
print("Lobo:", lobo)