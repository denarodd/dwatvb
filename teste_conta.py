from conta_bancaria import ContaBancaria


conta1 = ContaBancaria("123", "Ana Lima")

print("Saldo inicial:", conta1.get_saldo())

conta1.depositar(100)
print("Após depósito:", conta1.get_saldo())

conta1.sacar(40)
print("Após saque:", conta1.get_saldo())

try:
    conta1.sacar(100)
except ValueError as erro:
    print("Erro:", erro)

print("Saldo final:", conta1.get_saldo())

#atividade pratica
ana = ContaBancaria("123", "Ana Lima")
carlos = ContaBancaria("456", "Carlos Souza")
maria = ContaBancaria("789", "Maria Silva")

ana.depositar(500.00)
carlos.depositar(300.00)
maria.depositar(100.00)

ana.transferir(carlos, 200.00)

carlos.transferir(maria, 150.00)

try:
    maria.transferir(ana, 500.00)
except ValueError as erro:
    print("\nErro na transferência de Maria:", erro)

try:
    ana.transferir(ana, 10.00)
except ValueError as erro:
    print("Erro na transferência para a própria conta:", erro)

print("\nSaldos finais da atividade:")
print(f"Ana Lima (conta {ana.numero}): R$ {ana.get_saldo():.2f}")
print(f"Carlos Souza (conta {carlos.numero}): R$ {carlos.get_saldo():.2f}")
print(f"Maria Silva (conta {maria.numero}): R$ {maria.get_saldo():.2f}")