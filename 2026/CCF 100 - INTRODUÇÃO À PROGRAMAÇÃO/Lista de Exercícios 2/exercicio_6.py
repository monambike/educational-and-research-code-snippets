# ------------------------------------------------------------ #
# Copyright(c) 2026 Vinicius Gabriel Marques de Melo. All rights reserved.
# UFV - UNIVERSIDADE FEDERAL DE VIÇOSA
#
# Subject: CCF 100 - INTRODUÇÃO À PROGRAMAÇÃO
# Script Date: 2026/03/24 14:05
#
# Description:
# Exercício 6 da lista 2 de exercícios de programação.
# ------------------------------------------------------------ #


import platform
import subprocess
import textwrap


def clear_terminal() -> None:
    """Clears the terminal based upon the operational system."""
    subprocess.run("cls" if platform.system() == "Windows" else "clear", shell = True)


def input_numeric(input_text: str, allow_zero: bool = False) -> float:
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
            user_input = input(input_text)

            if allow_zero and user_input == "":
                return 0
            
            user_input = float(user_input.replace(",", "."))

            return user_input
        except:
            is_wrong_input = True

        if is_wrong_input:
            refresh_screen()
            # Displaying error message if input is wrong.
            print("""<< Por favor, insira um número válido! >>""")


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


def refresh_screen() -> None:
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


def refresh_screen() -> None:
    """Clears the terminal and displays the start screen of the application."""
    clear_terminal()
  
    show_start_screen()


def show_start_screen():
    """Displays the start screen of the application."""
    print(textwrap.dedent("""
    ------------------------------------------------------------
    CALCULADORA DE BHASKARA

    Por favor, informe os coeficientes da equação do segundo grau
    para calcular as raízes da equação.

    ax² + bx + c = 0
    a, b e c são os coeficientes da equação.
    ------------------------------------------------------------\n"""))


def calc_bhaskara_delta(a, b, c) -> float:
    # Delta = b² - 4ac
    return b**2 - 4*a*c


def calc_bhaskara_root(a, b, delta, negative_root_delta = False):
    sign = -1 if negative_root_delta else 1
    return (-b + sign * (delta**0.5)) / (2*a)

def calc_bhaskara(a, b, c) -> tuple:
    delta = calc_bhaskara_delta(a, b, c)

    # x = (-b ± √delta) / 2a

    if delta > 0:
        x1 = calc_bhaskara_root(a, b, delta)
        x2 = calc_bhaskara_root(a, b, delta, negative_root_delta = True)
    elif delta == 0:
        x1 = x2 = calc_bhaskara_root(a, b, delta)
    elif delta < 0:
        x1 = x2 = None

    return (x1, x2)


def input_coeficient(coefficient):
    while True:
        value = input_numeric(f"Por favor, informe o coeficiente {coefficient}: ")

        if value != 0:
            return value

        print("""<< O coeficiente a não pode ser zero! >>""")


def start_program():
    """The main entrypoint of the application."""
    refresh_screen()

    # Asking the input for the coeficient a.
    input_a = input_coeficient("a")

    # Asking the input for the coeficient b.
    input_b = input_coeficient("b")

    # Asking the input for the coeficient c.
    input_c = input_numeric("Por favor, informe o coeficiente c [0]: ", True)

    result = calc_bhaskara(input_a, input_b, input_c)

    print(f"\nPara os valores de a = {input_a}, b = {input_b} e c = {input_c}.")

    if result == (None, None):
        print("A equação não possui raízes reais.")
    elif result[0] != result[1] and result[0]:
        print(f"As raízes da equação são: x¹ = {result[0]} e x² = {result[1]}")
    elif result[0] == result[1]:
        print(f"As equação tem apenas a raiz: x = {result[0]}")



def main():
    """The main entrypoint of the application."""
    retry_loop(start_program)


# Running the main function of the application.
main()