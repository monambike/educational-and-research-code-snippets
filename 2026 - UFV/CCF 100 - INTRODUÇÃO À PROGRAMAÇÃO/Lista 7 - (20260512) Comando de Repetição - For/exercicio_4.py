# ------------------------------------------------------------ #
# Copyright(c) 2026 Vinicius Gabriel Marques de Melo. All rights reserved.
# UFV - UNIVERSIDADE FEDERAL DE VIÇOSA
#
# Subject: CCF 100 - INTRODUÇÃO À PROGRAMAÇÃO
# Script Date: 2026/05/15 00:10
#
# Description:
# Exercício 4 da lista 7 de exercícios de programação.
# ------------------------------------------------------------ #


import platform
import subprocess
import textwrap


PLAYERS = 11
TEAMS = ["A", "B"]


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
                user_input = int(input(input_text) or 0)

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
            + ANÁLISE DE PARTIDA ENTRE OS TIMES "A" E "B"               +
            +                                                           +
            + Esse  script fará a análise de dados de uma partida infor-+
            + mada entre os times "A" e "B"                             +
            +                                                           +
            =============================================================""")
        print(message)


def input_team(team_name):
    foul_amount = 0
    goal_amount = 0

    for player in range(1, PLAYERS + 1):
        Utils.refresh_screen()

        message_team_header = textwrap.dedent(f"""
        --------------- ---------------
        INSERINDO DADOS PARA O TIME "{team_name}"
        --------------- ---------------
        """)
        print(message_team_header)

        print(f"Jogador nº {player:0>2} / {PLAYERS}")
        input_foul_amount = Utils.input_integer("Informe o número de faltas (Pressione Enter para \"0\"): ")
        input_goal_amount = Utils.input_integer("Informe o número de gols (Pressione Enter para \"0\"): ")

        foul_amount += input_foul_amount
        goal_amount += input_goal_amount

    dictionary = { "fouls": foul_amount, "goals": goal_amount }

    return dictionary

def start_program():
    Utils.refresh_screen()

    team_a = input_team("A")
    team_b = input_team("B")

    team_a_fouls = team_a.get("fouls")
    team_b_fouls = team_b.get("fouls")
    team_a_goals = team_a.get("goals")
    team_b_goals = team_b.get("goals")

    Utils.refresh_screen()

    message_result = textwrap.dedent(f"""
       - TABELA DE TIMES -
    | TIME "A"  | TIME "B"  |
    -------------------------
    | Faltas: {team_a_fouls} | Faltas: {team_b_fouls} |
    | Gols:   {team_a_goals} | Gols:   {team_b_goals} |
    """)

    print(message_result)


def main():
    """The main entrypoint of the application."""
    Utils.retry_loop(start_program)


# Running the main function of the application.
main()
