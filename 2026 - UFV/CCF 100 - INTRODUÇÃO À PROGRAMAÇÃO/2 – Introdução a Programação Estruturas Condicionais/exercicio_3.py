# ------------------------------------------------------------ #
# Copyright(c) 2026 Vinicius Gabriel Marques de Melo. All rights reserved.
# UFV - UNIVERSIDADE FEDERAL DE VIÇOSA
#
# Subject: CCF 100 - INTRODUÇÃO À PROGRAMAÇÃO
# Script Date: 2026/03/24 13:26
#
# Description:
# Exercício 3 da lista 2 de exercícios de programação.
# ------------------------------------------------------------ #


import platform
import subprocess
import textwrap


CONST_NUMBERS_QUANTITY = 4


def clear_terminal() -> None:
    """Clears the terminal based upon the operational system."""
    subprocess.run("cls" if platform.system() == "Windows" else "clear", shell = True)


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
        + CALCULADORA DE NÚMEROS PARES                              +
        +                                                           +
        + O programa irá solicitar 4 números inteiros. Serão então  +
        + identificados os números pares e calculada a soma.        +
        ++++++++++++++++++++++++++++++ ++++++++++++++++++++++++++++++\n"""))


def start_program():
    """The main entrypoint of the application."""

    # Displaying the start screen.
    refresh_screen()

    even_numbers = []
    numbers = []
    for index in range(1, CONST_NUMBERS_QUANTITY + 1):
        value = input_integer(f"Insira o {index}º número: ")

        # Appending all numbers to the numbers list.
        numbers.append(value)
        # Appending even numbers to the even numbers list.
        if (value % 2 == 0):
            even_numbers.append(value)

    # Calculating the sum of the even numbers.
    even_numbers_sum = sum(even_numbers)

    # Displaying the result.
    print(textwrap.dedent(f"""
        Todos os valores informados: {numbers}
        Os valores pares informados são: {even_numbers}
        O resultado da soma é: {even_numbers_sum}"""))


def main():
    """The main entrypoint of the application."""
    retry_loop(start_program)


# Running the main function of the application.
main()
