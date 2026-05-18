from datetime import datetime

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

def ondeEsta (nom,agd):
    inicio=0
    final =len(agd)-1

    while inicio<=final:
        meio=(inicio+final)//2

        if nom.upper()==agd[meio][0].upper():
            return [True,meio]
        elif nom.upper()<agd[meio][0].upper():
            final=meio-1
        else:
            inicio=meio+1

    return [False,inicio]

def umNaoVazio(rotulo):
    txt = input(rotulo).strip()
    while txt == '':
        print('Valor inválido - Favor redigitar...')
        txt = input(rotulo).strip()
    return txt

def umAniversario(rotulo):
    txt = input(rotulo).strip()
    while True:
        try:
            datetime.strptime(txt, '%d/%m/%Y')
            return txt
        except:
            print('Data inválida (use DD/MM/AAAA) - Favor redigitar...')
            txt = input(rotulo).strip()

def soDigitos(s):
    return ''.join([c for c in s if c.isdigit()])

def umTelefone(rotulo, minimo):
    txt = input(rotulo).strip()
    num = soDigitos(txt)
    while num == '' or len(num) < minimo:
        print('Número inválido - Favor redigitar...')
        txt = input(rotulo).strip()
        num = soDigitos(txt)
    return num

def umEmail(rotulo):
    txt = input(rotulo).strip()
    while True:
        if txt == '':
            ok = False
        elif ' ' in txt:
            ok = False
        elif '@' not in txt:
            ok = False
        else:
            partes = txt.split('@')
            ok = (len(partes) == 2 and partes[0] != '' and partes[1] != '' and '.' in partes[1])
        if ok:
            return txt
        print('e-mail inválido - Favor redigitar...')
        txt = input(rotulo).strip()

def cadastrar (agd):
    chave=True
    while chave:
        nome=input('\nNome.......: ').strip()
        while nome=='':
            print('Nome inválido - Favor redigitar...')
            nome=input('\nNome.......: ').strip()

        resposta=ondeEsta(nome,agd)
        achou   = resposta[0]
        posicao = resposta[1]

        if achou:
            print ('Pessoa já cadastrada; tente novamente!')
        else:
            chave=False

    aniversario = umAniversario('Aniversário (DD/MM/AAAA): ')
    endereco    = umNaoVazio('Endereço...: ')
    telefone    = umTelefone('Telefone...: ', 8)
    celular     = umTelefone('Celular....: ', 9)
    email       = umEmail('e-mail.....: ')

    contato=[nome,aniversario,endereco,telefone,celular,email]
    agd.insert(posicao,contato)
    print('Cadastro realizado com sucesso!')

def procurar (agd):
    if len(agd)==0:
        print('Agenda vazia!')
        return

    chave=True
    while chave:
        nome=input('\nNome a procurar: ').strip()
        while nome=='':
            print('Nome inválido - Favor redigitar...')
            nome=input('\nNome a procurar: ').strip()

        resposta=ondeEsta(nome,agd)
        achou   = resposta[0]
        posicao = resposta[1]

        if not achou:
            print('Contato não encontrado - Favor redigitar...')
        else:
            chave=False

    print('-----------------------------')
    print('Nome.......: ',agd[posicao][0])
    print('Aniversário: ',agd[posicao][1])
    print('Endereço...: ',agd[posicao][2])
    print('Telefone...: ',agd[posicao][3])
    print('Celular....: ',agd[posicao][4])
    print('e-mail.....: ',agd[posicao][5])
    print('-----------------------------')

def atualizar (agd):
    if len(agd)==0:
        print('Agenda vazia!')
        return

    chave=True
    while chave:
        nome=input('\nNome do contato a atualizar: ').strip()
        while nome=='':
            print('Nome inválido - Favor redigitar...')
            nome=input('\nNome do contato a atualizar: ').strip()

        resposta=ondeEsta(nome,agd)
        achou   = resposta[0]
        posicao = resposta[1]

        if not achou:
            print('Contato não encontrado - Favor redigitar...')
        else:
            chave=False

    submenu=['Atualizar aniversário',\
             'Atualizar endereco',\
             'Atualizar telefone',\
             'Atualizar celular',\
             'Atualizar email',\
             'Finalizar as atualizações']

    finalizar=False
    while not finalizar:
        op=int(opcaoEscolhida(submenu))

        if op==1:
            agd[posicao][1]=umAniversario('Novo aniversário (DD/MM/AAAA): ')
            print('Aniversário atualizado com sucesso!')
        elif op==2:
            agd[posicao][2]=umNaoVazio('Novo endereco: ')
            print('Endereço atualizado com sucesso!')
        elif op==3:
            agd[posicao][3]=umTelefone('Novo telefone: ', 8)
            print('Telefone atualizado com sucesso!')
        elif op==4:
            agd[posicao][4]=umTelefone('Novo celular: ', 9)
            print('Celular atualizado com sucesso!')
        elif op==5:
            agd[posicao][5]=umEmail('Novo email: ')
            print('e-mail atualizado com sucesso!')
        else:
            finalizar=True

def listar (agd):
    if len(agd)==0:
        print("Agenda vazia!")
    else:
        posicao=0
        while posicao<len(agd):
            print('-----------------------------')
            print('Nome.......: ',agd[posicao][0])
            print('Aniversário: ',agd[posicao][1])
            print('Endereço...: ',agd[posicao][2])
            print('Telefone...: ',agd[posicao][3])
            print('Celular....: ',agd[posicao][4])
            print('e-mail.....: ',agd[posicao][5])
            posicao+=1
        print('-----------------------------')

def excluir (agd):
    if len(agd)==0:
        print('Agenda vazia!')
        return

    chave=True
    while chave:
        nome=input('\nNome do contato a excluir: ').strip()
        while nome=='':
            print('Nome inválido - Favor redigitar...')
            nome=input('\nNome do contato a excluir: ').strip()

        resposta=ondeEsta(nome,agd)
        achou   = resposta[0]
        posicao = resposta[1]

        if not achou:
            print('Contato não encontrado - Favor redigitar...')
        else:
            chave=False

    confirma = umTexto('Confirma exclusão (S/N)? ', 'Confirmação inválida', ['S','N','s','n']).upper()

    if confirma=='S':
        agd.pop(posicao)
        print('Exclusão realizada com sucesso!')
    else:
        print('Exclusão não realizada!')

apresenteSe()

agenda=[]

menu=['Cadastrar Contato',\
      'Procurar Contato',\
      'Atualizar Contato',\
      'Listar Contatos',\
      'Excluir Contato',\
      'Sair do Programa']

chave=True
while chave:
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
        chave=False

print('PROGRAMA ENCERRADO COM SUCESSO!')