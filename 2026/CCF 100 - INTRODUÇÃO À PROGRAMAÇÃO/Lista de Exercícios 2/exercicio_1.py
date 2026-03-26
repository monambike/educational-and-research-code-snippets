# ------------------------------------------------------------ #
# Copyright(c) 2026 Vinicius Gabriel Marques de Melo. All rights reserved.
# UFV - UNIVERSIDADE FEDERAL DE VIÇOSA
#
# Subject: CCF 100 - INTRODUÇÃO À PROGRAMAÇÃO
# Script Date: 2026/03/24 10:30
#
# Description:
# Exercício 1 da lista 2 de exercícios de programação.
# ------------------------------------------------------------ #


import platform
import subprocess
import textwrap


CONST_ASSESSMENT_QUANTITY = 5


class Assessment:
    def __init__(self, index: str, score: float) -> None:
        self.index = index
        self.score = score
        
        self.approved = self.is_approved(self.score)


    @staticmethod
    def is_approved(score: float) -> bool:
        """Checks if the assessment is approved based on the score.

        Args:
            score (float): The assessment's score."""
        return score >= 60


    @staticmethod
    def approval_as_string(approved: bool):
        return "Aprovado" if approved else "Reprovado"


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
        ++++++++++++++++++++++++++++++ ++++++++++++++++++++++++++++++
        + CALCULADORA DE MÉDIAS DE AVALIAÇÕES                       +
        +                                                           +
        + O valor da nota é de 0 até 100. Devem ser informadas {CONST_ASSESSMENT_QUANTITY} no-+
        + tas de avaliações.                                        +
        + Com  base nas notas serão disponibilizadas o status de a- +
        + provação  individual e então será calculada a média final +
        + e o status de aprovação geral.                            +
        ++++++++++++++++++++++++++++++ ++++++++++++++++++++++++++++++\n"""))


def input_assessments() -> Assessment:
    assessments = []
    for assessment_index in range(1, CONST_ASSESSMENT_QUANTITY + 1):
        score_input = input_numeric(f"Informe o {assessment_index}º Valor: ")

        assessment = Assessment(assessment_index, score_input)

        assessments.append(assessment)

    return assessments


def show_assessments_means(assessments: [Assessment]):
    print(textwrap.dedent("""
    + ------------------------------ +

    Esses são os valores das notas e status de aprovações individuais conforme valores fornecidos:\n"""))

    for assessment in assessments:
        print(f"{assessment.index}º avaliação: {assessment.score} - {Assessment.approval_as_string(assessment.approved)}")


def start_program():
    """The main method responsible for starting the program functions."""

    # Displaying the start screen.
    refresh_screen()

    # Asking the input of the assessments and storing them in a list.
    assessments = input_assessments()

    # Displaying the assessments and their means.
    show_assessments_means(assessments)

    # Calculating the mean of the assessments and checking if the student
    # is approved by the mean.
    mean = sum(assessment.score for assessment in assessments) / len(assessments)
    approved_by_mean = Assessment.is_approved(mean)

    # Displaying the mean and the approval by mean.
    print(f"\nO Cálculo da Média Geral {mean} / Aluno: {Assessment.approval_as_string(approved_by_mean)}\n")


def main():
    """The main entrypoint of the application."""
    retry_loop(start_program)


# Running the main function of the application.
main()
