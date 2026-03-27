# ------------------------------------------------------------ #
# Copyright(c) 2026 Vinicius Gabriel Marques de Melo. All rights reserved.
# UFV - UNIVERSIDADE FEDERAL DE VIÇOSA
#
# Subject: CCF 100 - INTRODUÇÃO À PROGRAMAÇÃO
# Script Date: 2026/03/24 14:07
#
# Description:
# Exercício 8 da lista 2 de exercícios de programação.
# ------------------------------------------------------------ #


import platform
import subprocess
import textwrap
from enum import Enum


class Weekday(Enum):
    SUNDAY    = 1
    MONDAY    = 2
    TUESDAY   = 3
    WEDNESDAY = 4
    THURSDAY  = 5
    FRIDAY    = 6
    SATURDAY  = 7


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

            is_wrong_input = user_input < 1 or user_input > 7

            if not is_wrong_input:
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


def show_start_screen():
    """Displays the start screen of the application."""
    print(textwrap.dedent(f"""
    ============================== ==============================
    CONVERSOR DE NÚMEROS PARA DIAS DA SEMANA

    Por  favor , informe um número para receber o valor da semana
    correspondente.
    ============================== ==============================\n"""))


def weekday_to_string(number) -> str:
    match Weekday(number):
        case Weekday.SUNDAY:
            return "Domingo"
        case Weekday.MONDAY:
            return "Segunda-feira"
        case Weekday.TUESDAY:
            return "Terça-feira"
        case Weekday.WEDNESDAY:
            return "Quarta-feira"
        case Weekday.THURSDAY:
            return "Quinta-feira"
        case Weekday.FRIDAY:
            return "Sexta-feira"
        case Weekday.SATURDAY:
            return "Sábado"


def start_program():
    """The main entrypoint of the application."""
    refresh_screen()

    number = input_numeric("Por favor informe um valor para receber o valor da semana correspondente: ")

    print(weekday_to_string(number))


def main():
    retry_loop(start_program)


main()
