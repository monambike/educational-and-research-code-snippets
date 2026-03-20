# ------------------------------------------------------------
# Copyright(c) 2026 Vinicius Gabriel Marques de Melo. All rights reserved.
# UFV - UNIVERSIDADE FEDERAL DE VIÇOSA
#
# Subject: CCF 100 - INTRODUÇÃO À PROGRAMAÇÃO
# Script Date: 2026/03/20 18:02
#
# Description:
# Exercício 2 da lista 1 de exercícios de programação.
# ------------------------------------------------------------

import subprocess
import platform


def clear_terminal() -> None:
    subprocess.run("cls" if platform.system() == "Windows" else "clear", shell = True)
    
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

print("Cálculo da área de um retângulo.\n")
base = input("Valor da Base:")
height = input("Valor da Altura:")

print("Cálculo da área de um triângulo.\n")
base = input("Valor da Base:")
height = input("Valor da Altura:")

print("Cálculo da área de uma circunferência.\n")
radius = input("Valor do Raio: ")
