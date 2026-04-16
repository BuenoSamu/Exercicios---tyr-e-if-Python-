from mysql.connector import connect, Error

'''
BD preparado para a execução
deste programa com o comando:

CREATE TABLE CONTATOS (
ID INT AUTO_INCREMENT PRIMARY KEY,
NOME VARCHAR(80) NOT NULL,
ANIVERSARIO DATE NOT NULL,
ENDERECO VARCHAR(200) NOT NULL,
TELEFONE BIGINT NOT NULL,
CELULAR BIGINT NOT NULL,
EMAIL VARCHAR(100) NOT NULL
)
'''

def apresenteSe ():
    print('+-------------------------------------------------------------+')
    print('|                                                             |')
    print('| AGENDA PESSOAL DE ANIVERSÁRIOS E FORMAS DE CONTATAR PESSOAS |')
    print('|                                                             |')
    print('| Profs André e J.G.Picolo                                    |')
    print('|                                                             |')
    print('| Versão 1.0 de 28/abril/2024                                 |')
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

def obtemConexao (servidor, usuario, senha, bd):
    if obtemConexao.conexao==None:
        obtemConexao.conexao = connect(host    =f"{servidor}",\
                                       user    =f"{usuario}",\
                                       password=f"{senha}",\
                                       database=f"{bd}")

    return obtemConexao.conexao
obtemConexao.conexao=None

def contatoCadastrado (nome):
    comando= f"Select * from CONTATOS where nome='{nome}'"

    conexao=obtemConexao("172.16.12.14","BD240225285","Ozgia4","BD240225285")
    cursor=conexao.cursor()
    cursor.execute(comando)

    linhas=cursor.fetchall()
    return linhas!=[] # se vem [], nao selecionou nada, nome nao cadastrado
    '''
    # o return acima produz o mesmo efeito que os comandos abaixo
    if linhas!=[]:
        return True
    else:
        return False
    '''

def insercaoDeContato (nome,aniversario,endereco,telefone,celular,email):
    comando= "Insert into CONTATOS "+\
             "(Nome,Aniversario,Endereco,Telefone,Celular,E_mail) "+\
             "values "+\
            f"('{nome}',STR_TO_DATE('{aniversario}','%d/%m/%Y'),'{endereco}',{telefone},{celular},'{email}')"

    conexao=obtemConexao("172.16.12.14","BD240225285","Ozgia4","BD240225285")
    cursor=conexao.cursor()
    cursor.execute(comando)
    conexao.commit()

def incluir ():
    nome=input('\nNome.......: ')

    try:
        jaCadastrado=contatoCadastrado(nome)
    except Error:    
        print("Problema de conexão com o BD!")
    else:
        if jaCadastrado:
            print("Nome já cadastrado!")
        else:
            aniversario=input('Aniversário: ')
            endereco   =input('Endereço...: ')
            telefone   =input('Telefone...: ')
            celular    =input('Celular....: ')
            email      =input('e-mail.....: ')

            try:
                insercaoDeContato (nome,aniversario,endereco,telefone,celular,email)
            except Error:
                print("Erro nos dados digitados!")
            else:
                print('Cadastro realizado com sucesso!')

def procurar ():
    print('Opção não implementada!')
    # Ficar pedindo para digitar um nome até digitar um nome que existe
    # cadastrado;
    # mostrar então na tela TODOS os demais dados encontrados 
    # sobre aquela pessoa.

def atualizar ():
    print('Opção não implementada!')
    # Ficar mostrando um menu oferecendo as opções de atualizar aniversário, ou
    # endereco, ou telefone, ou celular, ou email, ou finalizar as
    # atualizações; ficar pedindo para digitar a opção até digitar uma
    # opção válida; realizar a atulização solicitada; até ser escolhida a
    # opção de finalizar as atualizações.
    # USAR A FUNÇÃO opcaoEscolhida, JÁ IMPLEMENTADA, PARA FAZER O MENU

def listagemDeContatos ():
    comando= "Select Nome,DATE_FORMAT(Aniversario,'%d/%m/%Y') as Aniversario,Endereco,Telefone,Celular,E_mail from CONTATOS"
    conexao=obtemConexao("172.16.12.14","BD240225285","Ozgia4","BD240225285")
    cursor=conexao.cursor()
    cursor.execute(comando)

    linhas=cursor.fetchall()
    return linhas


def listar ():
    try:
        linha=listagemDeContatos()
    except Error:    
        print("Problema de conexão com o BD!")
    else:
        atual=0
        while atual<len(linha):
            print()
            print('Nome.......:',linha[atual][0])
            print('Aniversario:',linha[atual][1])
            print('Endereco...:',linha[atual][2])
            print('Telefone...:',linha[atual][3])
            print('Celular....:',linha[atual][4])
            print('e-mail.....:',linha[atual][5])
            atual+=1

        print()
        print("Listagem concluida com sucesso!")

def excluir ():
    print('Opção não implementada!')
    # Ficar pedindo para digitar um nome até digitar um nome que existe
    # cadastrado;
    # mostrar então na tela TODOS os demais dados encontrados 
    # sobre aquela pessoa.
    # Confirmar se deseja mesmo excluir, realizando a exclusão
    # em caso afirmativo.

def fechaConexao ():
    conexao=obtemConexao("143.106.250.84","andre","andre","andre")
    cursor=conexao.cursor()
    cursor.close()
    conexao.close()

# daqui para cima, definimos subprogramas (ou módulos, é a mesma coisa)
# daqui para baixo, implementamos o programa (nosso CRUD, C=create(inserir), R=read(recuperar), U=update(atualizar), D=delete(remover,apagar)

apresenteSe()

menu=['Incluir Contato',\
      'Procurar Contato',\
      'Atualizar Contato',\
      'Listar Contatos',\
      'Excluir Contato',\
      'Sair do Programa']

desejaSairDoPrograma=False
while not desejaSairDoPrograma:
    opcao = int(opcaoEscolhida(menu))

    if opcao==1:
        incluir()
    elif opcao==2:
        procurar()
    elif opcao==3:
        atualizar()
    elif opcao==4:
        listar()
    elif opcao==5:
        excluir()
    else: # if opcao==6:
        fechaConexao()
        desejaSairDoPrograma=True

print()        
print('PROGRAMA ENCERRADO; OBRIGADO POR USAR ESTE PROGRAMA!')
