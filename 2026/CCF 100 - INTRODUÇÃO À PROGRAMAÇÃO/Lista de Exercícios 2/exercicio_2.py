# ------------------------------------------------------------ #
# Copyright(c) 2026 Vinicius Gabriel Marques de Melo. All rights reserved.
# UFV - UNIVERSIDADE FEDERAL DE VIÇOSA
#
# Subject: CCF 100 - INTRODUÇÃO À PROGRAMAÇÃO
# Script Date: 2026/03/24 13:08
#
# Description:
# Exercício 2 da lista 2 de exercícios de programação.
# ------------------------------------------------------------ #


import platform
import subprocess
import textwrap


def clear_terminal() -> None:
    """Clears the terminal based upon the operational system."""
    subprocess.run("cls" if platform.system() == "Windows" else "clear", shell = True)


def input_numeric(input_text: str) -> float:
    """Requests the user for a numeric input and validates it.

    Accepts both comma and dot as decimal separators. Repeats
    until a valid number is entered.

    Returns:
        float: The validated numeric input.
    """
    while True:
        is_wrong_input = False

        user_input = None
        try:
            # Retrieving the user input and converting to float and allowing
            # conma as input.
            user_input = float(input(input_text).replace(",", "."))

            return user_input
        except:
            is_wrong_input = True

        if is_wrong_input:
            refresh_screen()
            # Displaying error message if input is wrong.
            print("""<< Por favor, insira um número válido! >>""")


def refresh_screen():
    """Clears the terminal and displays the start screen of the application."""
    clear_terminal()

    show_start_screen()


def retry_loop(action: callable[[], None]):
    """Runs a loop of an action until the user decides to quit.

    Args:
        action (callable[[], None]): The action to be performed in the loop.
    """
    while True:
        action()

        while True:
            answer = input("Você gostaria de fazer outra operação?[Y/n]").lower()

            if answer in ("y", ""):
                break
            elif answer == "n":
                quit()


def show_start_screen():
    """Displays the start screen of the application."""
    print(textwrap.dedent(f"""
        +-+-+-+-+-+-+-+-+-+-+-+-+-+-+- -+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
        CLASSIFICADOR DE NÚMEROS
        +-+-+-+-+-+-+-+-+-+-+-+-+-+-+- -+-+-+-+-+-+-+-+-+-+-+-+-+-+-+

        Este  programa  irá solicitar que você insira um número e irá
        classificá-lo como positivo, negativo ou zero.
        +-+-+-+-+-+-+-+-+-+-+-+-+-+-+- -+-+-+-+-+-+-+-+-+-+-+-+-+-+-+
    """))


def number_type(number):
    """Classifies a number as positive, negative or zero."""
    match number:
        case _ if number < 0:
            return "negativo"
        case 0:
            return "zero"
        case _ if number > 0:
            return "positivo"
        case _:
            return None


def start_program():
    """The main method responsible for starting the program functions."""

    refresh_screen()

    print("Digite um número para verificar se ele é positivo, negativo ou zero:")

    # Getting the user input and classifying it.
    input = input_numeric("Insira um valor para checar: ")
    type = number_type(input)

    # Displaying the result.
    print(f"O número {input} é um número \"{type}\".")


def main():
    """The main entrypoint of the application."""
    retry_loop(start_program)


# Running the main function of the application.
main()
