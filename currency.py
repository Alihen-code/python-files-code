# peso soles reais to usd converter
pesos = int(input('What do you have left in pesos?: '))
soles = int(input('What do you have left in soles?: '))
reais = int(input('What do you have left in reais?: '))
usd_from_pesos = pesos * 0.0539
usd_from_soles = soles * 0.2939
usd_from_reais = reais * 0.1764
total_usd = usd_from_pesos + usd_from_soles + usd_from_reais
print(round(total_usd, 1))