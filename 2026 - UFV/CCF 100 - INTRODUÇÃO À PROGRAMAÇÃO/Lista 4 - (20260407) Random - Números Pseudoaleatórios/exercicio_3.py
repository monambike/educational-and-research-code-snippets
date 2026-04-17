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


import platform
import random
import subprocess
import textwrap


HEAD = "Cara"
TAIL = "Coroa"
AVAILABLE_COINS = [HEAD, TAIL]
TIMES_FLIP_COIN = 5


class Utils:
    def clear_terminal() -> None:
        """Clears the terminal based upon the operational system."""
        subprocess.run("cls" if platform.system() == "Windows" else "clear", shell = True)


    def refresh_screen():
        """Clears the terminal and displays the start screen of the application."""
        Utils.clear_terminal()

        Messages.start_screen()


    def retry_loop(action: callable[[], None]):
        """Runs a loop of an action until the user decides to quit.

        Args:
            action (callable[[], None]): The action to be performed in the loop.
        """
        while True:
            action()

            while True:
                answer = input("Gostaria de jogar novamente?[Y/n]").lower()

                if answer in ("y", ""):
                    break
                elif answer == "n":
                    quit()


class Messages:
    def start_screen():
        """Displays the start screen of the application."""
        print(textwrap.dedent(f"""
            =============================================================
            + JOGO - CARA OU CORIA                                      +
            +                                                           +
            + Será sorteado cara ou coroa {TIMES_FLIP_COIN} vezes!                      +
            +                                                           +
            ============================================================="""))


def get_random_coin_flip():
    random_coin = random.choice(AVAILABLE_COINS)
    return random_coin


def filter_values_from_list(list, filter):
    filtered_list = [item for item in list if filter in item]
    return filtered_list


def start_program():
    Utils.refresh_screen()

    coins = []
    for index in range(1, TIMES_FLIP_COIN + 1):
        random_con_flip = get_random_coin_flip()
        coins.append(random_con_flip)

    heads = filter_values_from_list(coins, HEAD)
    tails = filter_values_from_list(coins, TAIL)

    msg = textwrap.dedent(f"""
        Foram realizados {TIMES_FLIP_COIN} lançamentos.
        Foram obtidos: {len(heads)} caras e {len(tails)} coroas!\n""")

    print(msg)


def main():
    """The main entrypoint of the application."""
    Utils.retry_loop(start_program)


# Running the main function of the application.
main()
