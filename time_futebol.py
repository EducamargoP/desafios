""""
 Enunciado do Desafio: Escalando o Time dos Sonhos
Você foi contratado como programador oficial de um clube de futebol fictício! Sua missão é criar um sistema em Python que cadastre os jogadores do time em um dicionário, contendo as seguintes informações:

nome: Nome completo do jogador

numero: Número da camisa

posicao: Posição em campo (ex: Goleiro, Zagueiro, Meio-campo, Atacante)

Além disso, para deixar o código mais robusto:

Crie jogadores loop infinito.

Armazene esses jogadores em uma lista de dicionários.

Novas funcionalidades que vamos implementar:
Perguntar ao técnico quantos jogadores deseja de cada posição.

Criar uma estrutura de controle para não ultrapassar esses limites.

Continuar usando a lista de dicionários para armazenar os jogadores.
"""

# Lista que armazena todos os jogadores
time = []

# Posições válidas
posicoes_validas = ["goleiro", "zagueiro", "meio", "atacante"]

# Números de camisa já usados
numeros_usados = []

def jogador():
    # Técnico define os limites por posição
    limite = {
        "goleiro": int(input("QUANTOS GOLEIROS DESEJA PARA O ELENCO: ")),
        "zagueiro": int(input("QUANTOS ZAGUEIROS DESEJA PARA O ELENCO: ")),
        "meio": int(input("QUANTOS MEIO-CAMPO DESEJA PARA O ELENCO: ")),
        "atacante": int(input("QUANTOS ATACANTES DESEJA PARA O ELENCO: "))
    }

    # Dicionário para armazenar os nomes por posição
    posicoes = {
        "goleiro": [],
        "zagueiro": [],
        "meio": [],
        "atacante": []
    }

    while True:
        # Verifica se todas as posições estão completas
        if all(len(posicoes[p]) >= limite[p] for p in posicoes_validas):
            print("\n✅ TODAS AS POSIÇÕES FORAM PREENCHIDAS. CADASTRO ENCERRADO.")
            break

        nome = input("\nNOME DO JOGADOR: ")

        # Escolha da posição com verificação de validade e limite
        while True:
            print("Posições disponíveis: goleiro, zagueiro, meio, atacante")
            posicao = input("POSIÇÃO: ").lower()
            if posicao not in posicoes_validas:
                print("❌ POSIÇÃO INVÁLIDA. TENTE NOVAMENTE!")
            elif len(posicoes[posicao]) >= limite[posicao]:
                print(f"⚠️ LIMITE DE {posicao.upper()}S ATINGIDO!")
            else:
                break

        # Escolha do número da camisa com verificação de duplicidade
        while True:
            numero = int(input("NÚMERO DA CAMISA: "))
            if numero in numeros_usados:
                print("❌ ESSE NÚMERO JÁ ESTÁ EM USO. TENTE OUTRO.")
            else:
                numeros_usados.append(numero)
                break

        # Cadastro do jogador
        contrato = {'Nome': nome, 'Posição': posicao, 'Número': numero}
        time.append(contrato)
        posicoes[posicao].append(nome)

        continuar = input("DESEJA ADICIONAR MAIS JOGADORES? [S/N]: ")
        if continuar.lower() == 'n':
            break

    # Exibe os jogadores por posição
    print("\n📋 ELENCO FINAL POR POSIÇÃO:")
    for p in posicoes_validas:
        print(f"- {p.upper()}: {posicoes[p]}")

# Executa o programa
jogador()

