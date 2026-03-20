# ------------------------------------------------------------
# Copyright(c) 2026 Vinicius Gabriel Marques de Melo. All rights reserved.
# UFV - UNIVERSIDADE FEDERAL DE VIÇOSA
#
# Subject: CCF 100 - INTRODUÇÃO À PROGRAMAÇÃO
# Script Date: 2026/03/20 18:18
#
# Description:
# Exercício 3 da lista 1 de exercícios de programação.
# ------------------------------------------------------------

import subprocess
import platform

CONST_MEAN_QUANTITY = 5

def clear_terminal() -> None:
    subprocess.run("cls" if platform.system() == "Windows" else "clear", shell = True)


# Contextualizing the script for the user.
print(f">>>>>>>>>>>>>>> <<<<<<<<<<<<<<<" + "\n"
    + "CALCULADORA DE MÉDIA" + "\n"
    + "\n"
    + "A média é um valor obtido informando um ou mais números, " + "\n"
    + "somando-os, e dividindo-os pela quantidade de números que " + "\n"
    + "foram informados." + "\n"
    + "Por favor, informe {CONST_MEAN_QUANTITY} números para que possa ser feita sua média."
    + ">>>>>>>>>>>>>>> <<<<<<<<<<<<<<<" + "\n" "\n")

user_input_sum = 0
for index in  CONST_MEAN_QUANTITY:
    user_input = input(f"Informe o {index}º valor: ")

    user_input_sum += user_input

mean = user_input_sum / CONST_MEAN_QUANTITY

print(f"O valor total da média é: {mean}")
