# ------------------------------------------------------------ #
# Copyright(c) 2026 Vinicius Gabriel Marques de Melo. All rights reserved.
# UFV - UNIVERSIDADE FEDERAL DE VIÇOSA
#
# Subject: CCF 100 - INTRODUÇÃO À PROGRAMAÇÃO
# Script Date: 2026/04/28 10:40
#
# Description:
# Exercício 2 da atividade prática 3 de exercícios de programação.
# ------------------------------------------------------------ #


import textwrap


input_amount  = input("Indique um número do qual você gostaria de obter o fatorial: ")
int_amount = int(input_amount)

int_numbers = [index for index in range(1, int_amount + 1)]
str_numbers = list(map(str, int_numbers))

string_test = " * ".join(str_numbers)

result = 1
for index in range(1, int_amount + 1):
    result *= index

message_result = textwrap.dedent(f"""
    Processo do Cálculo:
    {input_amount}! = {string_test} = {result}

    O fatorial de {input_amount}! é: {int_numbers}""")

print(message_result)
