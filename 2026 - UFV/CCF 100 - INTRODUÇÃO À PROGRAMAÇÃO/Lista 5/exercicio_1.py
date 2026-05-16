# ------------------------------------------------------------ #
# Copyright(c) 2026 Vinicius Gabriel Marques de Melo. All rights reserved.
# UFV - UNIVERSIDADE FEDERAL DE VIÇOSA
#
# Subject: CCF 100 - INTRODUÇÃO À PROGRAMAÇÃO
# Script Date: 2026/04/28 10:32
#
# Description:
# Exercício 1 da lista 5 de exercícios de programação.
# ------------------------------------------------------------ #


import textwrap


# E = 1/1 + 1 /2 + 1/3 + ... + 1/N
input_amount = input("Insira um valor que indique até quando você quer somar: ")
int_amount = int(input_amount)

int_numbers = [index for index in range(1, int_amount + 1)]
str_numbers = list(map(str, int_numbers))

result_fractions = " + 1/".join(str_numbers)

sum_numbers = sum(int_numbers)
result = 1 / sum_numbers
result_fraction = f"1 / {sum_numbers}"

msg = textwrap.dedent(f"""
    E = {result_fractions}

    O resultado na forma fracionária é: {result_fraction}
    O resultado na forma decimal é: {round(result, 4)}""")
print(msg)
