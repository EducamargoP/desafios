""""
🧠 Enunciado do Projeto: "Planner de Estudos com Sistema de Recompensas e Castigos"
Você deverá desenvolver um programa em Python com o objetivo de auxiliar estudantes na organização e disciplina dos seus estudos semanais.
O sistema funcionará como um planner interativo, onde o usuário poderá cadastrar:

As matérias que deseja estudar

Os horários dedicados para cada matéria

A distribuição dos estudos ao longo da semana

🎯 Funcionalidades obrigatórias:
Cadastro de planejamento semanal O usuário informa:

Quais matérias deseja estudar

Quantas horas por semana para cada matéria

Em quais dias e horários pretende estudar cada uma

Geração automática da planilha semanal O programa monta uma tabela com os dias da semana (segunda a domingo),
preenchendo os horários de estudo conforme o planejamento do usuário.

Registro de cumprimento diário Ao final de cada dia, o usuário informa se cumpriu ou não os estudos planejados.

Sistema de castigos e recompensas

Se o usuário não cumprir o estudo de um dia, o programa aplica um "castigo" (ex: aumentar o tempo de estudo no dia seguinte,
bloquear acesso a funcionalidades divertidas, ou sugerir tarefas extras).

Se o usuário cumprir consistentemente os estudos, o programa pode oferecer uma "recompensa" simbólica
(ex: mensagem motivacional, liberar tempo livre, ou mostrar estatísticas de progresso).

💡 Requisitos técnicos:
Utilizar estruturas como listas, dicionários e funções

Interface via terminal (modo texto)

Armazenamento dos dados em arquivos (opcional, para salvar progresso)

Sistema de validação para entrada de dados
"""
import random

print("📘 Planner de Estudos com Sistema de Recompensas e Castigos")

# Listas para armazenar dados do aluno
aluno_materia = []
aluno_semana = []

# Cadastro de matérias
quantidade = 0
materias = int(input('📚 Quantas matérias deseja estudar? '))
while materias > quantidade:
    curso = input('📝 Nome da matéria: ')
    quantidade += 1
    aluno_materia.append(curso)

# Dias da semana disponíveis
semana = ['Segunda-Feira', 'Terça-Feira', 'Quarta-Feira',
          'Quinta-Feira', 'Sexta-Feira', 'Sabado', 'Domingo']

print("\n📅 Lembrando que a semana tem 7 dias.")
dia = int(input("Quantos dias da semana deseja estudar? "))

# Cadastro dos dias de estudo
while len(aluno_semana) < dia:
    for dia_semana in semana:
        resposta = input(f'Deseja estudar {dia_semana}? [S/N]: ').lower()
        if resposta == 's' and dia_semana not in aluno_semana:
            aluno_semana.append(dia_semana)
        if len(aluno_semana) == dia:
            break

# Cadastro de horas disponíveis
print("\n⏱ Passe as horas em número inteiro. Exemplo: 4")
horario = int(input("Quantas horas tem disponível por dia? "))

# Cálculo de divisão de horas
divisao = horario / len(aluno_materia)
teoria = divisao / 2

# Exibição do planejamento
print("\n📊 Seu planejamento ficou assim:")
print(f"📚 Matérias escolhidas: {', '.join(aluno_materia)}")
print(f"🗓 Dias de estudo: {', '.join(aluno_semana)}")
print(f"⏱ Horas por dia: {horario}h")
print(f"📖 Cada matéria terá cerca de {divisao:.2f}h por dia, sendo {teoria:.2f}h de teoria e {teoria:.2f}h de prática.")

# Listas de castigos e elogios
castigos = [
    "Estudar 1 hora extra amanhã",
    "Fazer um resumo da matéria perdida",
    "Bloquear acesso ao celular por 2 horas",
    "Resolver 5 exercícios extras",
    "Assistir uma videoaula sem pular partes",
    "Revisar o conteúdo duas vezes amanhã"
]
elogios = [
    "Você mandou muito bem hoje!",
    "Continue assim, sua dedicação está brilhando!",
    "Orgulho define! 👏",
    "Você é mais capaz do que imagina.",
    "Seu esforço está valendo a pena!",
    "Parabéns pela sua evolução!",
    "Você está no caminho certo!",
    "Cada passo conta, e você está avançando!",
    "Sua persistência é inspiradora!",
    "Você é incrível, nunca duvide disso!",
    "Hoje foi um dia de vitória!",
    "Você merece reconhecimento!",
    "Seu trabalho está fazendo a diferença!",
    "Você está construindo algo grandioso!",
    "Acredite: você tem tudo para vencer!",
]

# Registro diário de cumprimento
print("\n🎯 Vamos registrar seu desempenho diário:")
for dia_estudo in aluno_semana:
    resposta = input(f"Você estudou em {dia_estudo}? [S/N]: ").lower()
    if resposta == 's':
        print("✅ Recompensa:")
        print(random.choice(elogios))
    else:
        print("⚠️ Castigo aplicado:")
        print(random.choice(castigos))












