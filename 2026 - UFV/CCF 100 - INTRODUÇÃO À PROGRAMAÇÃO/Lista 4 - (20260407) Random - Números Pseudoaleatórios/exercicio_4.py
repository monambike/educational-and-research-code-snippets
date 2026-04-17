# ------------------------------------------------------------ #
# Copyright(c) 2026 Vinicius Gabriel Marques de Melo. All rights reserved.
# UFV - UNIVERSIDADE FEDERAL DE VIÇOSA
#
# Subject: CCF 100 - INTRODUÇÃO À PROGRAMAÇÃO
# Script Date: 2026/04/09 16:01
#
# Description:
# Exercício 4 da lista 4 de exercícios de programação.
# ------------------------------------------------------------ #


import platform
import random
import subprocess
import textwrap


CARDS = ["Ás", "1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "Dama", "Rei"]
CARD_GROUPS = ["Copas", "Espadas", "Ouros", "Paus"]


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
            ++++++++++++++++++++++++++++++ ++++++++++++++++++++++++++++++
            + JOGO - SORTEIO DE CARTAS                                  +
            +                                                           +
            + Será sorteado uma carta de um grupo do baralho!           +
            +                                                           +
            ++++++++++++++++++++++++++++++ ++++++++++++++++++++++++++++++"""))


def start_program():
    """The main method responsible for starting the program functions."""
    Utils.refresh_screen()

    random_card = random.choice(CARDS)
    random_card_group = random.choice(CARD_GROUPS)

    msg = f"""
        SORTEIO DA CARTA:
        Foi sorteado: {random_card} de {random_card_group}!\n"""

    print(textwrap.dedent(msg))


def main():
    """The main entrypoint of the application."""
    Utils.retry_loop(start_program)


# Running the main function of the application.
main()

