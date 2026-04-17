# ------------------------------------------------------------ #
# Copyright(c) 2026 Vinicius Gabriel Marques de Melo. All rights reserved.
# UFV - UNIVERSIDADE FEDERAL DE VIÇOSA
#
# Subject: CCF 100 - INTRODUÇÃO À PROGRAMAÇÃO
# Script Date: 2026/03/20 18:18
#
# Description:
# Exercício 3 da lista 1 de exercícios de programação.
# ------------------------------------------------------------ #

import platform
import subprocess
import textwrap


CONST_MEAN_QUANTITY = 5


def clear_terminal() -> None:
    """Clears the terminal based upon the operational system."""
    subprocess.run("cls" if platform.system() == "Windows" else "clear", shell = True)


def show_start_screen() -> None:
    """Shows start screen explaining script usage."""

    # Contextualizing the script for the user.
    print(textwrap.dedent(f"""
    >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>  <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
                        CALCULADORA DE MÉDIA
    ==============================================================

    A média é um valor obtido informando um ou mais números, soma-
    ndo-os,  e  dividindo-os  pela quantidade de números que foram
    informados.
    Por favor, informe {CONST_MEAN_QUANTITY} números para que pos-
    sa ser feita sua média. 
    
    >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>  <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<\n"""))


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


def calculate_and_display_mean():
    clear_terminal()

    show_start_screen()

    user_input_sum = 0
    user_inputs = []
    for index in  range(1, CONST_MEAN_QUANTITY + 1):
        user_input = input_numeric(f"Informe o {index}º valor: ")

        user_input_sum += user_input
        user_inputs.append(user_input)

    mean = user_input_sum / CONST_MEAN_QUANTITY

    # Format the result to replace dot with comma allowing more inputs.
    formatted_result = str(mean).replace(".", ",")

    print(textwrap.dedent(f"""
    Valores Informados: {", ".join(map(str, user_inputs))}
    O valor total da média é: {formatted_result}\n"""))


def main():
    while True:
        calculate_and_display_mean()
        
        while True:
            answer = input("Você gostaria de fazer outra operação?[Y/n]").lower()

            if answer in ("y", ""):
                break
            elif answer == "n":
                quit()


main()
