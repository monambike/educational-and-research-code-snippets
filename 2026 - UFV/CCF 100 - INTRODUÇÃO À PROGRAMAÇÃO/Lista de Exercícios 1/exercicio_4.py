# ------------------------------------------------------------ #
# Copyright(c) 2026 Vinicius Gabriel Marques de Melo. All rights reserved.
# UFV - UNIVERSIDADE FEDERAL DE VIÇOSA
#
# Subject: CCF 100 - INTRODUÇÃO À PROGRAMAÇÃO
# Script Date: 2026/03/21 17:20
#
# Description:
# Exercício 4 da lista 1 de exercícios de programação.
# ------------------------------------------------------------ #

import platform
import subprocess
import textwrap


def clear_terminal() -> None:
    """Clears the terminal based upon the operational system."""
    subprocess.run("cls" if platform.system() == "Windows" else "clear", shell = True)


def show_start_screen() -> None:
    """Shows start screen explaining script usage."""

    # Contextualizing the script for the user.
    print(textwrap.dedent(f"""
    <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<  >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
                         CALCULADORA DE JUROS
    $ % / $ % / $ % / $ % / $ % / $ % / $ % / $ % / $ % / $ % / $
    O  cálculo  de  juros é dado por "M = C x (1 + i)^t", onde "P"
    é  o valor principal, "i" é a taxa de juros e "t" é o tempo em
    anos.
    
    Por  favor,  informe  o valor da parcela, a taxa de juros para
    que seja feito o cálculo dos juros.
    <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<  >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\n"""))


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

        clear_terminal()

        # Displaying header explaining the user input.
        show_start_screen()

        # Displaying error message if input is wrong.
        if is_wrong_input:
            print("""<< Por favor, insira um número válido! >>""")

        try:
            # Retrieving the user input and converting to float and allowing
            # conma as input.
            user_input = float(input(input_text).replace(",", "."))
        except:
            is_wrong_input = True

        # If user already input a correct number, exits the function.
        if isinstance(user_input, (int, float)):
            return user_input


def calculate_interest(installment: float, interest_rate: float, total_months: int = 12) -> None:
    final_text = []

    print("\nValores das Parcelas (de acordo com o mês):")

    columns = 3
    lines = int(total_months / columns)
    for month_index in range(1, total_months + 1):
        line_index = 0

        # M = C x (1 + i) ^ t
        result = installment * (1 + interest_rate) ** month_index
        final_text.insert(month_index - 1, f"{month_index:02}º mês: {result:.2f}")

        if month_index % columns == 0:
            line_index += 1

    for line_index in range(lines):
        print(" | ".join(final_text[line_index*columns:(line_index+1)*columns]))

    print(textwrap.dedent(f"""
        Valor da Parcela: {installment}
        Juros Calculado: {interest_rate}\n"""))


def main():
    while True:
        installment = input_numeric("Valor da Parcela: ")
        interest_rate = input_numeric("Valor da Taxa de Juros: ")
            
        calculate_interest(installment, interest_rate)
        
        while True:
            answer = input("Você gostaria de fazer outra operação?[Y/n]").lower()

            if answer in ("y", ""):
                break
            elif answer == "n":
                quit()


main()
