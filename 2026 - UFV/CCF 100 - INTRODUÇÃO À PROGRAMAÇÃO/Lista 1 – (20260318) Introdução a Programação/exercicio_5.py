# ------------------------------------------------------------ #
# Copyright(c) 2026 Vinicius Gabriel Marques de Melo. All rights reserved.
# UFV - UNIVERSIDADE FEDERAL DE VIÇOSA
#
# Subject: CCF 100 - INTRODUÇÃO À PROGRAMAÇÃO
# Script Date: 2026/03/21 19:16
#
# Description:
# Exercício 5 da lista 1 de exercícios de programação.
# ------------------------------------------------------------ #

import platform
import subprocess
import textwrap


def clear_terminal() -> None:
    """Clears the terminal based upon the operational system."""
    subprocess.run("cls" if platform.system() == "Windows" else "clear", shell = True)


def show_start_screen() -> None:
    """Shows start screen explaining script usage."""

    # Contextualizing the script for the user.
    print(textwrap.dedent(f"""
    <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<  >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
                  CONVERSOR DE FARENHEIT PARA CELSIUS
                    ⋆꙳•̩̩͙❅*̩̩͙‧͙    ‧͙*̩̩͙❆ ͙͛ ̩̩͙‧͙    ‧͙*̩ ˚₊⋆ ⋆꙳•̩̩͙❅*

    A fórmula para converter de Farenheit para Celsius é:
    "C = (F - 32) * 5 / 9".

    Por favor, informe um valor em Farenheit para que seja feita a
    conversão para Celsius.
    <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<  >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\n"""))


def input_numeric(input_text: str) -> float:
    """Requests the user for a numeric input and validates it.

    Accepts both comma and dot as decimal separators. Repeats
    until a valid number is entered.

    Returns:
        float: The validated numeric input.
    """
    
    is_wrong_input = False
    
    while True:
        user_input = None

        clear_terminal()

        # Displaying header explaining the user input.
        show_start_screen()

        # Displaying error message if input is wrong.
        if is_wrong_input:
            print("""<< Por favor, insira um número válido! >>""")

        try:
            # Retrieving the user input and converting to float and allowing
            # conma as input.
            user_input = float(input(input_text).replace(",", "."))
        except:
            is_wrong_input = True

        # If user already input a correct number, exits the function.
        if isinstance(user_input, (int, float)):
            return user_input


def convert_celsius_to_farenheit():
    farenheit = input_numeric("Informe o Valor em Farenheit: ")

    celsius = (farenheit - 32) * 5 / 9

    print(f"{farenheit}°F equivalem a {celsius:.2f}°C.")


def main():
    while True:
        convert_celsius_to_farenheit()
        
        while True:
            answer = input("Você gostaria de fazer outra operação?[Y/n]").lower()

            if answer in ("y", ""):
                break
            elif answer == "n":
                quit()


main()
