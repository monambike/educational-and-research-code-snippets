# ------------------------------------------------------------ #
# Copyright(c) 2026 Vinicius Gabriel Marques de Melo. All rights reserved.
# UFV - UNIVERSIDADE FEDERAL DE VIÇOSA
#
# Subject: CCF 100 - INTRODUÇÃO À PROGRAMAÇÃO
# Script Date: 2026/03/27 15:26
#
# Description:
# Exercício 7 da lista 2 de exercícios de programação.
# ------------------------------------------------------------ #


from enum import Enum
import platform
import subprocess
import textwrap


class Operations(Enum):
    SUM = 1
    SUBTRACTION = 2
    MULTIPLICATION = 3
    DIVISION = 4


class Operation():
    @staticmethod
    def check_operation(operation: str) -> Operation:
        """Checks if the given operation is valid and returns the corresponding enum.

        Args:
            operation (str): The operation to be checked.

        Returns:
            Operation: The corresponding enum value.
        """
        match operation:
            case "1" | "+":
                return Operations.SUM
            case "2" | "-":
                return Operations.SUBTRACTION
            case "3" | "*":
                return Operations.MULTIPLICATION
            case "4" | "/":
                return Operations.DIVISION
            case _:
                return None


    @staticmethod
    def do_calculation(first_value, second_value, operation) -> Operation:
        match operation:
            case Operations.SUM:
                return first_value + second_value
            case Operations.SUBTRACTION:
                return first_value - second_value
            case Operations.MULTIPLICATION:
                return first_value * second_value
            case Operations.DIVISION:
                return first_value / second_value if second_value != 0 else None
            case _:
                return None


    @staticmethod
    def operation_as_string(operation) -> str:
        match operation:
            case Operations.SUM:
                return "Soma"
            case Operations.SUBTRACTION:
                return "Subtração"
            case Operations.MULTIPLICATION:
                return "Multiplicação"
            case Operations.DIVISION:
                return "Divisão"
            case _:
                return None


    @staticmethod
    def operation_symbol_as_string(operation) -> str:
        match operation:
            case Operations.SUM:
                return "+"
            case Operations.SUBTRACTION:
                return "-"
            case Operations.MULTIPLICATION:
                return "*"
            case Operations.DIVISION:
                return "/"
            case _:
                return None


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


def input_operation(input_text: str) -> Operations:
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
            user_input = input(input_text)

            operation = Operation.check_operation(user_input)

            if operation is None:
                is_wrong_input = True
            else:
                return operation
        except:
            is_wrong_input = True

        if is_wrong_input:
            refresh_screen()
            # Displaying error message if input is wrong.
            print("""<< Por favor, insira uma operação válida! >>""")


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
        + CALCULADORA SIMPLES                                       +
        +                                                           +
        + Bem-vindo à Calculadora Simples!                          +
        + O programa irá solicitar 2 valores, e em seguida será so- +
        + licitado a operação a ser realizada.                      +
        ++++++++++++++++++++++++++++++ ++++++++++++++++++++++++++++++\n"""))


def start_program():
    """The main entrypoint of the application."""

    # Displaying the start screen.
    refresh_screen()

    # Requesting the user for four integer inputs.
    value_1 = input_numeric(f"Digite o 1º número inteiro: ")
    value_2 = input_numeric(f"Digite o 2º número inteiro: ")
    operation = input_operation(textwrap.dedent(f"""
        1 [+] Soma 2 [-] Subtração, 3 [*] Multiplicação, 4 [/] Divisão
        Digite a operação a ser realizada: """))

    result = Operation.do_calculation(value_1, value_2, operation)
    if result is None: result = "Inválido"

    operation_string = Operation.operation_as_string(operation)
    operation_symbol = Operation.operation_symbol_as_string(operation)

    # Displaying the result of the validation.
    print(textwrap.dedent(f"""
        <<< RESULTADO >>>
        Valor 1: {value_1} / Valor 2: {value_2} / Operação: {operation_string}
        A operação realizada foi {value_1} {operation_symbol} {value_2} = {result}\n"""))


def main():
    """The main entrypoint of the application."""
    retry_loop(start_program)


# Running the main function of the application.
main()
