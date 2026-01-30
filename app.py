import os

restaurantes = [{'nome':'Biel Lanches', 'categoria':'Hamburguer', 'ativo':False},
                {'nome':'Abaré', 'categoria':'Pizza', 'ativo':True},
                {'nome':'Cantina', 'categoria':'Italiano', 'ativo':False}
]

def exibir_nome_do_programa():
    '''Essa função é responsável por exibir o nome do programa'''
    print('''

░██████╗░█████╗░██████╗░░█████╗░██████╗░  ███████╗██╗░░██╗██████╗░██████╗░███████╗░██████╗░██████╗
██╔════╝██╔══██╗██╔══██╗██╔══██╗██╔══██╗  ██╔════╝╚██╗██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝██╔════╝
╚█████╗░███████║██████╦╝██║░░██║██████╔╝  █████╗░░░╚███╔╝░██████╔╝██████╔╝█████╗░░╚█████╗░╚█████╗░
░╚═══██╗██╔══██║██╔══██╗██║░░██║██╔══██╗  ██╔══╝░░░██╔██╗░██╔═══╝░██╔══██╗██╔══╝░░░╚═══██╗░╚═══██╗
██████╔╝██║░░██║██████╦╝╚█████╔╝██║░░██║  ███████╗██╔╝╚██╗██║░░░░░██║░░██║███████╗██████╔╝██████╔╝
╚═════╝░╚═╝░░╚═╝╚═════╝░░╚════╝░╚═╝░░╚═╝  ╚══════╝╚═╝░░╚═╝╚═╝░░░░░╚═╝░░╚═╝╚══════╝╚═════╝░╚═════╝░
''')

def exibir_opcoes():
    '''Essa função é responsável por exibir as opções disponíveis'''
    print('1. Cadastrar restaurante')
    print('2. Listar restaurantes')
    print('3. Alternar situação do Restaurante')
    print('4. Sair')

def finalizar_app():
    '''Essa função é responsável por mostrar que o app foi encerrado'''
    exibir_subtitulo('Encerrando o App')

def voltar_menu_principal():
    '''Essa função é responsável por voltar ao menu principal'''
    input('\nDigite uma tecla para voltar ao menu principal ')
    main()

def opcao_invalida():
    '''Essa função é responsável por mostrar que a opção escolhida é inválida e retornar ao menu principal'''
    print('Opção inválida!\n')
    voltar_menu_principal()

def exibir_subtitulo(texto):
    '''Essa função é responsável por exibir o subtitulo das opções'''
    os.system('cls')
    linha = '*' * len(texto)
    print(linha)
    print(texto)
    print(linha)
    print()

def cadastrar_novo_restaurante():
    '''Essa função é responsável por cadastrar um novo restaurante
    
    Inputs: 
    - Nome do Restaurante
    - Categoria

    Outputs:
    - Adiciona um novo restaurante a lista de restaurantes

    '''
    exibir_subtitulo('Cadastro de novos restaurantes')
    nome_do_restaurante = input('Digite o nome do restaurante que deseja cadastrar: ')
    categoria = input(f'Digite o nome da categoria do restaurante {nome_do_restaurante}: ')
    dados_do_restaurante = {'nome':nome_do_restaurante, 'categoria':categoria, 'ativo':False}
    restaurantes.append(dados_do_restaurante)
    print(f'O restaurante {nome_do_restaurante} foi cadastrado corretamente!')
    voltar_menu_principal()

def listar_restaurantes():
    '''Essa função é responsável por listar os restaurantes'''
    exibir_subtitulo('Listando os restaurantes')
    print(f'{'Nome do Restaurante'.ljust(22)} | {'Categoria'.ljust(20)} | Situação')
    for restaurante in restaurantes:
        nome_restaurante = restaurante['nome']
        categoria= restaurante['categoria']
        situacao = 'Ativado' if restaurante['ativo'] else 'Desativado'
        print(f'- {nome_restaurante.ljust(20)} | {categoria.ljust(20)} | {situacao}')
    voltar_menu_principal()

def definir_situacao_restaurante():
    '''Essa função é responsável por Alterar a situação do restaurante'''
    exibir_subtitulo('Definindo a situação do restaurante (Ativo | Inativo)')
    nome_restaurante = input('Digite o nome do restaurante que deseja definir a situação: ')
    restaurante_existe = False
    for restaurante in restaurantes:
        if nome_restaurante == restaurante['nome']:
            restaurante_existe = True
            restaurante['ativo'] = not restaurante['ativo']
            mensagem = f'O restaurante {nome_restaurante} foi ativo com sucesso' if restaurante['ativo'] else f'O restaurante {nome_restaurante} foi desativado com sucesso'
            print(mensagem)
    if not restaurante_existe:
        print('O restaurante não foi encontrado!')
    voltar_menu_principal()

def escolher_opcoes():
    '''Essa função é responsável por definir a opção escolhida'''
    try:
        opcao_escolhida = int(input('Escolha uma opção: '))
        # opcao_escolhida = int(opcao_escolhida)

        if opcao_escolhida == 1:
            cadastrar_novo_restaurante()
        elif opcao_escolhida == 2:
            listar_restaurantes()
        elif opcao_escolhida == 3:
            definir_situacao_restaurante()
        elif opcao_escolhida == 4:
            finalizar_app()
        else:
            opcao_invalida()
    except:
        opcao_invalida()

def main():
    '''Função main, responsável pela execução do programa'''
    os.system('cls')
    exibir_nome_do_programa()
    exibir_opcoes()
    escolher_opcoes()

if __name__ == '__main__':
    main()