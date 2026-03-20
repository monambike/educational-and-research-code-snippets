# ------------------------------------------------------------
# Copyright(c) 2026 Vinicius Gabriel Marques de Melo. All rights reserved.
# UFV - UNIVERSIDADE FEDERAL DE VIÇOSA
#
# Subject: CCF 100 - INTRODUÇÃO À PROGRAMAÇÃO
# Script Date: 2026/03/20 14:03
#
# Description:
# Exercício 1 da lista 1 de exercícios de programação.
# ------------------------------------------------------------

import subprocess
import platform


def clear_terminal() -> None:
    subprocess.run("cls" if platform.system() == "Windows" else "clear", shell = True)


def display_header() -> None:
    """Clears terminal and displays header explaining welcoming script usage.
    """

    clear_terminal()

    print("------------------------------" + "\n"
    + "CÁLCULO DE EXPRESSÃO" + "\n"
    + "\n"
    + "Esse programa fará o cálculo da expressão \"f(x) = Kx²+2x+5\", "
    + "onde K = 109." + "\n"
    + "\n"
    + "Para tanto, por favor, forneça um valor para \"x\":" + "\n"
    + "------------------------------" + "\n")


def retrieve_user_input() -> float:
    """Asks, validates and retrieves the user input.

    Returns:
        float: Returns the user input as a number.
    """
    
    is_wrong_input = False
    
    while True:
        user_input = None

        # Displaying header explaining the user input.
        display_header()

        # Displaying error message if input is wrong.
        if is_wrong_input: print("<< Por favor, insira um número válido! >>\n\n")

        try:
            # Retrieving the user input and converting to float.
            user_input = float(input("Valor de \"x\": "))
        except:
            is_wrong_input = True

        # If user already input a correct number, exits the function.
        if isinstance(user_input, (int, float)):
            return user_input


def calculate_expression(x: float) -> float:
    """Calculates a expression "f(x) = Kx²+2x+5" based on the value
    of "x" returning a float value.

    Args:
        x (float): _description_

    Returns:
        float: _description_
    """
    CONST_K = 109

    # f(x) = Kx² + 2x + 5
    y = CONST_K * x**2 + 2*x + 5
    
    return y


keep_trying = True
while True:
    user_input = retrieve_user_input()
    result = calculate_expression(user_input)

    print(f"O resultado se dá por: \"{str(result)}\".\n\n")
    
    valid_answer = False
    while not valid_answer:
        answer = input("Você gostaria de tentar novamente?[Y/n]").lower()

        if answer in ("y", ""):
            break
        elif answer == "n":
            quit()
