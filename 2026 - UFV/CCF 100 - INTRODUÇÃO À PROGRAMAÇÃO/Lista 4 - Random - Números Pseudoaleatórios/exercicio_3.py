# ------------------------------------------------------------ #
# Copyright(c) 2026 Vinicius Gabriel Marques de Melo. All rights reserved.
# UFV - UNIVERSIDADE FEDERAL DE VIÇOSA
#
# Subject: CCF 100 - INTRODUÇÃO À PROGRAMAÇÃO
# Script Date: 2026/04/09 16:01
#
# Description:
# Exercício 3 da lista 4 de exercícios de programação.
# ------------------------------------------------------------ #


import random
import textwrap


HEAD = "Cara"
TAIL = "Coroa"
AVAILABLE_COINS = [HEAD, TAIL]
TIMES_FLIP_COIN = 5


def get_random_coin_flip():
    random_coin = random.choice(AVAILABLE_COINS)
    return random_coin

def filter_values_from_list(list, filter):
    filtered_list = [item for item in list if filter in item]
    return filtered_list

def start_program():
    input("<<Pressione enter para começar!>>")

    coins = []
    for index in range(1, TIMES_FLIP_COIN + 1):
        random_con_flip = get_random_coin_flip()
        coins.append(random_con_flip)

    heads = filter_values_from_list(coins, HEAD)
    tails = filter_values_from_list(coins, TAIL)

    msg = textwrap.dedent(f"""
        Foram realizados {TIMES_FLIP_COIN} lançamentos.
        Foram obtidos: {len(heads)} caras e {len(tails)} coroas!""")

    print(msg)


def main():
    start_program()


main()