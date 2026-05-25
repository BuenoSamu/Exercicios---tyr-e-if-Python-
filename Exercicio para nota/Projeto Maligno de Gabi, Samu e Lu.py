'''

⋆𐙚₊˚⊹♡ Programa atualizado por Gabriela, Luiza e Samuel ⋆𐙚₊˚⊹♡
Versão 1.1 de 25/05/26

'''

import re

def apresenteSe ():
    print('+-------------------------------------------------------------+')
    print('|                                                             |')
    print('| AGENDA PESSOAL DE ANIVERSÁRIOS E FORMAS DE CONTATAR PESSOAS |')
    print('|                                                             |')
    print('| Prof André Luís dos Reis Gomes de Carvalho                  |')
    print('|                                                             |')
    print('| Versão 1.1 de 25/05/26                                      |')
    print('|                                                             |')
    print('+-------------------------------------------------------------+')

def _lerTextoObrigatorio(solicitacao, mensagem, min_len=1):
    while True:
        txt = input(solicitacao).strip()
        if len(txt) < min_len:
            print(mensagem, '- Favor redigitar...')
        else:
            return txt

def _validarAniversario(txt):
    txt = txt.strip()
    m = re.fullmatch(r'(\d{1,2})/(\d{1,2})(?:/(\d{4}))?', txt)
    if not m:
        return False

    dia = int(m.group(1))
    mes = int(m.group(2))
    ano = m.group(3)

    if mes < 1 or mes > 12:
        return False
    if dia < 1 or dia > 31:
        return False

    if ano is not None:
        a = int(ano)
        if a < 1900 or a > 2100:
            return False

    return True

def _lerAniversario(solicitacao):
    while True:
        txt = input(solicitacao).strip()
        if _validarAniversario(txt):
            return txt
        print('Aniversário inválido - use dd/mm ou dd/mm/aaaa. Ex: 22/04 ou 22/04/2006')

def _soDigitos(txt):
    return ''.join(ch for ch in txt if ch.isdigit())

def _lerTelefone(solicitacao, permitirVazio=True):
    while True:
        bruto = input(solicitacao).strip()

        if permitirVazio and bruto == '':
            return ''

        numero = _soDigitos(bruto)
        if numero.isdigit() and 8 <= len(numero) <= 13:
            return numero

        print('Telefone/Celular inválido - digite de 8 a 13 dígitos (pode usar ( ) espaço e -).')

def _lerEmail(solicitacao, permitirVazio=True):
    padrao = r'^[A-Za-z0-9._%+\-]+@[A-Za-z0-9\-]+(\.[A-Za-z0-9\-]+)+$'

    while True:
        txt = input(solicitacao).strip()

        if permitirVazio and txt == '':
            return ''

        if re.fullmatch(padrao, txt):
            return txt

        print('e-mail inválido - Favor redigitar... (ex: nome@dominio.com)')

def _lerSimNao(solicitacao):
    while True:
        resp = input(solicitacao).strip().upper()
        if resp in ['S','N']:
            return resp
        print('Opção inválida! Digite S ou N.')

def umTexto (solicitacao, mensagem, valido):
    digitouDireito=False
    while not digitouDireito:
        txt=input(solicitacao).strip()

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
    nom = nom.strip()

    while inicio<=final:
        meio=(inicio+final)//2

        if nom.upper()==agd[meio][0].upper():
            return [True,meio]
        elif nom.upper()<agd[meio][0].upper():
            final=meio-1
        else:
            inicio=meio+1

    return [False,inicio]

def cadastrar (agd):
    chave_para_digitar_ate_acertar_ligada=True
    while chave_para_digitar_ate_acertar_ligada:
        nome=_lerTextoObrigatorio('\nNome.......: ', 'Nome inválido', min_len=2)

        resposta=ondeEsta(nome,agd)
        achou   = resposta[0]
        posicao = resposta[1]

        if achou:
            print ('Pessoa já cadastrada; tente novamente!')
        else:
            chave_para_digitar_ate_acertar_ligada=False

    aniversario=_lerAniversario('Aniversário (dd/mm ou dd/mm/aaaa): ')
    endereco   =_lerTextoObrigatorio('Endereço...: ', 'Endereço inválido', min_len=3)
    telefone   =_lerTelefone('Telefone...: ', permitirVazio=True)
    celular    =_lerTelefone('Celular....: ', permitirVazio=True)
    email      =_lerEmail('e-mail.....: ', permitirVazio=True)

    contato=[nome,aniversario,endereco,telefone,celular,email]

    agd.insert(posicao,contato)
    print('Cadastro realizado com sucesso!')

def procurar(agd):
    if len(agd) == 0:
        print('Agenda vazia!')
    else:
        achou = False

        while not achou:
            # valida nome
            nome = _lerTextoObrigatorio('\nDigite o nome que deseja procurar: ', 'Nome inválido', min_len=2)

            resposta = ondeEsta(nome, agd)

            achou = resposta[0]
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

def atualizar(agd):
    if len(agd) == 0:
        print('Agenda vazia!')
    else:
        achou = False

        while not achou:
            # valida nome
            nome = _lerTextoObrigatorio('\nDigite o nome do contato que deseja atualizar: ', 'Nome inválido', min_len=2)

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

            opcao = input('Escolha uma opção: ').strip()

            if opcao == '1':
                agd[posicao][1] = _lerAniversario('Novo aniversário (dd/mm ou dd/mm/aaaa): ')
                print('Aniversário atualizado com sucesso!')

            elif opcao == '2':
                agd[posicao][2] = _lerTextoObrigatorio('Novo endereço...: ', 'Endereço inválido', min_len=3)
                print('Endereço atualizado com sucesso!')

            elif opcao == '3':
                agd[posicao][3] = _lerTelefone('Novo telefone...: ', permitirVazio=True)
                print('Telefone atualizado com sucesso!')

            elif opcao == '4':
                agd[posicao][4] = _lerTelefone('Novo celular....: ', permitirVazio=True)
                print('Celular atualizado com sucesso!')

            elif opcao == '5':
                agd[posicao][5] = _lerEmail('Novo e-mail.....: ', permitirVazio=True)
                print('e-mail atualizado com sucesso!')

            elif opcao == '6':
                finalizar = True
            else:
                print('Este número não é valido! Por favor, digite um valor entre 1-6!')

def listar(agd):
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

def excluir (agd):
    if len(agd)==0:
        print('Agenda vazia!')
    else:
        # valida nome
        nome=_lerTextoObrigatorio('\nNome do contato para excluir: ', 'Nome inválido', min_len=2)
        resposta=ondeEsta(nome,agd)

        achou = resposta[0]
        posicao = resposta[1]

        if not achou:
            print('Contato não cadastrado!')
        else:
            confirmacao = _lerSimNao('Confirma exclusão? [S/N] ')
            if confirmacao=='S':
                del agd[posicao]
                print('Exclusão confirmada!')
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