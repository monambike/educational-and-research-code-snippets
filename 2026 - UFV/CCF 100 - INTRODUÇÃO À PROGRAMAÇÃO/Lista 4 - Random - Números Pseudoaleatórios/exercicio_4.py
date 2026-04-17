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

CARDS = ["Ás", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Dama", "Rei"]
CARD_GROUPS = ["Copas", "Espadas" "Ouros", "Paus"]


import random
def main():
  random_card = random.choice(CARDS)
  random_card_group = random.choice(CARD_GROUPS)

  print(f"{random_card_group} e {random_card}")
