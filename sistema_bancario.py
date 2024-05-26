### Sistema bancário otimizado - Módulo 2 DIO

menu = """
[a] adicionar usuario
[c] criar conta
[d] depositar
[s] sacar
[e] extrato
[l] exibir lista de usuários e contas ativas
[q] sair

==>
"""

#funções criadas
import re

def validar_dados(*, dado, pattern):
    while not re.match(pattern, dado):
        dado = input("Dado inválido. Digite novamente: ")
    return dado

def adicionar_usuario(lista_cadastro):
    
    #Validação de dados - somente números são aceitos
    cpf_cadastro = input("Digite seu cpf. Somente números")
    cpf_padrao = r"\d{11}"

    cpf_cadastro = validar_dados(dado = cpf_cadastro, pattern = cpf_padrao)

    #NÃO podem existir dois cpfs iguais - validação dos dados
    if cpf_cadastro in lista_cadastro:
        print("O CPF já existe na lista de usuários.")

    else: 
        nome_cadastro = input("Digite seu nome: ")
        data_nasc_cadastro = input("Digite sua data de nascimento. Formato válido dd-mm-aaaa")
        
        #validação de dados para a data de nascimento
        data_nasc_padrao = r"\d{2}-\d{2}-\d{4}"
        data_nasc_cadastro = validar_dados(dado = data_nasc_cadastro, pattern = data_nasc_padrao)

        endereco_cadastro = input("Digite seu endereço. Formato válido: logradouro, nro, bairro, cidade, sigla estado")
        
        #criar dicionário com dados do novo usuário
        usuario = {
            "nome": nome_cadastro,
            "data_nascimento": data_nasc_cadastro,
            "endereco": endereco_cadastro
            }
    
        #ao final do código, acrescentar o novo usuario a lista de usuarios preexistente
        lista_cadastro[cpf_cadastro] = usuario
        print("Cadastro realizado com sucesso!")
        
    return lista_cadastro


def criar_conta(*, lista_de_contas, lista_de_usuarios):
    nro_conta = len(lista_de_contas) + 1

    ##pesquisar cpf do cliente para ver se já é cadastrado
    cpf = input("Digite seu cpf. Somente números")
    
    #verificar se o usuário já é cadastrado

    if lista_de_usuarios.get(cpf) == None:
        print("CPF não cadastrado.")
    else:
        conta_nova = dict(agencia = "0001", nro_conta = nro_conta, usuario = cpf)
        lista_de_contas.append(conta_nova)
        print("Conta cadastrada com sucesso!")
    return lista_de_contas
    

def depositar (saldo, deposito, extrato):
    if deposito < 0:
            print("Operação cancelada. O valor informado é inválido")
    else:
        saldo += deposito
        extrato += f"Depósito de R$ {deposito:.2f}\n"
        print("Seu saldo é R$ {:.2f}".format(saldo))    
    return saldo, extrato

def sacar (*, saldo, saque, extrato, limite, numero_saques, limite_saques):

    excedeu_saldo = saque > saldo
    excedeu_limite = saque > limite
    excedeu_num_saques = numero_saques >= limite_saques

    if excedeu_num_saques:
        print("Você atingiu o limite de saques diários.")
    
    elif excedeu_limite:
        print("Você atingiu o limite da operação de saque. Limite diário de R$500,00")

    elif excedeu_saldo:
        print("Saldo insuficiente. Seu saldo é R$ {:.2f}".format(saldo))
        
    elif saque > 0:
        saldo -= saque
        extrato += f"Saque de R$ {saque:.2f}\n"
        numero_saques += 1
        print("Você sacou R$ {:.2f}. Seu saldo atual é {:.2f}".format(saque, saldo))
    else:
        print("Operação cancelada. O valor informado é inválido")

    return saldo, extrato, numero_saques

def exibir_extrato(saldo, *, extrato):
    print("\n============= EXTRATO =============")
    print("Não foram realizadas movimentações." if not extrato else extrato)
    print("Saldo: {:.2f}".format(saldo))
    print("===================================")

def main():
    #limites e valores predefinidos
    saldo = 0
    limite = 500
    extrato = ""
    num_saques = 0
    limite_saques = 3
    lista_usuarios = {}
    lista_contas = []
    
    #sistema bancário
    while True:
    
        opcao = input(menu)
    
        if opcao == "d":
            deposito = float(input("Qual valor gostaria de depositar?"))
            saldo, extrato = depositar(saldo, deposito, extrato)
    
        elif opcao == "s":
            saque = float(input("Qual valor gostaria de sacar?"))
            saldo, extrato, num_saques = sacar(saldo = saldo, saque = saque, extrato = extrato, limite = limite, numero_saques = num_saques, limite_saques = limite_saques)
        
        elif opcao == "e":
            extrato = exibir_extrato(saldo, extrato = extrato)
    
        elif opcao == "a":
            lista_usuarios = adicionar_usuario(lista_usuarios)
        
        elif opcao == "c":
            lista_contas = criar_conta(lista_de_contas = lista_contas, lista_de_usuarios = lista_usuarios)
    
        elif opcao == "l":
            print("Usuários ativos: ", lista_usuarios,"\n", "Contas ativas: ", lista_contas)
    
        elif opcao == "q":
            break
        
        else:
            print("Operação inválida. Por favor selecione novamente a operação desejada.")

main()