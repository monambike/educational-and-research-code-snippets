MAX_MINUTES = 15

MIN_SAFE_TEMP = 72
MAX_SAFE_TEMP = 75

is_process_ok = False
current_minutes = 1

while (current_minutes < MAX_MINUTES + 1):
    is_process_ok = False
    input_temp = input(f"[{current_minutes}min / {MAX_MINUTES}min] Informe a temperatura atual: ")

    current_temp = float(input_temp)

    if current_temp < MIN_SAFE_TEMP:
        print(f"Temperatura muito baixa no minuto {current_minutes}. Processo interrompido.")
        break
    if current_temp > MAX_SAFE_TEMP:
        print(f"Temperatura muito alta no minuto {current_minutes}. Processo interrompido.")
        break
    if current_temp >= MIN_SAFE_TEMP and  current_temp <= MAX_SAFE_TEMP:
        print(f"Minuto {current_minutes}: temperatura OK.")
        is_process_ok = True
    current_minutes += 1

if is_process_ok and current_minutes == MAX_MINUTES:
    print("Pasteurização concluída com sucesso. Leite próprio para o consumo.")
