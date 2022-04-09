class CaixaEletronico:
    def __init__(self, saldo,id, senha):
        self.saldo = float(saldo)
        self.id = int(id)
        self.senha = int(senha)

    def VerSaldo():
        print(f"\033[1;31;40m {CaixaEletronico.saldo}")
        print("")
        
    def Depositar():
        saldo_adicional = float(input("Quanto dinheiro vc ira depositar: "))
        CaixaEletronico.saldo = saldo_adicional + CaixaEletronico.saldo
        print(f"\033[1;31;40m {CaixaEletronico.saldo}")
        print("")

    def Retirar():
        saldo_retirado = float(input("Quanto dinheiro vc ira retirar: "))
        if saldo_retirado < CaixaEletronico.saldo:
            CaixaEletronico.saldo = CaixaEletronico.saldo - saldo_retirado
            print(f"\033[1;31;40m {CaixaEletronico.saldo}")
        elif saldo_retirado > CaixaEletronico.saldo:
            print("Vc nao possui esse dinheiro")

    def Sair():
        global continuar
        continuar = 2
        print("\033c")

print("\033c")
CaixaEletronico.saldo = 0
print("Bem vindo ao banco !!\n Vamos criar sua conta!!! \n No seu ID e na sua Senha so podem haver numeros inteiros")
CaixaEletronico.id = int(input("Crie seu ID: "))
CaixaEletronico.senha = int(input("Crie sua senha: "))
print("\033c")
while True:
    id = input("Seu ID: ")
    senha = input("Sua senha: ")
    print("\033c")
    if int(id) == int(CaixaEletronico.id) and int(senha) == int(CaixaEletronico.senha):
        print("Bem vindo a sua conta !!!")
        continuar = 1
        while continuar == 1:
            input("\033[1;37;40m [ENTER]")
            print("\033c")
            print("""O que vc deseja fazer::
            [ 1 ]Ver Saldo da conta
            [ 2 ]Depositar na conta
            [ 3 ]Retirar da conta
            [ 4 ]Sair
            """)
            opcao = input
            if opcao == 1:
               CaixaEletronico.VerSaldo()
            elif opcao == 2:
                CaixaEletronico.Depositar()
            elif opcao == 3:
                CaixaEletronico.Retirar()
            elif opcao == 4:
                CaixaEletronico.Sair()
            else:
                print("Opcao invalida!!!!")
        else:
            id = 0
            senha = 0 
    else:
        print("ID e/ou Senha invalido")
