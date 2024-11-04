class conta:
    def __init__ (self, nome, cpf, numero, saldo):
        self.nome = nome
        self.cpf = cpf
        self.numero = numero
        self.saldo = saldo

    def depositar (self, valor):
        self.saldo += valor
    
    def sacar (self, valor):
        self.saldo -= valor
    
    def gerar_extrato (self):
        print(f'numero: {self.numero}, cpf: {self.cpf}, saldo: {self.saldo}')

def main():
    c1 = conta ('Ryan', 132553, 555, 500000)
    c1.depositar(500)
    c1.sacar(123)
    c1.gerar_extrato()

if __name__ == "__main__":
    main()