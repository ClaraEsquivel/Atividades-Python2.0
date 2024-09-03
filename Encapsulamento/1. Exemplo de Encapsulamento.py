import os

os.system("cls||clear")

#Criando sua própria exceção
class SaldoInsuficienteError(Exception):
    pass
      
#Criando sua própria exceção
class ValorNegativoError (Exception):
    pass

class Conta:
    def __init__(self, numero_conta:int, agencia:int) -> None:
        self.numero_conta = numero_conta
        self.agencia = agencia
        self._saldo = 0 #dessa forma não é obrigado a pedir um valor, ele já é pré definido.
        # _  = atributo protegido (pode ser herdado)

    @property #saberá sem acessar o atributo
    def saldo(self):
        return self._saldo
    
    def sacar(self, valor) -> float:
        try:
            self.__verificar_sacar(valor)
        except SaldoInsuficienteError as error:
            return f"Erro: {error}"
            
        self._saldo -= valor #diminui
        return self._saldo
    
    def __verificar_sacar(self, valor): #Método privado / serve de apoio para um método público
        if valor > self._saldo:
            raise SaldoInsuficienteError("Saldo insuficiente.")
            #raise = lançando um erro 
    

    def depositar(self, valor):
        try:
            self.__verificar_depositar(valor)
        except ValorNegativoError as error:
            return f"Erro: {error}"    

        self._saldo += valor #soma
        return self._saldo
    
    def __verificar_depositar(self, valor):
        if valor < 0:
            raise ValorNegativoError("Não é possível depositar um valor negativo")


class ContaCorrente(Conta):
    pass

class ContaPoupanca(Conta):
    pass

#Instanciando classes.
conta_corrente = ContaCorrente(123, 111)
conta_poupança = ContaPoupanca(456, 222)

print(conta_corrente.saldo)
print(conta_corrente.sacar(200))
print(conta_corrente.saldo)
print(conta_corrente.depositar(-200))

    