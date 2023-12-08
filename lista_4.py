import os
from datetime import datetime

# Crie uma lista de arquivos de texto, um para cada horário
arquivos = {
    "manha": "C:\\Users\\becke\\Desktop\\nomes_manha.txt",
    "tarde": "C:\\Users\\becke\\Desktop\\nomes_tarde.txt",
    "tarde_noite": "C:\\Users\\becke\\Desktop\\nomes_noite.txt",
    "noite": "C:\\Users\\becke\\Desktop\\nomes_noite.txt"
}

# Determine o horário atual
agora = datetime.now()
hora = agora.hour

# Escolha o arquivo com base na hora atual
if 6 <= hora < 12:
    periodo = "manha"
elif 12 <= hora < 17:  # Considerando "tarde" até 17 horas
    periodo = "tarde"
elif 17 <= hora < 21:  # Considerando "tarde_noite" até 21 horas
    periodo = "tarde_noite"
else:
    periodo = "noite"

# Cria um dicionário para armazenar a presença de cada pessoa
presenca = {}
faltas_contador = {}

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

# Inicializa o contador de faltas para cada pessoa
for nome in nomes:
    faltas_contador[nome] = 0

# Faz a chamada
for nome in nomes:
    resposta = input(f"{nome}, está presente? (S/N): ").strip().lower()

    while resposta not in ["s", "n"]:
        print("Resposta inválida!! Responda com 'S' para SIM PRESENTE ou 'N' Não para AUSENTE.")
        resposta = input(f"{nome}, você está presente? (S/N): ").strip().lower()

    if resposta == "s":
        presenca[nome] = "Presente"
    else:
        presenca[nome] = "Faltou"
        faltas_contador[nome] += 1

        # Exibir aviso após quatro faltas

    for nome, faltas in faltas_contador.items():
        if faltas > 4:
            print(f"{nome} ultrapassou o limite de faltas permitido. Ação adicional pode ser necessária.")

# Exibe o registro de presença para todos
print("\nRegistro de Presença:")
for nome, status in presenca.items():
    print(f"{nome}: {status}")

# Salvar os resultados em um arquivo para todos na pasta correspondente
pasta_resultado = os.path.join("resultados", periodo)
os.makedirs(pasta_resultado, exist_ok=True)
todos_filename = os.path.join(pasta_resultado, f"todos_{periodo}.txt")
with open(todos_filename, 'w') as todos_file:
    for nome, status in presenca.items():
        todos_file.write(f"{nome}: {status}\n")

print(f"Todos salvos em {todos_filename}")

# Filtra apenas os que faltaram
faltantes = {nome: status for nome, status in presenca.items() if status == "Faltou"}

# Exibe o registro de faltantes
print("\nRegistro de Faltantes:")
for nome, status in faltantes.items():
    print(f"{nome}: {status}")

# Salvar os resultados dos faltantes em um arquivo na pasta correspondente
faltantes_filename = os.path.join(pasta_resultado, f"faltantes_{periodo}.txt")
with open(faltantes_filename, 'w') as resultado_file:
    for nome, status in faltantes.items():
        resultado_file.write(f"{nome}: {status}\n")

print(f"Faltantes salvos em {faltantes_filename}")


# Exibe o registro de faltantes
print("\nRegistro de Faltantes:")
for nome, status in faltantes.items():
    print(f"{nome}: {status}")

# Obtenha o caminho para a área de trabalho
desktop_path = os.path.join(os.path.expanduser("~"), "Desktop")

# Crie o caminho completo para o arquivo de faltantes
faltantes_filename = os.path.join(desktop_path, f"faltantes_{periodo}.txt")

# Salve os resultados dos faltantes no arquivo
with open(faltantes_filename, 'w') as resultado_file:
    for nome, status in faltantes.items():
        resultado_file.write(f"{nome}: {status}\n")

# Salvar os resultados dos faltantes em um arquivo na pasta correspondente
#faltantes_filename = os.path.join(pasta_resultado, f"faltantes_{periodo}.txt")
#with open(faltantes_filename, 'w') as resultado_file:
#    for nome, status in faltantes.items():
#        resultado_file.write(f"{nome}: {status}\n")

print(f"Faltantes salvos em {faltantes_filename}")

# Verifica se algum nome tem mais de 4 faltas
nomes_com_mais_de_quatro_faltas = [nome for nome, faltas in faltas_contador.items() if faltas > 4]

# Salvar os nomes com mais de 4 faltas em um arquivo
if nomes_com_mais_de_quatro_faltas:
    filename_mais_quatro_faltas = os.path.join(pasta_resultado, f"mais_quatro_faltas_{periodo}.txt")
    with open(filename_mais_quatro_faltas, 'w') as mais_quatro_faltas_file:
        for nome in nomes_com_mais_de_quatro_faltas:
            mais_quatro_faltas_file.write(f"{nome}\n")

    print(f"Nomes com mais de 4 faltas salvos em {filename_mais_quatro_faltas}")
else:
    print("Nenhum nome ultrapassou o limite de 4 faltas.")
