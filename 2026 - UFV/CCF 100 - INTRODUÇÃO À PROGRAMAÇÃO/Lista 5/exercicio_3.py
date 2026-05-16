# ------------------------------------------------------------ #
# Copyright(c) 2026 Vinicius Gabriel Marques de Melo. All rights reserved.
# UFV - UNIVERSIDADE FEDERAL DE VIÇOSA
#
# Subject: CCF 100 - INTRODUÇÃO À PROGRAMAÇÃO
# Script Date: 2026/04/28 11:19
#
# Description:
# Exercício 3 da atividade prática 3 de exercícios de programação.
# ------------------------------------------------------------ #

import textwrap

input_value = input("Informe um valor para que seja disposta sua tabuada: ")
int_value = int(input_value)

text = ""
index = 0
for index in range(1, int_value + 1):
    result = index * int_value
    text += f"{index} x {int_value} = {result}\n"

msg = textwrap.dedent(f"""
--- Tabuada do {int_value} ---
{text}""")

print(msg)
