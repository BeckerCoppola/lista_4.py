import os
from datetime import datetime

# Crie uma lista de arquivos de texto, um para cada horário
arquivos = {
    "manha": "nomes.txt",
    "tarde": "nomes1.txt",
    "noite": "nomes2.txt"
}

# Determine o horário atual
agora = datetime.now()
hora = agora.hour

# Escolha o arquivo com base na hora atual
if 6 <= hora < 12:
    periodo = "manha"
elif 12 <= hora < 18:
    periodo = "tarde"
else:
    periodo = "noite"

# Cria um dicionário para armazenar a presença de cada pessoa
presenca = {}

# Tenta ler os nomes a partir do arquivo
arquivo_nome = arquivos.get(periodo)
if arquivo_nome:
    try:
        with open(arquivo_nome, 'r') as arquivo:
            nomes = [linha.strip() for linha in arquivo]
    except FileNotFoundError:
        print(f"O arquivo '{arquivo_nome}' não foi encontrado.")
        nomes = []
else:
    print(f"Horário não reconhecido para escolha do arquivo.")

# Faz a chamada
for nome in nomes:
    resposta = input(f"{nome}, você está presente? (S/N): ").strip().upper()
    while resposta not in ["S" , "N"]:
        print('Reposta inválida. Por favor, responda S para PRESENTE ou N para AUSENTE')
        resposta = input(f'{nome} voce esta presente? (S/N): ').strip().upper()

    if resposta == "s":
        presenca[nome] = "Presente"
    else:
        presenca[nome] = "Faltou"

# Exibe o registro de presença
print("\nRegistro de Presença:")
for nome, status in presenca.items():
    print(f"{nome}: {status}")
