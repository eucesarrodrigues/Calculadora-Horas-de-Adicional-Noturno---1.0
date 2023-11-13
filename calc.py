from datetime import datetime, timedelta

def calcular_horas_extras():
    # Solicitando informações ao usuário
    hora_entrada = input("Informe a hora de entrada (formato HH:MM): ")
    hora_saida = input("Informe a hora de saída (formato HH:MM): ")
    carga_horaria_diaria = int(input("Informe a carga horária diária (em horas): "))
    carga_horaria_mensal = int(input("Informe a carga horária mensal (total de horas trabalhadas no mês): "))
    valor_hora = float(input("Informe o valor da hora de trabalho: "))
    percentual_hora_extra = float(input("Informe o percentual da hora extra (mínimo 50%, domingos e feriados 100%): "))
    duracao_hora = input("Informe a duração de uma hora (52:30 ou 60): ")

    # Convertendo a duração da hora para timedelta
    duracao_hora = timedelta(minutes=52, seconds=30) if duracao_hora == "52:30" else timedelta(hours=1)

    # Calculando salário bruto com base na carga horária mensal
    salario_bruto = carga_horaria_mensal * valor_hora

    # Definindo a hora de início e fim do expediente noturno (22:00 às 05:00)
    hora_inicio_noturno = 22
    hora_fim_noturno = 5

    # Convertendo as strings de hora para objetos datetime
    formato_hora = "%H:%M"
    entrada = datetime.strptime(hora_entrada, formato_hora)

    # Corrigindo a hora de saída para o próximo dia, se for antes da hora de entrada
    if entrada.hour > hora_inicio_noturno:
        saida = datetime.strptime(hora_saida, formato_hora)
    else:
        saida = datetime.strptime(hora_saida, formato_hora) + timedelta(days=1)

    # Calculando carga horária diária
    carga_horaria_real = (saida - entrada).seconds / 3600

    # Calculando horas extras com base na carga horária diária
    horas_extras_diarias = max(carga_horaria_real - carga_horaria_diaria, 0)

    # Calculando o adicional noturno
    adicional_noturno = 0
    hora_atual = entrada
    while hora_atual < saida:
        if hora_inicio_noturno <= hora_atual.hour <= 23 or 0 <= hora_atual.hour <= hora_fim_noturno - 1:
            adicional_noturno += 1
        hora_atual += duracao_hora

    # Convertendo as horas de adicional noturno para o formato HH:MM
    horas_formatadas = "{:02}:{:02}".format(*divmod(adicional_noturno * duracao_hora.seconds // 60, 60))

    # Calculando o valor do adicional noturno
    valor_adicional_noturno = adicional_noturno * (valor_hora / (duracao_hora.seconds / 3600)) * 0.2  # 20% de adicional noturno

    # Calculando as horas extras
    valor_hora_extra = valor_hora * (percentual_hora_extra / 100)
    valor_horas_extras = valor_hora_extra * horas_extras_diarias

    # Exibindo os resultados
    print("\nTabela de Informações:")
    print(f"Salário bruto: R$ {salario_bruto:.2f}")
    print(f"Carga horária diária: {carga_horaria_real:.2f} horas")
    print(f"Horas extras diárias: {horas_extras_diarias:.2f} horas")
    print(f"Salário-hora: R$ {valor_hora:.2f}")
    print(f"Porcentagem das horas extras: {percentual_hora_extra}%")
    print(f"Valor total das horas extras: R$ {valor_horas_extras:.2f}")

    # Exibindo os resultados da calculadora de adicional noturno
    print("\nResultado da Calculadora de Adicional Noturno:")
    print(f"Horas de adicional noturno: {horas_formatadas}")
    print(f"Valor do adicional noturno: R$ {valor_adicional_noturno:.2f}")

# Chamando a função para calcular horas extras e adicional noturno
calcular_horas_extras()
