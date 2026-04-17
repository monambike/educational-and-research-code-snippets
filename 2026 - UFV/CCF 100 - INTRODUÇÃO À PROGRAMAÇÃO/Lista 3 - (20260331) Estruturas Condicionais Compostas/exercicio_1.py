# ------------------------------------------------------------ #
# Copyright(c) 2026 Vinicius Gabriel Marques de Melo. All rights reserved.
# UFV - UNIVERSIDADE FEDERAL DE VIÇOSA
#
# Subject: CCF 100 - INTRODUÇÃO À PROGRAMAÇÃO
# Script Date: 2026/03/31 10:39
#
# Description:
# Exercício 1 da lista 3 de exercícios de programação.
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
        =============================================================
        + CALCULADORA DE PREÇO DE MULTA                             +
        +                                                           +
        + Esse  programa  faz  o  cálculo para o valor de multa que +
        + deve  ser  paga com base no valor da kilometragem que foi +
        + passada.                                                  +
        +                                                           +
        +  R$50,00 se ultrapassar em até 10km                       +
        + R$100,00 se ultrapassar em até 30km                       +
        + R$200,00 se ultrapassar mais de 30km                      +
        =============================================================\n"""))


def return_tax(difference_velocity):
    if 0 < difference_velocity <= 10:
        return 50
    if 10 < difference_velocity <= 30:
        return 100
    if 30 < difference_velocity:
        return 200
    return 0


def validate():
    kilometers = 0
    tax = 0


def msg_exceeded(tax, difference_velocity):
    print(f"\nVocê ultrapassou o limite de velocidade em: {difference_velocity}km")
    print(f"A quantia à ser paga é de: {tax}\n")


def msg_not_exceeded():
    print("\nVocê não ultrapassou o limite de velocidade da via.")
    print("Não é necessário pagar a taxa.\n")


def start_program():
    """The main method responsible for starting the program functions."""

    # Displaying the start screen.
    refresh_screen()

    max_velocity = input_numeric("Insira a velocidade máxima da via: ")
    walking_velocity = input_numeric("Informe a qual velocidade você estava andando: ")

    difference_velocity = walking_velocity - max_velocity

    tax = return_tax(difference_velocity)
    print(f"diferença: {difference_velocity}")
    print(f"taxa: {tax}")

    if (difference_velocity == 0):
        msg_not_exceeded()
    else:
        msg_exceeded(tax, difference_velocity)


def main():
    """The main entrypoint of the application."""
    retry_loop(start_program)


# Running the main function of the application.
main()
