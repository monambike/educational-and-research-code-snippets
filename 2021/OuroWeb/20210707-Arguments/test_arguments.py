import argparse
import os
# -------------------------------------------------------------
# Bibliotecas





# LIMPA O TERMINAL
# -------------------------------------------------------------
# Descrição:
# Limpa o terminal
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>> <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
os.system("cls")
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>> <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
# -------------------------------------------------------------



# Criando parser
mainParser = argparse.ArgumentParser(allow_abbrev=False)
# ARGUMENTOS UTILIZADOS NO PARSER
# -------------------------------------------------------------
# Descrição:
# Aqui estão dispostos os argumentos que vão ser passados  para
# o parser mais tarde
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>> <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
# Argumento que conterá o caminho de importação (Obrigatório)
mainParser.add_argument(
    "--importPath",
    required = True,
    type = str
)
# Argumento que conterá o caminho de exportação (Opcional)
mainParser.add_argument(
    "--exportPath",
    required = False,
    type = str
)
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>> <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
# -------------------------------------------------------------

# Adiciona os argumentos informados anteriormente na região an-
# terior ao parser
args = mainParser.parse_args()


# Exibe o título do log para o usuário
print(
    "------------------------------\n"
    "      LOG DE INFORMAÇÕES\n"
    "------------------------------\n"
    "\n"
    "\n"
)


# VALIDAÇÃO DE DIRETÓRIO DE IMPORTAÇÃO
# -------------------------------------------------------------
# Descrição:
# Condicional que realiza a validação do diretório de  importa-
# ção
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>> <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
resultImportValidation = ""
# Se não existe
if (not os.path.isdir(args.importPath)):
    # Concatena mensagem
    resultImportValidation = "não "
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>> <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
# -------------------------------------------------------------



# VALIDAÇÃO DE DIRETÓRIO DE EXPORTAÇÃO
# -------------------------------------------------------------
# Descrição:
# Condicional que realiza a validação do diretório de  exporta-
# ção, caso o usuário a tenha informado.
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>> <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
resultExportValidation = ""
# Caso o usuário tenha informado o caminho de exportação
if (args.exportPath != None):
    # E caso o diretório não exista
    if (not os.path.isdir(args.exportPath)):
        # Concatena o "não" com espaço,  à variável
        resultExportValidation = "não "

    # Sempre concatena o "existe" à variável e sempre mostra  o
    # caminho que o usuário digitou
    resultExportValidation += (
        "existe\n"
        "caminho: '" + args.exportPath + "'"
    )
else:
    # afirma que o diretório de exportação não foi informado
    resultExportValidation = "não foi informado"
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>> <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
# -------------------------------------------------------------



# Exibe mensagem final para o usuário
print(
    "[OBRIGATÓRIO]\n"
    "Diretório de importação " + resultImportValidation + "foi encontrado\n"
    "caminho: '" + args.importPath + "'\n"
    "\n"
    "[OPCIONAL]\n"
    "Diretório de exportação " + resultExportValidation + ""
)