import os, getpass

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

#menu geral
def menu_principal():
    print('''
          # 1 - Entre na sua conta
          # 0 - Encerrar sistema
          ''')
    try:
        retorno_menu = int(input('Digite a opção desejada:'))
        return retorno_menu
    except ValueError:
        print('Opção invalida, digite novamente')
        return menu_principal()
    
# Sistema de login
def logar():
    usuario = input('Digite seu usuario:')
    senha = getpass.getpass("Digite sua senha: ")
    tentativas = 1
    if usuario == 'admin' and senha == 'admin':
        print('Login realizado com sucesso!')
        return True
    else:
        print('Usuario ou senha invalidos')
        tentativas +=1
        if tentativas < 3:
            logar()
        else:
            print('Limite de tentativas excedido')
            return False


# Sistema financeiro
def menu_fin():
    print('''
          # 1 - Ver Saldo
          # 2 - Realizar Saque
          # 3 - Realizar Deposito
          # 5 - Encerrar sistema
          ''')
    try:
        retorno_menu_fin = int(input('Digite a opção desejada:'))
        return retorno_menu_fin
    except ValueError:
        print('Opção invalida, digite novamente')
        return menu_fin()
    
# Sistema financeiro
def financeiro():
    saldo = 0
    while True:
        opcao_fin =  menu_fin()
        limpar_tela()
        if opcao_fin == 1:
            print(f'O saldo atual é: {saldo}')
        elif opcao_fin == 2:
            limpar_tela()
            saldo = saque(saldo)
        elif opcao_fin == 3:
            limpar_tela()
            saldo = deposito(saldo)
        elif opcao_fin == 5:
            limpar_tela()
            print('Sistema encerrado')
            exit()


# Funções de saque 
def saque(saldo):
    valor =  float(input('Valor de saque:'))
    if valor < saldo:
        valor_restante = saldo - valor 
        print(f'Saque realizado \nSaldo total {valor_restante}')
        return valor_restante
    else:
        print(f'Saldo indisponivel')

# Funções de deposito
def deposito(saldo):
    valor =  float(input('Valor de deposito:'))
    if valor > 0:
        valor_fin = saldo + valor
        print(f'Deposito realizado \nSaldo total {valor_fin}')
        return valor_fin
    else:
        print(f'Valor invalido')


# Programa Principal
limpar_tela()
print("Bem-Vindo ao Sistema Bancario!")
menu = menu_principal()
if menu == 1:
    login = logar()
    if login == True:
        limpar_tela()
        print('     Entrando na sua conta...')
        financeiro()
    elif login == False:
        print('Parece que você não tem acesso ao sistema, entre em contato com o administrador')
        exit()
elif menu == 0:
    print('Sistema encerrado')
    limpar_tela()
    exit()
