# ------------------------------------------------------------ #
# Copyright(c) 2026 Vinicius Gabriel Marques de Melo. All rights reserved.
# UFV - UNIVERSIDADE FEDERAL DE VIÇOSA
#
# Subject: CCF 100 - INTRODUÇÃO À PROGRAMAÇÃO
# Script Date: 2026/03/20 18:02
#
# Description:
# Exercício 2 da lista 1 de exercícios de programação.
# ------------------------------------------------------------ #

import platform
import subprocess
import textwrap


def clear_terminal() -> None:
    """Clears the terminal based upon the operational system."""
    subprocess.run("cls" if platform.system() == "Windows" else "clear", shell = True)


def show_start_screen() -> None:
    """Shows start screen explaining script usage."""

    print(textwrap.dedent("""
    ------------------------------------------------------------
                   CÁLCULO DE FIGURAS GEOMÉTRICAS
    ------------------------------------------------------------

    Esse  programa  fará  o cálculo de figuras geométricas, como
    retângulo, triângulo e circunferência.
    
    Serão solicitados os dados necessários para o cálculo de ca-
    da figura geométrica respectivamente.
    ------------------------------------------------------------\n"""))


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


def calculate_area_rectangle(base, height):
    # Área do retângulo = Base x Altura;
    result = base * height
    return result


def calculate_area_triangle(base, height):
    # Área do triângulo = (Base x Altura)/2;
    result = (base * height) / 2
    return result


def calculate_area_circle(radius):
    CONST_PI = 3.1415
    # Área da circunferência = π x Raio2
    result = CONST_PI * radius / 2
    return result


def calculate_all_geometric_shapes():
    header_rectangle = "Cálculo da área de um retângulo. Área = Base x Altura\n"
    base_text = "Valor da Base: "
    base = input_numeric(f"{header_rectangle}{base_text}")
    height_text = "Valor da Altura: "
    height = input_numeric(f"{header_rectangle}{height_text}")
    print(f"\n{base_text}{base}, {height_text}{height}")
    print("Resultado: ", calculate_area_rectangle(base, height))
    input("Pressione Enter para continuar...")

    header_triangle = "Cálculo da área de um triângulo. Área = (Base x Altura)/2\n"
    base_text = "Valor da Base: "
    base = input_numeric(header_triangle + base_text)
    height_text = "Valor da Altura: "
    height = input_numeric(header_triangle + height_text)
    print(f"\n{base_text}{base}, {height_text}{height}")
    print("Resultado: ", calculate_area_triangle(base, height))
    input("Pressione Enter para continuar...")

    header_circle = "Cálculo da área de uma circunferência. Área = π x Raio²3\n"
    radius_text = "Valor do Raio: "
    radius = input_numeric(header_circle + radius_text)
    print(f"\n{radius_text}{radius}")
    print("Resultado: ", calculate_area_circle(radius))
    input("Pressione Enter para continuar...")


def main():
    while True:
        result = calculate_all_geometric_shapes()

        # Format the result to replace dot with comma allowing more inputs.
        formatted_result = str(result).replace(".", ",")

        print(f"O resultado se dá por: \"{formatted_result}\".\n\n")
        
        while True:
            answer = input("Você gostaria de fazer outra operação?[Y/n]").lower()

            if answer in ("y", ""):
                break
            elif answer == "n":
                quit()


main()
