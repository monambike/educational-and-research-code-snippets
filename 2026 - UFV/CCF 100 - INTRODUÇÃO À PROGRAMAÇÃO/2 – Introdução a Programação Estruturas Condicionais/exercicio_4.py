# ------------------------------------------------------------ #
# Copyright(c) 2026 Vinicius Gabriel Marques de Melo. All rights reserved.
# UFV - UNIVERSIDADE FEDERAL DE VIÇOSA
#
# Subject: CCF 100 - INTRODUÇÃO À PROGRAMAÇÃO
# Script Date: 2026/03/2 15:13
#
# Description:
# Exercício 4 da lista 2 de exercícios de programação.
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


def input_integer(input_text: str) -> int:
    """Requests the user for a integer input and validates it.

    Accepts only integer values. Repeats until a valid number is entered.

    Returns:
        int: The validated integer input.
    """
    while True:
        is_wrong_input = False

        user_input = None
        try:
            # Retrieving the user input and converting to float and allowing
            # conma as input.
            user_input = int(input(input_text))

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


def show_start_screen() -> None:
    """Displays the start screen of the application."""
    print(textwrap.dedent(f"""
        ++++++++++++++++++++++++++++++ ++++++++++++++++++++++++++++++
        + VALIDADOR DE FORMA DE TRIÂNGULO                           +
        +                                                           +
        + O programa irá solicitar 3 valores inteiros e apartir de- +
        + les será informado se é possível com esses valores criar  +
        + um triângulo ou não.                                      +
        ++++++++++++++++++++++++++++++ ++++++++++++++++++++++++++++++\n"""))


def start_program():
    """The main entrypoint of the application."""

    # Displaying the start screen.
    refresh_screen()

    # Requesting the user for four integer inputs.
    a = input_integer(f"Digite o 1º número inteiro: ")
    b = input_integer(f"Digite o 2º número inteiro: ")
    c = input_integer(f"Digite o 3º número inteiro: ")

    # Validating if is a triangle based on the formula:
    # a + b > c, a + c > b, b + c > a
    is_triangle = a + b > c and a + c > b and b + c > a

    # Displaying the result of the validation.
    is_triangle_as_string = "formam" if is_triangle else "não formam"
    print(f"Os números {is_triangle_as_string} um triângulo.")


def main():
    """The main entrypoint of the application."""
    retry_loop(start_program)


# Running the main function of the application.
main()
