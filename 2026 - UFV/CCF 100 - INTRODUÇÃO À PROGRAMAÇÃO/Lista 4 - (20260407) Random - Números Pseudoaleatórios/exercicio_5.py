# ------------------------------------------------------------ #
# Copyright(c) 2026 Vinicius Gabriel Marques de Melo. All rights reserved.
# UFV - UNIVERSIDADE FEDERAL DE VIÇOSA
#
# Subject: CCF 100 - INTRODUÇÃO À PROGRAMAÇÃO
# Script Date: 2026/04/09 16:01
#
# Description:
# Exercício 5 da lista 4 de exercícios de programação.
# ------------------------------------------------------------ #


import platform
import random
import subprocess
import textwrap


PLAYERS = 3
MAX_STEPS = 30


class Player:
    def __init__(self, name, current_steps = 0):
        self.name = name
        self.current_steps = current_steps


class Messages:
    def start_screen():
        """Displays the start screen of the application."""
        print(textwrap.dedent(f"""
            =============================================================
            - JOGO - CORRIDA MALUCA                                     -
            -                                                           -
            - Entre com {PLAYERS} e disputam uma corrida até que o primeiro jo- -
            - gador consiga atingir {MAX_STEPS} passos!                 -
            -                                                           -
            =============================================================\n"""))


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
                answer = input("Gostaria de jogar novamente?[Y/n]").lower()

                if answer in ("y", ""):
                    break
                elif answer == "n":
                    quit()


def play_and_return_player(players):
    print("\nJOGO INICIADO!! >>>>> >>>>> >>>>> >>>>> >>>>>")

    round_index = 1
    while True:
        print(f"ROUND {round_index}")
        for player in players:
            random_steps = random.randint(1, 10)
            player.current_steps += random_steps

            print(f"Jogador \"{player.name}\" Andou +{random_steps} passos. Total: {player.current_steps}")
            if player.current_steps > MAX_STEPS: return player

        input(f"<< Pressione \"Enter\" para ir ao próximo round >>")
       
        round_index += 1


def start_program():
    Utils.refresh_screen()

    print("CADASTRO DE JOGADORES ------------------------------")
    players = []
    for index_player in range(1, PLAYERS + 1):
        input_name = input(f"Por favor, informe o nome do {index_player} jogador: ")
        player = Player(input_name)
        players.append(player)
    print("----------------------------------------------------")

    winner = play_and_return_player(players)
    print(f"O vencedor é o jogador \"{winner.name}\"!")


def main():
    """The main entrypoint of the application."""
    Utils.retry_loop(start_program)


# Running the main function of the application.
main()
