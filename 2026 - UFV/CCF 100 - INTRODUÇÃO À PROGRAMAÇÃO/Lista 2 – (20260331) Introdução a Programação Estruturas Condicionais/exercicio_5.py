# ------------------------------------------------------------ #
# Copyright(c) 2026 Vinicius Gabriel Marques de Melo. All rights reserved.
# UFV - UNIVERSIDADE FEDERAL DE VIÇOSA
#
# Subject: CCF 100 - INTRODUÇÃO À PROGRAMAÇÃO
# Script Date: 2026/03/24 13:43
#
# Description:
# Exercício 5 da lista 2 de exercícios de programação.
# ------------------------------------------------------------ #


import platform
import subprocess
import textwrap
from enum import Enum


class Gender(Enum):
    MAN = 0
    WOMAN = 1


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


def show_start_screen() -> None:
    """Displays the start screen of the application."""
    print(textwrap.dedent("""
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^
    CALCULADORA DE PESO IDEAL PARA HOMENS E MULHERES
    BASEADO NO IMC

    Será solicitado o gênero e a altura do usuário. Então, o pro-
    grama  calculará  o peso ideal baseado no IMC e exibirá o re-
    sultado.
    ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^\n"""))


def calc_BMI(height, constant_a, constant_b) -> float:
    """General formula of BMI calculation.

    Args:
        height (float): The height of the person in meters.
        constant_a (float): The constant A used in BMI formula.
        constant_b (float): The constant B used in BMI formula.

    Returns:
        float: The calculated ideal weight.
    """
    return constant_a * height - constant_b


def calc_BMI_man(height) -> float:
    """Calculate BMI for male individuals.

    Args:
        height (float): The height of the person in meters.

    Returns:
        float: The calculated ideal weight for male individuals.
    """
    return calc_BMI(72.7, height, 58)


def calc_BMI_woman(height) -> float:
    """Calculate BMI for female individuals.

    Args:
        height (float): The height of the person in meters.

    Returns:
        float: The calculated ideal weight for female individuals.
    """
    return calc_BMI(62.1, height, 44.7)


def input_gender():
    while True:
        input_gender = input("Por favor, informe seu gênero (m) masculino/(f) feminino): ")

        gender = retrieve_gender(input_gender)

        if gender is not None:
            return gender

        print("""<< Por favor, insira um gênero válido! >>""")


def retrieve_gender(gender: str) -> Gender:
    match gender.lower():
        case "m" | "masculino" | "homem" | "menino" | "garoto":
            return Gender.MAN
        case "f" | "feminino" | "mulher" | "menina" | "garota":
            return Gender.WOMAN
        case _:
            return None


def gender_as_string_portuguese(gender: Gender) -> str:
    """Returns the provided gender as string in portuguese.

    Args:
        gender (Gender): The gender.

    Returns:
        str: The gender as string in portuguese.
    """
    match gender:
        case Gender.MAN:
            return "Masculino"
        case Gender.WOMAN:
            return "Feminino"


def start_program():
    """The main entrypoint of the application."""
    
    refresh_screen()

    # Retrieving the user input for gender.
    gender = input_gender()

    # Retrieving the user input for height.
    input_height = input_numeric("Por favor, informe sua altura: ")

    # Converting height to meters if the input is in centimeters.
    height = input_height / 100 if input_height > 3 else input_height 

    result = 0
    # Performing the calculation based on the gender.
    match gender:
        case Gender.MAN:
            result = calc_BMI_man(height)
        case Gender.WOMAN:
            result = calc_BMI_woman(height)

    # Converting the gender as string portuguese for display.
    string_gender = gender_as_string_portuguese(gender)

    # Displaying the result.
    print(textwrap.dedent(f"""
    Baseado na Escolha de Gênero \"{string_gender}\" e Altura \"{height}m\",
    Seu peso ideal seria: {result}kg de acordo com o IMC"""))


def main():
    """The main entrypoint of the application."""
    retry_loop(start_program)


# Running the main function of the application.
main()
