def somarimposto(valor,taxa):
    valor_final = valor +(valor*(taxa/100))
    return valor_final
valor =float(input("digite o valor "))
taxa = float(input("digite  a taxa"))
print(somarimposto(valor,taxa))
