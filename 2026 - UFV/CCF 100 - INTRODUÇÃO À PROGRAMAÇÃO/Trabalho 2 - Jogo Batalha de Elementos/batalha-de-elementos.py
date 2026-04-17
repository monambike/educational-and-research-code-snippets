# ------------------------------------------------------------ #
# Copyright(c) 2026 Vinicius Gabriel Marques de Melo. All rights reserved.
# UFV - UNIVERSIDADE FEDERAL DE VIÇOSA
#
# Subject: CCF 100 - INTRODUÇÃO À PROGRAMAÇÃO
# Script Date: 2026/03/07 12:46

# Description:
# Desenvolvimento de um jogo semelhante ao Pedra, Panel e Tesoura
# mas com 5 elementos. Fogo, água, planta, raio e pedra.
# ------------------------------------------------------------ #


from colorama import Fore, Back, Style, init
from enum import Enum
import platform
import random
import subprocess
import textwrap
import time


class Players(Enum):
    PLAYER_1 = 0
    PLAYER_2 = 1


class BattleResult(Enum):
    VICTORY = 0
    DEFEAT = 1
    DRAW = 2


class ElementType(Enum):
    FIRE = 1
    WATER = 2
    PLANT = 3
    THUNDER = 4
    ROCK = 5


class Element:
    def __init__(self, elementType: ElementType, winners: list[ElementType], losers: list[ElementType], label):
        self.wins_to = winners
        self.loses_to = losers
        self.elementType = elementType
        self.label = Style.BRIGHT + label + Style.RESET_ALL

    @staticmethod
    def get_element_by_element_type(elementType: ElementType) -> Element | None:
        for element in Elements.elements:
            if element.elementType == elementType: return element
        return None

    @staticmethod
    def get_random_element():
        result = random.choice(Elements.elements)
        return result

    @staticmethod
    def element_type_choice() -> ElementType:
        while True:
            player1_input_element = input(Utils.player_speech("Por favor escolha seu elemento: ", Players.PLAYER_1))

            try:
                player1_input_element_int = int(player1_input_element)
                element_type = ElementType(player1_input_element_int)

                return element_type
            except:
                print("<< Por favor, selecione uma opção válida! >>")

    @staticmethod
    def check_player1_won_player2(player1_element: Element, player2_element: Element) -> BattleResult:
        if player1_element.elementType in player2_element.wins_to:
            return BattleResult.DEFEAT
        if player1_element.elementType in player2_element.loses_to:
            return BattleResult.VICTORY
        if player1_element.elementType == player1_element.elementType:
            return BattleResult.DRAW

    @staticmethod
    def battle_result_as_string(battle_result: BattleResult):
        match(battle_result):
            case BattleResult.VICTORY:
                return "Vitória"
            case BattleResult.DEFEAT:
                return "Derrota"
            case BattleResult.DRAW:
                return "Empate"

    @staticmethod
    def element_type_as_string(element_type: ElementType):
        match(element_type):
            case ElementType.FIRE:
                return Elements.fire.label
            case ElementType.WATER:
                return Elements.water.label
            case ElementType.PLANT:
                return Elements.plant.label
            case ElementType.THUNDER:
                return Elements.thunder.label
            case ElementType.ROCK:
                return Elements.rock.label

    @staticmethod
    def battle_result_description_as_string(battle_result):
        match(battle_result):
            case BattleResult.VICTORY: 
                return "Parabéns você venceu! 👏🥳🎉"
            case BattleResult.DEFEAT:
                return "Que pena... Você perdeu... 😔🥀"
            case BattleResult.DRAW:
                return "Deu empate! Caramba, ninguém ganhou... 😬😦"


class Elements:
    fire = Element(ElementType.FIRE,
      winners=[ElementType.PLANT, ElementType.ROCK],
      losers=[ElementType.WATER, ElementType.THUNDER],
      label=(Fore.RED + "🔥 Fogo"))
    
    water = Element(ElementType.WATER,
      winners=[ElementType.FIRE, ElementType.ROCK],
      losers=[ElementType.PLANT, ElementType.THUNDER],
      label=(Fore.BLUE + "🫗  Água"))
    
    plant = Element(ElementType.PLANT,
      winners=[ElementType.WATER, ElementType.THUNDER],
      losers=[ElementType.FIRE, ElementType.ROCK],
      label=(Fore.GREEN + "🌿 Planta"))
    
    thunder = Element(ElementType.THUNDER,
      winners=[ElementType.WATER, ElementType.FIRE],
      losers=[ElementType.PLANT, ElementType.ROCK],
      label=(Fore.YELLOW + "⚡ Raio"))
    
    rock = Element(ElementType.ROCK,
      winners=[ElementType.THUNDER, ElementType.PLANT],
      losers=[ElementType.WATER, ElementType.FIRE],
      label=(Fore.WHITE + "🪨  Pedra"))

    elements = [fire, water, plant, thunder, rock]


class Utils:
    @staticmethod
    def clear_terminal() -> None:
        """Clears the terminal based upon the operational system."""
        subprocess.run("cls" if platform.system() == "Windows" else "clear", shell = True)


    @staticmethod
    def show_start_screen():
        """Displays the start screen of the application."""
        text = f"""
            ++++++++++++++++++++++++++++++++++  ++++++++++++++++++++++++++++++++++
            +                     << BATALHA DE ELEMENTOS >>                     +
            +                                                                    +
            + Esse é um jogo "pedra, papel e tesoura" mas que conta com          +
            + cinco (5) elementos!                                               +
            +                                                                    +
            + Regras:                                                            +
            +                                                                    +
            + | ELEMENTO      VENCE                     PERDE                 |  +
            + ------------------------------------------------------------------ +
            + | {Elements.fire.label}      {Elements.plant.label}  | {Elements.rock.label}      {Elements.water.label}    | {Elements.thunder.label}  |  +
            + | {Elements.water.label}      {Elements.fire.label}    | {Elements.rock.label}      {Elements.plant.label}  | {Elements.thunder.label}  |  +
            + | {Elements.plant.label}    {Elements.water.label}    | {Elements.thunder.label}       {Elements.fire.label}    | {Elements.rock.label} |  +
            + | {Elements.thunder.label}      {Elements.water.label}    | {Elements.fire.label}       {Elements.plant.label}  | {Elements.rock.label} |  +
            + | {Elements.rock.label}     {Elements.thunder.label}    | {Elements.plant.label}     {Elements.water.label}    | {Elements.fire.label}  |  +
            +                                                                    +
            ++++++++++++++++++++++++++++++++++  ++++++++++++++++++++++++++++++++++\n"""
        print(textwrap.dedent(text))

    @staticmethod
    def show_elements_choice_screen():
        """Displays the element choice screen."""
        print(textwrap.dedent(f"""
        ------------------------------------------------------------
        LISTA DE ELEMENTOS DISPONÍVEIS                                 
        Lista de elementos disponível para escolha no jogo.            
                                                                      
        1: {Elements.fire.label}          | 2: {Elements.water.label}  
        3: {Elements.plant.label}        | 4: {Elements.thunder.label} 
        5: {Elements.rock.label}                                       
        ------------------------------------------------------------\n"""))

    @staticmethod
    def show_results_screen(player1_element, player2_element):
        battle_result = Element.check_player1_won_player2(player1_element, player2_element)
        battle_result_description_string = Element.battle_result_description_as_string(battle_result)

        battle_result_string = Element.battle_result_as_string(battle_result)
        player1_element_type_string = Element.element_type_as_string(player1_element.elementType)
        player2_element_type_string = Element.element_type_as_string(player2_element.elementType)

        print(textwrap.dedent(f"""
              ------------------------------------------------------------
              Jogador 1: {player1_element_type_string}
              Jogador 2: {player2_element_type_string}

              RESULTADO: {battle_result_string}
              {battle_result_description_string}
              ------------------------------------------------------------"""))

    @staticmethod
    def refresh_screen():
        """Clears the terminal and displays the start screen of the application."""
        Utils.clear_terminal()

        Utils.show_start_screen()

    @staticmethod
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

    @staticmethod
    def player_speech(message, player):
        match(player):
            case Players.PLAYER_1:
                foreground_color = Fore.BLUE
                player_name_tag = "(Jogador 1)"
            case Players.PLAYER_2:
                foreground_color = Fore.RED
                player_name_tag = "(Jogador 2)"

        # Styling the player tag name
        styled_player_tag = Style.BRIGHT + foreground_color + player_name_tag + Style.RESET_ALL

        # Putting together and styling the final message
        styled_message = styled_player_tag + Style.RESET_ALL + foreground_color + f" {message}" + Style.RESET_ALL

        return styled_message


def start_program():
    """The main method responsible for starting the program functions."""

    Utils.refresh_screen()
    Utils.show_elements_choice_screen()

    print(textwrap.dedent("""
        > >> >>> >>>> >>>>> >>>>>> >>>>>>> >>>>>>>> >>>>>>>>> >>>>>>>>>>
        EM JOGO - JOGO INICIADO
    """))
    init(autoreset=True)  # Automatically resets style after each print)

    player1_element_type = Element.element_type_choice()
    player1_element = Element.get_element_by_element_type(player1_element_type)
    print(Utils.player_speech("Escolheu sua jogada!", Players.PLAYER_1))

    time.sleep(2)
    print(Utils.player_speech("Por favor escolha seu elemento:", Players.PLAYER_2))
    print(Utils.player_speech("Está escolhendo seu elemento... ", Players.PLAYER_2))
    player2_element = Element.get_random_element()
    time.sleep(2)
    print(Utils.player_speech("Escolheu sua jogada!", Players.PLAYER_2))

    print("\nVamos conferir os resultados!")
    input("<< Pressione \"Enter\" para continuar... >>")

    Utils.show_results_screen(player1_element, player2_element)


def main():
    """The main entrypoint of the application."""
    Utils.retry_loop(start_program)


# Running the main function of the application.
main()
