# ------------------------------------------------------------ #
# Copyright(c) 2026 Vinicius Gabriel Marques de Melo. All rights reserved.
# UFV - UNIVERSIDADE FEDERAL DE VIÇOSA
#
# Subject: CCF 100 - INTRODUÇÃO À PROGRAMAÇÃO
# Script Date: 2026/05/12 10:39
#
# Description:
# Exercício 3 da lista 7 de exercícios de programação.
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

            # Displaying error message if input is wrong.
            if is_wrong_input:
                Utils.refresh_screen()
                # Displaying error message if input is wrong.
                print("""<< Por favor, insira um número válido! >>""")

            try:
                # Retrieving the user input and converting to float and allowing
                # conma as input.
                user_input = float(input(input_text).replace(",", "."))

                return user_input
            except:
                is_wrong_input = True


class Messages:
    def start_screen():
        """Displays the start screen of the application."""
        message = textwrap.dedent(f"""
            =============================================================
            + ANÁLISE DE NOTAS DE ESTUDANTES                            +
            +                                                           +
            + Esse  script fará a análise das notas informadas dos alu- +
            + nos.                                                      +
            +                                                           +
            =============================================================\n""")
        print(message)


def start_program():
    Utils.refresh_screen()

    alumni_amount = Utils.input_integer("Por favor, informe a quantidade de alunos: ")

    grades = []
    for alumni in range(1, alumni_amount + 1):
        grade = Utils.input_numeric(f"Por favor, informe a nota do {alumni}º aluno: ")
        grades.append(grade)

    grade_mean = round(sum(grades) / alumni_amount, 2)

    grade_highest = max(grades)
    grade_lowest = min(grades)

    grades_as_string = ", ".join(list(map(str, grades)))

    message_result = textwrap.dedent(f"""
    = RESULTADO ------------------------------
    = Foram avaliados {alumni_amount} alunos.

    = Notas: "{grades_as_string}"
    = Média da Turma: {grade_mean}

    = Maior Nota: {grade_highest}
    = Menor Nota: {grade_lowest}
    ------------------------------------------
    """)

    print(message_result)


def main():
    """The main entrypoint of the application."""
    Utils.retry_loop(start_program)


# Running the main function of the application.
main()
