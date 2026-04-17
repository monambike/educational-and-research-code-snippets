# ------------------------------------------------------------ #
# Copyright(c) 2026 Vinicius Gabriel Marques de Melo. All rights reserved.
# UFV - UNIVERSIDADE FEDERAL DE VIÇOSA
#
# Subject: CCF 100 - INTRODUÇÃO À PROGRAMAÇÃO
# Script Date: 2026/04/06 16:43
#
# Description:
# Exercício 2 da lista 3 de exercícios de programação.
# ------------------------------------------------------------ #


from enum import Enum
import platform
import subprocess
import textwrap


MINIMUM_AGE_MAN = 65
MINIMUM_AGE_WOMAN = 60

MINIMUM_WORKTIME_MAN = 30
MINIMUM_WORKTIME_WOMAN = 25


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
            refresh_screen()
            # Displaying error message if input is wrong.
            print("""<< Por favor, insira um número válido! >>""")


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
        + AVALIADOR DE POSSIBILIDADE DE APOSENTADORIA               +
        +                                                           +
        + Esse  programa  fará uma avaliação para verificar se você +
        + tem direito à aposentadoria.                              +
        +                                                           +
        + Masculino - Idade Mínima: 65 anos / Tempo de Con. 30 anos +
        + Feminino  - Idade Mínima: 60 anos / Tempo de Con. 25 anos +
        +                                                           +
        ++++++++++++++++++++++++++++++ ++++++++++++++++++++++++++++++\n"""))


def error_validate_age_message(gender, minimum_age):
    gender_as_string = gender_as_string_portuguese(gender)
    message = f"É necessário ter pelo menos {minimum_age} anos para aposentar sendo do sexo \"{gender_as_string}\"."
    print(message)


def error_validate_work_time_message(gender, work_time):
    gender_as_string = gender_as_string_portuguese(gender)
    message = f"É *necessário ter pelo menos {work_time} anos de tempo de contribuição para aposentar sendo do sexo \"{gender_as_string}\"."
    print(message)


def success_validate_retirement():
    print("Sua aposentadoria foi validada com êxito! Você pode se aposentar.")


def retirement_message(age, gender, work_time):
    if (gender is Gender.MAN):
        # Validate age
        if (age >= MINIMUM_AGE_MAN):
            # Validate work time
            if (work_time >= MINIMUM_WORKTIME_MAN):
                return success_validate_retirement()
            else:
                error_validate_work_time_message(gender, MINIMUM_WORKTIME_MAN)
        else:
            error_validate_age_message(gender, MINIMUM_AGE_MAN)
    elif (gender is Gender.WOMAN):
        # Validate age
        if (age >= MINIMUM_AGE_WOMAN):
            # Validate work time
            if (work_time >= MINIMUM_WORKTIME_WOMAN):
                return success_validate_retirement()
            else:
                error_validate_work_time_message(gender, MINIMUM_WORKTIME_WOMAN)
        else:
            error_validate_age_message(gender, MINIMUM_AGE_WOMAN)


def start_program():
    """The main method responsible for starting the program functions."""

    # Displaying the start screen.
    refresh_screen()

    gender = input_gender()

    age = input_integer("Por favor, informe a sua idade: ")

    workTime = input_numeric("Por favor, informe o seu tempo de contribuição: ")

    retirement_message(age, gender, workTime)


def main():
    """The main entrypoint of the application."""
    retry_loop(start_program)


# Running the main function of the application.
main()
