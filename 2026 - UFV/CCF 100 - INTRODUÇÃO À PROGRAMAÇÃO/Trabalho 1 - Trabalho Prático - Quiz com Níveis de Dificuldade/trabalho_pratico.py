# ------------------------------------------------------------ #
# Copyright(c) 2026 Vinicius Gabriel Marques de Melo. All rights reserved.
# UFV - UNIVERSIDADE FEDERAL DE VIÇOSA
#
# Subject: CCF 100 - INTRODUÇÃO À PROGRAMAÇÃO
# Script Date: 2026/03/07 12:46
#
# Description:
# Trabalho Prático 1 - Quiz com Níveis de Dificuldade, Estruturas Condicionais.
# Desafio: Não pode usar laços nem vetores de forma alguma, sem repetição automática.
# Cada pergunta deve ser # feita individualmente no código.
# ------------------------------------------------------------ #


from enum import Enum
import platform
import random
import subprocess
import textwrap


SCORE_PER_CORRECT_GUESS = 10
SCORE_PER_WRONG = 0
QUESTIONS_QUANTITY = 5


class DifficultyLevel(Enum):
    EASY = 0
    MEDIUM = 1
    HARD = 2


class Option(Enum):
    A = 0
    B = 1
    C = 2


class Utils:
    def clear_terminal() -> None:
      """Clears the terminal based upon the operational system."""
      subprocess.run("cls" if platform.system() == "Windows" else "clear", shell = True)


class Player:
    score = 0
    name = ""
    correct_guesses = 0

    def add_score():
        Player.score += SCORE_PER_CORRECT_GUESS

    def display_score():
        print(f"Jogador: {Player.name} / Pontos Totais: {Player.score}\n{Quiz.last_guess}")


class Difficulty:
    @staticmethod
    def select_difficulty_level():
        message_select_difficulty_level = textwrap.dedent(f"""
            ) )) ))) )))) ))))) )))))) ))))))) )))))))) ))))))))) ))))))))))
            NÍVEL DE DIFICULDADE DO QUIZ

            Por favor {Player.name}, selecione um nível de dificuldade:
            (1) Fácil
            (2) Médio
            (3) Difícil

            Selecionar nível de dificuldade: """)

        result = input(message_select_difficulty_level)
        return result


    @staticmethod
    def return_difficulty_level_as_enum(difficult):
        # Normalizing string
        difficult =  difficult.lower()
        if (difficult == "fácil" or difficult == "facil" or difficult == "1"):
            return DifficultyLevel.EASY
        if (difficult == "médio" or difficult == "medio" or difficult == "2"):
            return DifficultyLevel.MEDIUM
        if (difficult == "difícil" or difficult == "dificil" or difficult == "3"):
            return DifficultyLevel.HARD


    @staticmethod
    def play_difficulty_level(difficult: DifficultyLevel) -> None:
        # Resetting question index on level choice start
        Quiz.question_index = 0

        if (difficult == DifficultyLevel.EASY):
            Quiz.Easy.show_all_questions()
        if (difficult == DifficultyLevel.MEDIUM):
            Quiz.Medium.show_all_questions()
        if (difficult == DifficultyLevel.HARD):
            Quiz.Hard.show_all_questions()


class QuizUtils:
    def get_shuffle_options_position(randomint):
        if (randomint == 1 or randomint == 2):
            return Option.A
        if (randomint == 3 or randomint == 4):
            return Option.B
        if (randomint == 5 or randomint == 6):
            return Option.C

    def get_suffle_options_string(randomint, correct, wrong_1, wrong_2):
        if (randomint == 1):
            option_a = correct
            option_b = wrong_1
            option_c = wrong_2
        if (randomint == 2):
            option_a = correct
            option_b = wrong_2
            option_c = wrong_1
        if (randomint == 3):
            option_a = wrong_1
            option_b = correct
            option_c = wrong_2
        if (randomint == 4):
            option_a = wrong_2
            option_b = correct
            option_c = wrong_1
        if (randomint == 5):
            option_a = wrong_1
            option_b = wrong_2
            option_c = correct
        if (randomint == 6):
            option_a = wrong_2
            option_b = wrong_1
            option_c = correct

        options = textwrap.dedent(f"""
            a) {option_a}
            b) {option_b}
            c) {option_c}""")

        return options

    def return_quiz_option_as_enum(option: str) -> Option:
        # Normalizing string
        option = option.lower()
        if (option.lower() == "a"):
            return Option.A
        if (option.lower() == "b"):
            return Option.B
        if (option.lower() == "c"):
            return Option.C


    def input_option(input_content: str) -> str:
        result = input(input_content)

        if (result != "a" or result != "b" or result != "c"):
            print("Atenção, essa não é uma opção válida! Você não receberá pontos por essa pergunta.")

        return result

    def get_add_score_message(input_content: str, score: int) -> str:
        signal = "+" if score >= 0 else ""
        message = f"[ ({signal}{score} pontos) {input_content}]\n"
        return message


    def show_quiz_header(difficulty_level: DifficultyLevel) -> None:
        difficulty_string = QuizUtils.quiz_difficulty_as_string(difficulty_level).upper()

        msg = f"""--- QUIZ DE DIFICULDADE {difficulty_string} ---"""
        print(msg)

    def quiz_difficulty_as_string(difficulty_level: DifficultyLevel) -> str:
        if (difficulty_level == DifficultyLevel.EASY):
            return "Fácil"
        if (difficulty_level == DifficultyLevel.MEDIUM):
            return "Médio"
        if (difficulty_level == DifficultyLevel.HARD):
            return "Difícil"


class Quiz:
    last_guess = ""
    question_index = 0

    def start_play():
        # Requesting the name
        input_name = input("Por favor, informe o seu nome: ")
        Player.name = input_name

        # Selecting the level of difficulty
        input_difficulty_level = Difficulty.select_difficulty_level()
        difficulty_level = Difficulty.return_difficulty_level_as_enum(input_difficulty_level)

        Difficulty.play_difficulty_level(difficulty_level)

        Utils.clear_terminal()
        QuizUtils.show_quiz_header(difficulty_level)

        print(textwrap.dedent(f"""
            Olá {input_name}, você finalizou o Quiz!
            muito obrigado por jogar.

            Você acertou {Player.correct_guesses}/{QUESTIONS_QUANTITY} perguntas;
            Seu Score final foi de {Player.score} pontos!\n"""))
        input("<< Pressione \"Enter\" para encerrar o programa! >>")


    def build_question(content, options, question_index):
        message = textwrap.dedent(f"""
+ --------------- + --------------- +
Pergunta {question_index}: {content}
{options}
+ --------------- + --------------- +""")
        print(message)

    @staticmethod
    def question(content, answer_correct, difficulty, answer_wrong_1, answer_wrong_2):
        Quiz.question_index += 1

        # Showing the Quiz header per difficulty
        Utils.clear_terminal()

        Player.display_score()
        QuizUtils.show_quiz_header(difficulty)

        # Shuffling the correct options
        random_index = random.randint(1, 6)
        options = QuizUtils.get_suffle_options_string(random_index, answer_correct, answer_wrong_1, answer_wrong_2)
        correct_value = QuizUtils.get_shuffle_options_position(random_index)

        # Building the question
        Quiz.build_question(content, options, Quiz.question_index)

        # Retrieving user input
        user_input = input(f"Reposta: ")

        # Normalizing user input and correct answer for comparison
        user_choosen_option = str(user_input.lower())
        correct_option = correct_value.name.lower()

        correct_question = user_choosen_option == correct_option

        message_guess_correct = QuizUtils.get_add_score_message("Parabéns, Você Acertou!", SCORE_PER_CORRECT_GUESS)
        message_guess_wrong = QuizUtils.get_add_score_message("Infelizmente, Você errou...", 0)

        # Display the message according to result
        if correct_question :
            Quiz.last_guess = message_guess_correct
            Player.add_score()
            Player.correct_guesses += 1
        else:
            Quiz.last_guess = message_guess_wrong

        return correct_question


    class Easy:
        @staticmethod
        def question(content, correct_answer, wrong_answer_1, wrong_answer_2):
            Quiz.question(content, correct_answer, DifficultyLevel.EASY, wrong_answer_1, wrong_answer_2)

        @staticmethod
        def show_all_questions():
            Quiz.Easy.question_1()
            Quiz.Easy.question_2()
            Quiz.Easy.question_3()
            Quiz.Easy.question_4()
            Quiz.Easy.question_5()

        @staticmethod
        def question_1():
            question = "Gatos não gostam que você faça carinho na(s):"
            answer_correct = "Barriga"
            answer_wrong_1 = "Cabeça"
            answer_wrong_2 = "Costas"
            Quiz.Easy.question(question, answer_correct, answer_wrong_1, answer_wrong_2)

        @staticmethod
        def question_2():
            question = "Misturar amarelo e vermelho, dá qual cor?"
            answer_correct = "Laranja"
            answer_wrong_1 = "Verde"
            answer_wrong_2 = "Azul"
            Quiz.Easy.question(question, answer_correct, answer_wrong_1, answer_wrong_2)

        @staticmethod
        def question_3():
            question = "Qual a temperatura de ebulição da água?"
            answer_correct = "100 graus"
            answer_wrong_1 = "10 graus"
            answer_wrong_2 = "80 graus"
            Quiz.Easy.question(question, answer_correct, answer_wrong_1, answer_wrong_2)

        @staticmethod
        def question_4():
            question = "Qual molécula química corresponde à h2o?"
            answer_correct = "Água"
            answer_wrong_1 = "Hidrogênio"
            answer_wrong_2 = "Oxigênio"
            Quiz.Easy.question(question, answer_correct, answer_wrong_1, answer_wrong_2)

        @staticmethod
        def question_5():
            question = "Quanto é 9x4?"
            answer_correct = "36"
            answer_wrong_1 = "45"
            answer_wrong_2 = "54"
            Quiz.Easy.question(question, answer_correct, answer_wrong_1, answer_wrong_2)


    class Medium:
        @staticmethod
        def question(content, correct_answer, wrong_answer_1, wrong_answer_2):
            Quiz.question(content, correct_answer, DifficultyLevel.MEDIUM, wrong_answer_1, wrong_answer_2)

        @staticmethod
        def show_all_questions():
            Quiz.Medium.question_1()
            Quiz.Medium.question_2()
            Quiz.Medium.question_3()
            Quiz.Medium.question_4()
            Quiz.Medium.question_5()

        @staticmethod
        def question_1():
            question = "Qual a raiz quadrada de 81?"
            answer_correct = "9"
            answer_wrong_1 = "27"
            answer_wrong_2 = "3"
            Quiz.Medium.question(question, answer_correct, answer_wrong_1, answer_wrong_2)

        @staticmethod
        def question_2():
            question = "Para descobrir o \"x\" em funções de segundo grau, usa-se:"
            answer_correct = "Fórmula de Bháskara"
            answer_wrong_1 = "Pitágoras"
            answer_wrong_2 = "Teorema de Tales"
            Quiz.Medium.question(question, answer_correct, answer_wrong_1, answer_wrong_2)

        @staticmethod
        def question_3():
            question = "Em qual continente fica o Egito?"
            answer_correct = "Africano"
            answer_wrong_1 = "Europeu"
            answer_wrong_2 = "Asiático"
            Quiz.Medium.question(question, answer_correct, answer_wrong_1, answer_wrong_2)

        @staticmethod
        def question_4():
            question = "Qual empresa é dona do WhatsApp?"
            answer_correct = "Meta"
            answer_wrong_1 = "Google"
            answer_wrong_2 = "WhatsApp é uma empresa independente"
            Quiz.Medium.question(question, answer_correct, answer_wrong_1, answer_wrong_2)

        @staticmethod
        def question_5():
            question = "Gatos trazem animais mortos aos donos pois querem:"
            answer_correct = "Trazer presentes e demonstrar afeto"
            answer_wrong_1 = "Pagar o aluguel"
            answer_wrong_2 = "Ver o circo pegar fogo"
            Quiz.Medium.question(question, answer_correct, answer_wrong_1, answer_wrong_2)


    class Hard:
        @staticmethod
        def question(content, correct_answer, wrong_answer_1, wrong_answer_2):
            Quiz.question(content, correct_answer, DifficultyLevel.HARD, wrong_answer_1, wrong_answer_2)

        @staticmethod
        def show_all_questions():
            Quiz.Hard.question_1()
            Quiz.Hard.question_2()
            Quiz.Hard.question_3()
            Quiz.Hard.question_4()
            Quiz.Hard.question_5()

        @staticmethod
        def question_1():
            question = "Em que ano terminou a segunda guerra mundial?"
            answer_correct = "1945"
            answer_wrong_1 = "1939"
            answer_wrong_2 = "1947"
            Quiz.Hard.question(question, answer_correct, answer_wrong_1, answer_wrong_2)

        @staticmethod
        def question_2():
            question = "Qual valor de PI com 4 casas decimais?"
            answer_correct = "3,1415"
            answer_wrong_1 = "3,1414"
            answer_wrong_2 = "3,1416"
            Quiz.Hard.question(question, answer_correct, answer_wrong_1, answer_wrong_2)

        @staticmethod
        def question_3():
            question = "Qual a raça de gato que nasce sem pelos?"
            answer_correct = "Sphynx"
            answer_wrong_1 = "Siamês"
            answer_wrong_2 = "Persa"
            Quiz.Hard.question(question, answer_correct, answer_wrong_1, answer_wrong_2)

        @staticmethod
        def question_4():
            question = "Qual é o metal que fica líquido em temperatura ambiente?"
            answer_correct = "Mercúrio"
            answer_wrong_1 = "Frâncio"
            answer_wrong_2 = "Tungstênio"
            Quiz.Hard.question(question, answer_correct, answer_wrong_1, answer_wrong_2)

        @staticmethod
        def question_5():
            question = "Qual o único número primo par?"
            answer_correct = "2"
            answer_wrong_1 = "0"
            answer_wrong_2 = "-2"
            Quiz.Hard.question(question, answer_correct, answer_wrong_1, answer_wrong_2)


def main():
    Utils.clear_terminal()

    Quiz.start_play()


main()
