gastos = []
def adicionar_gastos():
    nome = input("Digite o nome do gasto: ")
    valor = float(input("Digite o valor do gasto: "))

    gasto = {'nome': nome, 'valor': valor}
    gastos.append(gasto)

    print('gasto adicionado com sucesso !')
def listar_gastos():
    for gasto in gastos:
        print(gasto['nome'], '-', gasto['valor'])

def total_gastos():
    total = sum(g['valor'] for g in gastos)
    print('total de gastos:', total)

while True:
    print('1 - adicionar gasto')
    print('2 - listar gastos ')
    print('3 - total gasto')
    print('4 - sair ')

    opcao = input('digite sua opcao: ')
    if opcao == '1':
        adicionar_gastos()
    elif opcao == '2':
        listar_gastos()
    elif opcao == '3':
        total_gastos()
    elif opcao == '4':
        break