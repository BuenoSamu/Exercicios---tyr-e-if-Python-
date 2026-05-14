# ============================================================
# LISTONA PRINCIPAL
#
# FINALIDADE:
# Guardar várias disciplinas.
#
# CADA LISTINHA POSSUI:
#
# [0] -> Nome da disciplina
# [1] -> Nota
# [2] -> Frequência
# ============================================================

registro_de_disciplina = [

    ["Matemática", 8.5, 0.90],
    ["Português", 7.0, 0.85],
    ["História", 9.2, 0.95],
    ["Física", 6.5, 0.80],
    ["Química", 5.0, 0.75]
]



# ============================================================
# FUNÇÃO: adicionar_registro_em_posicao()
#
# FINALIDADE:
# Permitir que o usuário escolha
# em qual posição deseja inserir
# um novo registro.
#
# FUNCIONAMENTO:
#
# 1. Mostra os registros atuais.
# 2. Pergunta os dados da nova disciplina.
# 3. Pergunta a posição desejada.
# 4. Insere o novo registro na posição escolhida.
# ============================================================

def adicionar_registro_em_posicao(lista):


    # --------------------------------------------------------
    # MOSTRAR A LISTA ATUAL
    #
    # FINALIDADE:
    # Mostrar ao usuário as posições existentes.
    # --------------------------------------------------------
    print("\nLISTA ATUAL:\n")


    # --------------------------------------------------------
    # CONTADOR
    #
    # FINALIDADE:
    # Percorrer a listona.
    # --------------------------------------------------------
    i = 0


    # --------------------------------------------------------
    # LOOP PARA MOSTRAR OS REGISTROS
    # --------------------------------------------------------
    while i < len(lista):


        # ----------------------------------------------------
        # Exibe:
        #
        # posição -> registro
        # ----------------------------------------------------
        print(i, "->", lista[i])


        # ----------------------------------------------------
        # Incrementa o contador.
        # ----------------------------------------------------
        i += 1


    # --------------------------------------------------------
    # CADASTRO DO NOVO REGISTRO
    # --------------------------------------------------------

    print("\nNOVO REGISTRO:\n")


    # --------------------------------------------------------
    # input()
    #
    # FINALIDADE:
    # Receber dados digitados pelo usuário.
    # --------------------------------------------------------
    nome = input("Digite o nome da disciplina: ")


    # --------------------------------------------------------
    # float()
    #
    # FINALIDADE:
    # Converter o valor para número decimal.
    # --------------------------------------------------------
    nota = float(input("Digite a nota: "))


    frequencia = float(input("Digite a frequência: "))


    # --------------------------------------------------------
    # Cria a nova listinha.
    # --------------------------------------------------------
    novo_registro = [nome, nota, frequencia]


    # --------------------------------------------------------
    # Pergunta a posição desejada.
    # --------------------------------------------------------
    posicao = int(input("\nDigite a posição desejada: "))


    # --------------------------------------------------------
    # insert()
    #
    # FINALIDADE:
    # Inserir um elemento
    # em uma posição específica.
    #
    # Sintaxe:
    #
    # lista.insert(posicao, valor)
    # --------------------------------------------------------
    lista.insert(posicao, novo_registro)


    # --------------------------------------------------------
    # Retorna a lista atualizada.
    # --------------------------------------------------------
    return lista




# ============================================================
# CHAMADA DA FUNÇÃO
# ============================================================

print(adicionar_registro_em_posicao(
    registro_de_disciplina
))