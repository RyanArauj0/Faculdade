class conta:
    def __init__ (self, nome, cpf, numero, saldo):
        self.nome = nome
        self.cpf = cpf
        self.numero = numero
        self.saldo = saldo

    def depositar (self, valor):
        self.saldo += valor
    
    def sacar (self, valor):
        if self.saldo < valor:
            return False
        else:
            self.saldo -= valor
            return True
    
    def gerar_extrato (self):
        print(f'numero: {self.numero}, cpf: {self.cpf}, saldo: {self.saldo}')

    def tranfereValor (self, contaDestino, valor):
        if self.saldo < valor:
            return ('Não existe saldo suficiente')
        else:
            contaDestino.depositar(valor)
            self.saldo -= valor
            return('Transferência realizada!')
