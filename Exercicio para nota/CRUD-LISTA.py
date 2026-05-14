def apresenteSe():
    print('+-------------------------------------------------------------+')
    print('|                                                             |')
    print('| AGENDA PESSOAL DE ANIVERSÁRIOS E FORMAS DE CONTATAR PESSOAS |')
    print('|                                                             |')
    print('| Prof André Luís dos Reis Gomes de Carvalho                  |')
    print('|                                                             |')
    print('| Versão 1.0 de 22/abril/2026                                 |')
    print('|                                                             |')
    print('+-------------------------------------------------------------+')


def umTexto(solicitacao, mensagem, valido):
    digitouDireito = False
    while not digitouDireito:
        txt = input(solicitacao)

        if txt not in valido:
            print(mensagem, '- Favor redigitar...')
        else:
            digitouDireito = True

    return txt


def opcaoEscolhida(mnu):
    print()

    opcoesValidas = []
    posicao = 0
    while posicao < len(mnu):
        print(posicao + 1, ') ', mnu[posicao], sep='')
        opcoesValidas.append(str(posicao + 1))
        posicao += 1

    print()
    return umTexto('Qual é a sua opção? ', 'Opção inválida', opcoesValidas)


def ondeEsta(nom, agd):
    inicio = 0
    final = len(agd) - 1

    while inicio <= final:
        meio = (inicio + final) // 2

        if nom.upper() == agd[meio][0].upper():
            return [True, meio]
        elif nom.upper() < agd[meio][0].upper():
            final = meio - 1
        else:
            inicio = meio + 1

    return [False, inicio]


def cadastrar(agd):
    # Pede o nome até o usuário digitar um que ainda não exista
    while True:
        nome = input('\nNome.......: ')

        resposta = ondeEsta(nome, agd)
        achou = resposta[0]
        posicao = resposta[1]

        if achou:
            print('Pessoa já cadastrada; tente novamente!')
        else:
            break

    aniversario = input('Aniversário: ')
    endereco = input('Endereço...: ')
    telefone = input('Telefone...: ')
    celular = input('Celular....: ')
    email = input('e-mail.....: ')

    contato = [nome, aniversario, endereco, telefone, celular, email]
    agd.insert(posicao, contato)
    print('Cadastro realizado com sucesso!')


def procurar(agd):
    print('Opção não implementada!')


def atualizar(agd):
    print('Opção não implementada!')


def listar(agd):
    # Se não houver contatos cadastrados, avisa e retorna
    if len(agd) == 0:
        print("Agenda vazia!")
        return

    # Percorre a lista de contatos e exibe todos os dados de cada um
    posicao = 0
    while posicao < len(agd):
        print('-----------------------------')
        print('Nome.......: ', agd[posicao][0])
        print('Aniversário: ', agd[posicao][1])
        print('Endereço...: ', agd[posicao][2])
        print('Telefone...: ', agd[posicao][3])
        print('Celular....: ', agd[posicao][4])
        print('e-mail.....: ', agd[posicao][5])
        posicao += 1
    print('-----------------------------')


def excluir(agd):
    print('Opção não implementada!')


apresenteSe()

agenda = []

menu = [
    'Cadastrar Contato',
    'Procurar Contato',
    'Atualizar Contato',
    'Listar Contatos',
    'Excluir Contato',
    'Sair do Programa'
]

# Executa o menu até o usuário escolher sair
while True:
    opcao = int(opcaoEscolhida(menu))

    if opcao == 1:
        cadastrar(agenda)
    elif opcao == 2:
        procurar(agenda)
    elif opcao == 3:
        atualizar(agenda)
    elif opcao == 4:
        listar(agenda)
    elif opcao == 5:
        excluir(agenda)
    else:
        break

print('PROGRAMA ENCERRADO COM SUCESSO!')