from conta import conta

conta1 = conta('Ryan', 000, 123, 0)
conta2 = conta('Lucas', 111, 789, 0)

conta1.depositar(1000)
conta1.transfereValor(conta2, 500)

print(conta1.saldo)
print(conta2.saldo)