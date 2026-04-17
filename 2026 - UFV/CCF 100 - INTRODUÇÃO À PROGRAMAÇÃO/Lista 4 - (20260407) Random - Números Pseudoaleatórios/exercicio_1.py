# ------------------------------------------------------------ #
# Copyright(c) 2026 Vinicius Gabriel Marques de Melo. All rights reserved.
# UFV - UNIVERSIDADE FEDERAL DE VIÇOSA
#
# Subject: CCF 100 - INTRODUÇÃO À PROGRAMAÇÃO
# Script Date: 2026/04/09 16:01
#
# Description:
# Exercício 1 da lista 4 de exercícios de programação.
# ------------------------------------------------------------ #

import platform
import random
import subprocess
import textwrap


MINIMUM_VALUE = 1
MAXIMUM_VALUE = 100


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
                answer = input("Você acertou!! Gostaria de jogar novamente?[Y/n]").lower()

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
        print(textwrap.dedent(f"""
            ++++++++++++++++++++++++++++++ ++++++++++++++++++++++++++++++
            + JOGO - ADIVINHE O NÚMERO ALEATÓRIO {MINIMUM_VALUE} à {MAXIMUM_VALUE}                +
            +                                                           +
            + Será sorteado um número de {MINIMUM_VALUE} à {MAXIMUM_VALUE}, após isso, informe um +
            + valor  e diremos se você conseguiu adivinhar, ou se o nú- +
            + ro  era maior ou menor. Será repetido até acertar ou você +
            + desistir.                                                 +
            +                                                           +
            ++++++++++++++++++++++++++++++ ++++++++++++++++++++++++++++++\n"""))

    def correct_guess(input_value, generated_value):
        msg_correct = "Parabéns! Você acertou o valor corretamente."
        msg_wrong = "Você não acertou"
        msg = msg_correct if input_value == generated_value else msg_wrong
        print(msg)


class Game:
    def input_test(random_integer):
        last_guess = ""
        is_equal_value = False

        while not is_equal_value:
            Utils.refresh_screen()

            print(last_guess)
            input_value = Utils.input_integer("Por favor, informe um valor inteiro: ")

            type_value = "maior" if input_value > random_integer else "menor" 

            last_guess = f"O valor {input_value} informado é {type_value} que o valor informado."
            is_equal_value = input_value == random_integer


    def play_guess_the_number():
        random_integer = random.randint(MINIMUM_VALUE, MAXIMUM_VALUE)
        Game.input_test(random_integer)


def start_program():
    """The main method responsible for starting the program functions."""

    # Displaying the start screen.
    Utils.refresh_screen()

    Game.play_guess_the_number()


def main():
    """The main entrypoint of the application."""
    Utils.retry_loop(start_program)


# Running the main function of the application.
main()
