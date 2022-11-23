import random
import json
import os

numero = 0
conta = {
         'nome': None,
         'numero': numero,
         'senha': None,
         'saldo': 0
         }
#definindo o valor da conta
senha1 = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X ', 'Y', 'Z']
senha2 = ['1', ' 2', '3', '4', '5', '6', '7', '8', '9', '0']

letras = (random.choices(senha1,k=3))
numeros = (random.choices(senha2, k=3))
juntos = str(letras+numeros)
juntos = juntos.replace(',', '')#Arrumar esta parte
juntos = juntos.replace('[', '')
juntos = juntos.replace(']', '')
juntos = juntos.replace("'", '')
juntos = juntos.replace(' ', '')
conta['numero'] = juntos


#definindo funçoes da conta
def criar_conta(nome, senha):
    conta['nome'] = nome
    conta['senha'] = senha
    with open(f"BANCOJSON/conta{conta.get('nome')}-{conta.get('numero')}.json", 'w') as arquivo:
        json.dump(conta, arquivo, indent=3)
    with open(f"BANCOJSON/conta{conta.get('nome')}-{conta.get('numero')}.json", 'r') as arquivo2:
        print(arquivo2.read())

def logar(login_nome,login_numero_conta,  login_senha):
    with open(f'BANCOJSON/conta{login_nome}-{login_numero_conta}.json', 'r') as arquivo :
        dict = json.load(arquivo)
        if login_senha == dict['senha']:
            print('logado com sucesso')
            print(dict)
        else:
            print('houve uma falha no login')
            quit()

def depositar(quantia, login_nome, login_numero_conta):
    with open(f'BANCOJSON/conta{login_nome}-{login_numero_conta}.json', 'r') as arquivo:
        data = json.load(arquivo)
        data['saldo'] = data.get('saldo') + int(quantia)

    with open(f'BANCOJSON/conta{login_nome}-{login_numero_conta}.json', 'w') as arq2:
        ndata = json.dumps(data, indent=3)
        arq2.write(ndata)

    with open(f'BANCOJSON/conta{login_nome}-{login_numero_conta}.json', 'r') as arq:
        data = json.load(arq)
        print(f'seu novo saldo é {data.get("saldo")}')



def sacar(quantia, login_nome, login_numero_conta):
    with open(f'BANCOJSON/conta{login_nome}-{login_numero_conta}.json', 'r') as arquivo:
        data = json.load(arquivo)
        data['saldo'] = data.get('saldo') - int(quantia)
        if data['saldo'] < int(quantia):
            print('saldo insuficiente')
            quit()


    with open(f'BANCOJSON/conta{login_nome}-{login_numero_conta}.json', 'w') as arq:
        ndata = json.dumps(data, indent=3)
        arq.write(ndata)

    with open(f'BANCOJSON/conta{login_nome}-{login_numero_conta}.json', 'r') as arq2:
        data = json.load(arq2)
        print(data)
        print(f'seu novo saldo é de {data.get("saldo")}')

def excluir_conta(login_nome, login_numero_conta):
    os.remove(f'BANCOJSON/conta{login_nome}-{login_numero_conta}.json')
    print('sua conta foi removida com sucesso!!!')











