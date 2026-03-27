# ------------------------------------------------------------ #
# Copyright(c) 2026 Vinicius Gabriel Marques de Melo. All rights reserved.
# UFV - UNIVERSIDADE FEDERAL DE VIÇOSA
#
# Subject: CCF 100 - INTRODUÇÃO À PROGRAMAÇÃO
# Script Date: 2026/03/20 14:03
#
# Description:
# Exercício 1 da lista 1 de exercícios de programação.
# ------------------------------------------------------------ #


import platform
import subprocess
import textwrap


CONST_K = 109


def clear_terminal() -> None:
    """Clears the terminal based upon the operational system."""
    subprocess.run("cls" if platform.system() == "Windows" else "clear", shell = True)


def show_start_screen() -> None:
    """Shows start screen explaining script usage."""

    print(textwrap.dedent("""
    ------------------------------------------------------------
                        CÁLCULO DE EXPRESSÃO
    ------------------------------------------------------------

    Esse programa fará o cálculo da expressão "f(x) = Kx²+2x+5",
    onde K = 109.
    
    Para tanto, por favor, forneça um valor para "x":
    ------------------------------------------------------------\n"""))


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

            return user_input
        except:
            is_wrong_input = True


def calculate_expression(x: float) -> float:
    """Calculates a expression "f(x) = Kx²+2x+5" based on the value
    of "x" returning a float value.

    Args:
        x (float): The input value of "x".

    Returns:
        float: The result of "f(x)" from the expression.
    """

    # f(x) = Kx² + 2x + 5
    y = CONST_K * x**2 + 2*x + 5

    return y


def run_calculation():
    user_input = input_numeric("Valor de \"x\": ")
    result = calculate_expression(user_input)
    
    # Remove leading zeros.
    if (result.is_integer()): result = int(result)

    return result


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


def start_program():
    """The main method responsible for starting the program functions."""

    # Running the calculation and storing the result.
    result = run_calculation()

    # Format the result to replace dot with comma allowing more inputs.
    formatted_result = str(result).replace(".", ",")

    print(f"O resultado se dá por: \"{formatted_result}\".\n\n")


def main():
    """The main entrypoint of the application."""
    retry_loop(start_program)


main()
