import os

def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')

limpar_tela()

while True:
    conta = input('Entre com a conta ou digite "S" para sair : ')
    if conta.lower() == 's':
        print('Saindo...')
        break
    else:
        try:
            resultado = eval(conta)
            print(f'Resultado: {resultado}')
        except Exception as e:
            print(f'Erro: Caractere inválido ou erro na conta, Tente novamente.')
    
