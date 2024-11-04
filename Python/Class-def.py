class conta:
    def __init__ (self, nome, cpf, numero, saldo):
        self.nome = nome
        self.cpf = cpf
        self.numero = numero
        self.saldo = saldo

      

def main():
    c1 = conta (nome, cpf, numero, saldo)
    print(f'Nome do titular da conta: {c1.nome}')
    print(f'Cpf do titular da conta: {c1.cpf}')
    print(f'Numero da conta: {c1.numero}')
    print(f'Saldo da conta: {c1.saldo}')
        
nome = input("Nome do titular da conta: ")
cpf = int(input("Cpf do titular da conta: "))
numero = int(input("Numero da conta: "))
saldo = float(input("Saldo da conta: R$"))

    
if __name__ == "__main__":
    main()