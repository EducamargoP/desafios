""""
Controle de estoque com alerta de reposição
🎯 Cenário:
Uma loja possui um sistema de controle de estoque. Cada produto tem:

Nome

Quantidade atual em estoque

Quantidade mínima necessária

A loja quer automatizar o processo de verificação para saber quais produtos precisam ser repostos.

✅ Objetivo:
Criar um programa que:

Receba uma lista de produtos com suas quantidades.

Verifique se a quantidade atual está abaixo da mínima.

Exiba um alerta para reposição dos produtos que estão com estoque baixo.
"""



produtos = []
minima = []
def controle_loja():

    while True:
        produto = input("PRODUTO: ")
        quantidade = int(input("QUANTIDADE: "))
        minima_estoque = int(input('MINIMO DE ESTOQUE:'))
        valor = float(input("VALOR R$: "))
        lista = dict(produto= produto, quantidade = quantidade, valor= valor, minima_estoque = minima_estoque)
        produtos.append(lista)


        deseja = input("DESEJA CADASTRAR [S/N]: ").lower()
        if deseja == 'n':
            break

        if quantidade <= minima_estoque:
            minima.append(produto)

controle_loja()
print(produtos)
print(f'{minima} QUANTIDADE ATUAL ESTÁ ABAIXO DA MÍNIMA!')
