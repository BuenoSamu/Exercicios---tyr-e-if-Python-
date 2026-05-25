'''

⋆𐙚₊˚⊹♡ Programa atualizado por Gabriela, Luiza e Samuel ⋆𐙚₊˚⊹♡

'''
def apresenteSe ():
    print('+-------------------------------------------------------------+')
    print('|                                                             |')
    print('| AGENDA PESSOAL DE ANIVERSÁRIOS E FORMAS DE CONTATAR PESSOAS |')
    print('|                                                             |')
    print('| Prof André Luís dos Reis Gomes de Carvalho                  |')
    print('|                                                             |')
    print('| Versão 1.0 de 22/abril/2026                                 |')
    print('|                                                             |')
    print('+-------------------------------------------------------------+')

def umTexto (solicitacao, mensagem, valido):
    digitouDireito=False
    while not digitouDireito:
        txt=input(solicitacao)

        if txt not in valido:
            print(mensagem,'- Favor redigitar...')
        else:
            digitouDireito=True

    return txt

def opcaoEscolhida (mnu):
    print ()

    opcoesValidas=[]
    posicao=0
    while posicao<len(mnu):
        print (posicao+1,') ',mnu[posicao],sep='')
        opcoesValidas.append(str(posicao+1))
        posicao+=1

    print()
    return umTexto('Qual é a sua opção? ', 'Opção inválida', opcoesValidas)

'''
procura nom em agd e, se achou, retorna:
uma lista contendo True e a posicao onde achou;
MAS, se não achou, retorna:
uma lista contendo False e a posição onde inserir,
aquilo que foi buscado, mas nao foi encontrado,
mantendo a ordenação da lista.
'''

def ondeEsta (nom,agd):
    inicio=0
    final =len(agd)-1
    
    while inicio<=final:
        meio=(inicio+final)//2
        
        if nom.upper()==agd[meio][0].upper():
            return [True,meio]
        elif nom.upper()<agd[meio][0].upper():
            final=meio-1
        else: # nom.upper()>agd[meio][0].upper()
            inicio=meio+1
            
    return [False,inicio]

def cadastrar (agd):
    chave_para_digitar_ate_acertar_ligada=True
    while chave_para_digitar_ate_acertar_ligada:
        nome=input('\nNome.......: ')

        resposta=ondeEsta(nome,agd)
        achou   = resposta[0]
        posicao = resposta[1]

        if achou:
            print ('Pessoa já cadastrada; tente novamente!')
        else:
            chave_para_digitar_ate_acertar_ligada=False
            
    aniversario=input('Aniversário: ')
    endereco   =input('Endereço...: ')
    telefone   =input('Telefone...: ')
    celular    =input('Celular....: ')
    email      =input('e-mail.....: ')
    
    contato=[nome,aniversario,endereco,telefone,celular,email]
    
    agd.insert(posicao,contato)
    print('Cadastro realizado com sucesso!')

def procurar(agd):  #FEITO =============================================================
    if len(agd) == 0:
        print('Agenda vazia!')
    else:
        achou = False

        while not achou:
            nome = input('\nDigite o nome que deseja procurar: ')

            resposta = ondeEsta(nome, agd)

            achou = resposta[0] #True ou False
            posicao = resposta[1] 

            if not achou:
                print('Pessoa não cadastrada; tente novamente!')

        print('='*70)
        print('Nome.......: ', agd[posicao][0])
        print('Aniversário: ', agd[posicao][1])
        print('Endereço...: ', agd[posicao][2])
        print('Telefone...: ', agd[posicao][3])
        print('Celular....: ', agd[posicao][4])
        print('e-mail.....: ', agd[posicao][5])
        print('='*70)
        
        
def atualizar(agd): #FEITO =============================================================

    if len(agd) == 0:
        print('Agenda vazia!')
    else:

        achou = False

        while not achou:

            nome = input('\nDigite o nome do contato que deseja atualizar: ')

            resposta = ondeEsta(nome, agd)

            achou = resposta[0]
            posicao = resposta[1]

            if not achou:
                print('Pessoa não cadastrada; tente novamente!')

        finalizar = False

        while not finalizar:

            print('\n1) Atualizar aniversário')
            print('2) Atualizar endereço')
            print('3) Atualizar telefone')
            print('4) Atualizar celular')
            print('5) Atualizar e-mail')
            print('6) Finalizar atualizações')

            opcao = input('Escolha uma opção: ')

            if opcao == '1':

                agd[posicao][1] = input('Novo aniversário: ')
                print('Aniversário atualizado com sucesso!')

            elif opcao == '2':

                agd[posicao][2] = input('Novo endereço...: ')
                print('Endereço atualizado com sucesso!')

            elif opcao == '3':

                agd[posicao][3] = input('Novo telefone...: ')
                print('Telefone atualizado com sucesso!')

            elif opcao == '4':

                agd[posicao][4] = input('Novo celular....: ')
                print('Celular atualizado com sucesso!')

            elif opcao == '5':

                agd[posicao][5] = input('Novo e-mail.....: ')
                print('e-mail atualizado com sucesso!')

            elif opcao == '6':
                finalizar = True
            else:
                print('Este número não é valido! Por favor, digite um valor entre 1-6!')

def listar(agd):  #FEITO =============================================================
    if len(agd) == 0:
        print("Agenda vazia!")
    else:
        posicao = 0
        while posicao < len(agd):
            print('='*70)
            print('Nome.......: ',agd[posicao][0],sep='')
            print('Aniversário: ',agd[posicao][1],sep='')
            print('Endereço...: ',agd[posicao][2],sep='')
            print('Telefone...: ',agd[posicao][3],sep='')
            print('Celular....: ',agd[posicao][4],sep='')
            print('e-mail.....: ',agd[posicao][5],sep='')
            print('='*70)
            posicao+=1


def excluir (agd):  #FEITO =============================================================
    if len(agd)==0:
        print('Agenda vazia!')
    else:
        nome=input('\nNome do contato para excluir: ')
        resposta=ondeEsta(nome,agd) # --> pega o contato

        achou = resposta[0] # ---=---> acho = nome
        posicao = resposta[1] # ----> pos = 2

        if not achou:
            print('Contato não cadastrado!')
        else:
            confirmacao = input('Confirma exclusão? [S/N]')
            if confirmacao.upper()=='S':
                del agd[posicao] #-----> vira del agr[2] e o 2 é o nome do contato
                print('Exclusão confirmada!')

            elif confirmacao.upper()=='N':
                    print('Exclusão não realizada!')
            else:
                    print('Opção inválida!')

apresenteSe()

agenda=[]

menu=['Cadastrar Contato',\
      'Procurar Contato',\
      'Atualizar Contato',\
      'Listar Contatos',\
      'Excluir Contato',\
      'Sair do Programa']

chave_para_executar_opcoes_ate_escolher_sair_ligada=True
while chave_para_executar_opcoes_ate_escolher_sair_ligada:
    opcao = int(opcaoEscolhida(menu))

    if opcao==1:
        cadastrar(agenda)
    elif opcao==2:
        procurar(agenda)
    elif opcao==3:
        atualizar(agenda)
    elif opcao==4:
        listar(agenda)
    elif opcao==5:
        excluir(agenda)
    else: 
        chave_para_executar_opcoes_ate_escolher_sair_ligada=False
        
print('૮ ྀིᴗ͈ . ᴗ͈ ྀིა Programa Finalizado! Volte sempre .✦ ૮ ྀིᴗ͈ . ᴗ͈ ྀིა')