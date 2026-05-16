print("Esse programa solicitará a mudança na temperatura até que atinja a temperatura limite.")

MAX_TEMP = 75

current_temp = 0
index_temp = 1
while current_temp < 75:
    change_temp = 0
    is_valid_temp = False
    while not is_valid_temp:
        input_temp = input(f"({index_temp}ª Entrada) Informe a mudança na temperatura: ")

        change_temp = float(input_temp)

        is_valid_temp = change_temp > 0
        if not is_valid_temp: print("Informe temperatura > 0!")

    current_temp += change_temp
    index_temp += 1

print(f"""
A temperatura passou de {MAX_TEMP}!

Temperatura Final Atingida: {current_temp}
Ciclos: {index_temp}

A temperatura ultrapassou em: {current_temp - MAX_TEMP}
""")
