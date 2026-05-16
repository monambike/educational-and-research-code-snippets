# ------------------------------------------------------------ #
# Copyright(c) 2026 Vinicius Gabriel Marques de Melo. All rights reserved.
# UFV - UNIVERSIDADE FEDERAL DE VIÇOSA
#
# Subject: CCF 100 - INTRODUÇÃO À PROGRAMAÇÃO
# Script Date: 2026/05/12 10:39
#
# Description:
# Exercício 1 da lista 7 de exercícios de programação.
# ------------------------------------------------------------ #


import platform
import subprocess
import textwrap


NUMBER_START = 1
SUFFIX = " + "


class Utils:
    def clear_terminal() -> None:
        """Clears the terminal based upon the operational system."""
        subprocess.run("cls" if platform.system() == "Windows" else "clear", shell = True)


    def refresh_screen():
        """Clears the terminal and displays the start screen of the application."""
        Utils.clear_terminal()

        Messages.start_screen()


    def retry_loop(action: callable[[], None]):
        """Runs a loop of an action until the user decides to quit.

        Args:
            action (callable[[], None]): The action to be performed in the loop.
        """
        while True:
            action()

            while True:
                answer = input("Gostaria de tentar novamente?[Y/n] ").lower()

                if answer in ("y", ""):
                    break
                elif answer == "n":
                    quit()


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
                Utils.refresh_screen()
                # Displaying error message if input is wrong.
                print("""<< Por favor, insira um número válido! >>""")


class Messages:
    def start_screen():
        """Displays the start screen of the application."""
        message = textwrap.dedent(f"""
            =============================================================
            + SOMA DE "N" NÚMEROS ÍMPARES                               +
            +                                                           +
            + Esse programa irá de {NUMBER_START} até o número escolhido, pegando to-+
            + dos os ímpares e realizando a soma.                       +
            +                                                           +
            =============================================================""")
        print(message)


def start_program():
    Utils.refresh_screen()

    number_end_input = Utils.input_integer("\nPor favor, selecione até quando deve ser realizada a soma: ")
    number_end = int(number_end_input)

    sum_as_string = ""
    total_sum = 0
    for index in range(1, number_end):
        if index % 2 != 0:
            total_sum += index

            sum_as_string += f"{index}{SUFFIX}"

    sum_as_string = sum_as_string.removesuffix(SUFFIX)

    message_result = textwrap.dedent(f"""
    Somando todos os valores temos: {total_sum}

    Conta Realizada: {sum_as_string} = {total_sum}
    """)
    print(message_result)


def main():
    """The main entrypoint of the application."""
    Utils.retry_loop(start_program)


# Running the main function of the application.
main()
