""""
Problema real: cálculo de comissão de vendedores
Cenário: Uma empresa de e-commerce possui vários vendedores que recebem comissão sobre as vendas realizadas.
A comissão varia de acordo com o valor total vendido no mês:

Até R$ 5.000 → 5% de comissão

De R$ 5.001 a R$ 10.000 → 7% de comissão

Acima de R$ 10.000 → 10% de comissão

A empresa quer automatizar esse cálculo usando Python.
"""


def calculo_comissao():

        if venda <= 5000:
            comissao = venda * 0.05

        elif venda <= 10000:
            comissao = venda * 0.07
        elif venda > 10000:
            comissao = venda * 0.10

        return f"Vendedor {nome} teve uma venda de R$ {venda:.2f} com comissão de R$ {comissao:.2f}"



nome = input("NOME:")
venda = float(input('VENDA:'))
print(calculo_comissao())