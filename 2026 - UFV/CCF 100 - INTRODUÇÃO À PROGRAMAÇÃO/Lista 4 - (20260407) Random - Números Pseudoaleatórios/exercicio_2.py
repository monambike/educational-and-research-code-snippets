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


import platform
import random
import subprocess
import textwrap


NAME_AMOUNT = 5


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
            + JOGO - SORTEIO DE VENCEDOR                                +
            +                                                           +
            + Será sorteado um vencedor dentre {NAME_AMOUNT} candidatos!            +
            +                                                           +
            =============================================================\n"""))


def display_winner(names, winner):
    names_string = ",\" ".join(f"\"{name}\"" for name in names)

    message = textwrap.dedent(f"""
        =============== RESULTADO ===============
        Os nomes incluídos foram: {names_string}

        VENCEDOR: "{winner}"
        =========================================\n""")
    print(message)

def start_program():
    Utils.refresh_screen()

    print("INSIRA O NOME DOS CANDIDATOS ------------------------------")
    names = []
    for index in range(1, NAME_AMOUNT + 1):
        name = input(f"Por favor, informe o {index}º nome: ")
        names.append(name)
    print("-----------------------------------------------------------")

    random_winner = random.choice(names)
    display_winner(names, random_winner)


def main():
    """The main entrypoint of the application."""
    Utils.retry_loop(start_program)


# Running the main function of the application.
main()
