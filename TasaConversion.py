def exchange_money(budget, exchange_rate):
    resultado = budget * exchange_rate
    return resultado

#Corea: 300 USD a Wones
print(exchange_money(300, 1428.46))

#México: 500 USD a pesos MX
print(exchange_money(500, 19.61))

#Francia: 400 USD a euros
print(exchange_money(400, 0.88))

#Colombia: 250 USD -> pesos colombianos
print(exchange_money(250, 4295.25))
