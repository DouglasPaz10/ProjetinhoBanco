import conta


print('olá, seja bem vindo, o que voce gostaria de fazer?')
print('1-criar conta \n2-login')
menu = input()

if menu == "1":
    nome = input('qual seu nome?').upper().strip()
    senha = input('qual sua senha?').upper()
    conta.criar_conta(nome, senha)

if menu == "2":
    print("digite seu nome")
    login_nome = input().upper()
    print("digite sua senha")
    login_senha = input().upper().strip()
    print("qual o numero da sua conta?")
    login_numero_conta = input().upper()
    conta.logar(login_nome, login_numero_conta, login_senha)
    print('qual o próximo passo?\n1-sacar\n2-transferir\n3-depositar\n4-excluir conta')
    user_logado = input()

    if user_logado == '1':
        print('qual a quantia?')
        quantia = input()
        conta.sacar(quantia, login_nome, login_numero_conta)


    if user_logado == '2':
        print('qual o destinatario')
        destinatario = input()
        print('qual o numero da conta do destinatario?')
        nmr_destinatario = input()
        print('valor desejado')
        quantia = input()
        #conta.transferir(login_nome, login_numero_conta,  quantia, destinatario, nmr_destinatario)

    if user_logado == "3":
        print('qual a quantia?')
        quantia = input()
        conta.depositar(quantia, login_nome, login_numero_conta)

    if user_logado == "4":
        ctz = input('voce tem certeza disso?  1-sim \n 2-não')
        if ctz == "1":
            conta.excluir_conta(login_nome, login_numero_conta)
        else:
            quit


