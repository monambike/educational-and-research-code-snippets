# ------------------------------------------------------------ #
# Copyright(c) 2026 Vinicius Gabriel Marques de Melo. All rights reserved.
# UFV - UNIVERSIDADE FEDERAL DE VIÇOSA
#
# Subject: CCF 100 - INTRODUÇÃO À PROGRAMAÇÃO
# Script Date: 2026/05/12 10:39
#
# Description:
# Exercício 2 da lista 7 de exercícios de programação.
# ------------------------------------------------------------ #


import platform
import subprocess
import textwrap


SUFFIX = " x "


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
            + FATORIAL DE UM NÚMERO                                     +
            +                                                           +
            + Esse script lerá um número inteiro positivo e realizará o +
            + fatorial dele.                                            +
            +                                                           +
            =============================================================""")
        print(message)


def start_program():
    Utils.refresh_screen()

    input_number = Utils.input_integer("\nPor favor, insira um número inteiro positivo: ")
    number = int(input_number)

    total = 0
    factor_as_string = ""
    for index in range(number, 0, -1):
        if index != number:
            total *= index
        else:
            total = index

        factor_as_string += f"{index}{SUFFIX}"
    factor_as_string = factor_as_string.removesuffix(SUFFIX)

    message_result = textwrap.dedent(f"""
    O valor total é de: {total}

    Conta Realizada: {factor_as_string} = {total}
    """)

    print(message_result)


def main():
    """The main entrypoint of the application."""
    Utils.retry_loop(start_program)


# Running the main function of the application.
main()
