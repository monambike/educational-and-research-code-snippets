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
            + SIMULAÇÃO DE FASE DE GRUPOS DA COPA DO MUNDO ⚽           +
            +                                                           +
            + Esse  script fará uma simulação da fase de grupos da copa +
            + do mundo.                                                 +
            +                                                           +
            =============================================================\n""")
        print(message)


class Team:
    score_per_victory = 3
    score_per_draw = 1

    def __init__(self, name, victories, defeats, draws, goals_scored, goals_conceded):
        self.name = name
        self.victories = victories
        self.defeats = defeats
        self.draws = draws
        self.goals_scored = goals_scored
        self.goals_conceded = goals_conceded


    @property
    def games_amount(self):
        return self.victories + self.defeats + self.draws


    @property
    def score(self):
        score = self.victories * Team.score_per_victory + self.draws * Team.score_per_draw

        return score

    def score_calculus_as_string(self):
        return f"({self.victories} vitórias x {Team.score_per_victory} pts) + ({self.draws} empates x {Team.score_per_draw} pts)"


class TeamList(list):
    def to_string(teams: list[Team]):
        string = ""
        for team in teams:
            string += textwrap.dedent(f"""
            "{team.name}" (Jogos Disputados: {team.games_amount})
                Vitórias: {team.victories} / Derrotas: {team.defeats} / Empates: {team.draws}
                Gols Marcados: {team.goals_scored} / Gols Sofridos: {team.goals_conceded}""")
        return string


    def get_highest_score(teams: list[Team]):
        team_highest_score = None
        for team in teams:
            if team_highest_score is None or team_highest_score.score < team.score:
                team_highest_score = team
        return team_highest_score
    
    def get_highest_goal(teams: list[Team]):
        team_highest_goal = None
        for team in teams:
            if team_highest_goal is None or team_highest_goal.score < team.score:
                team_highest_goal = team
        return team_highest_goal

    def get_goals_mean(teams: list[Team]):
        total = 0
        for team in teams:
            total += team.goals_scored
        mean = total / len(teams)
        return mean

    def get_no_defeat(teams: list[Team]):
        no_defeat = 0
        for team in teams:
            if team.defeats == 0:
              no_defeat += 1
        return no_defeat


def start_program():
    Utils.refresh_screen()

    teams = TeamList()

    team_amount = Utils.input_integer("Informe a quantidade de times: ")
    Utils.refresh_screen()

    for team in range(1, team_amount + 1):
        print("> Identificação")
        name = input("Nome: ")
        print()

        print("> Partidas")
        victories = Utils.input_integer("Vitórias: ")
        defeats = Utils.input_integer("Derrotas: ")
        draws = Utils.input_integer("Empates: ")
        print()

        print("> Gols")
        goals_scored = Utils.input_integer("Gols marcados: ")
        goals_conceded = Utils.input_integer("Gols levados: ")

        team = Team(name, victories, defeats, draws, goals_scored, goals_conceded)

        teams.append(team)

        Utils.refresh_screen()


    highest_goal = teams.get_highest_goal()
    highest_score = teams.get_highest_score()
    goals_mean = teams.get_goals_mean()
    no_defeat = teams.get_no_defeat()

    result_message = textwrap.dedent(
f"""--------------- RESULTADO ---------------

DADOS DOS TIMES:

{teams.to_string()}

=========================================

DADOS GERAIS:

Quantidade de Times: {len(teams)}

Time com mais gols marcados:
"{highest_goal.name}"
Gols: {highest_goal.goals_scored}

Time com a maior pontuação:
"{highest_score.name}"
Pontos: {highest_score.score} ({highest_score.score_calculus_as_string()})

Média de Gols: {goals_mean}
Times Sem Derrota: {no_defeat}

--------------- +-+-+-+- ---------------\n""")

    print(result_message)


def main():
    """The main entrypoint of the application."""
    Utils.retry_loop(start_program)


# Running the main function of the application.
main()
