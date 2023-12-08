import os
from datetime import datetime

# Crie uma lista de arquivos de texto, um para cada horário
arquivos = {
    "manha": "C:\\Users\\becke\\Desktop\\nomes_manha.txt",
    "tarde": "C:\\Users\\becke\\Desktop\\nomes_tarde.txt",
    "tarde_noite": "C:\\Users\\becke\\Desktop\\nomes_tarde_noite.txt",
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
    resposta = input(f"{nome}, você está presente? (S/N): ").strip().lower()

    while resposta not in ["s", "n"]:
        print("Resposta inválida. Por favor, responda com 'S' para PRESENTE ou 'N' para FALTA.")
        resposta = input(f"{nome}, você está presente? (S/N): ").strip().lower()

    if resposta == "s":
        presenca[nome] = "Presente"
    else:
        presenca[nome] = "Faltou"

# Filtra apenas os que faltaram
faltantes = {nome: status for nome, status in presenca.items() if status == "Faltou"}

# Exibe o registro de presença
print("\nRegistro de Presença:")
for nome, status in faltantes.items():
    print(f"{nome}: {status}")

# Salvar os resultados dos faltantes em um arquivo na pasta correspondente
pasta_resultado = os.path.join("resultados", periodo)
os.makedirs(pasta_resultado, exist_ok=True)
resultado_filename = os.path.join(pasta_resultado, f"faltantes_{periodo}.txt")
with open(resultado_filename, 'w') as resultado_file:
    for nome, status in faltantes.items():
        resultado_file.write(f"{nome}: {status}\n")

print(f"Faltantes salvos em {resultado_filename}")
