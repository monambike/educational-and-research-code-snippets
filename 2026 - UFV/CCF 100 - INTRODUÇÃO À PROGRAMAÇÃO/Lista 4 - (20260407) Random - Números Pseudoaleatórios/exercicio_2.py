# ------------------------------------------------------------ #
# Copyright(c) 2026 Vinicius Gabriel Marques de Melo. All rights reserved.
# UFV - UNIVERSIDADE FEDERAL DE VIÇOSA
#
# Subject: CCF 100 - INTRODUÇÃO À PROGRAMAÇÃO
# Script Date: 2026/04/09 16:01
#
# Description:
# Exercício 2 da lista 4 de exercícios de programação.
# ------------------------------------------------------------ #

import random
import textwrap

NAME_AMOUNT = 5

def display_winner(names, winner):
    message = textwrap.dedent(f"""
        =============== RESULTADO ===============
        Vencedor: \"{winner}\""

        Os nomes incluídos foram: {names}
          """)
    print(message)

def main():
    names = []
    for index in range(1, NAME_AMOUNT + 1):
        name = input(f"Por favor, informe o {index}º nome: ")
        names.append(name)

    random_winner = random.choice(names)
    display_winner(names, random_winner)

main()