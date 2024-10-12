# Exemplo de herança
print("Exemplo de Herança")
class Animal():
  def __init__(self, nome) -> None:
    self.nome = nome
    
  def andar(self):
    return f"o {self.nome} andou."
    
  def emitir_som(self):
    pass
  
class Cachorro(Animal):
  def emitir_som(self):
    return "au au"
  
class Gato(Animal):
  def emitir_som(self):
    return "miauuu"
  
cachorro = Cachorro("Rex")
gato = Gato("Felix")

print("\nExemplo de polimorfismo")
animais = [cachorro,gato]
for animal in animais:
  print(f"\n{animal.nome} faz {animal.emitir_som()}")
  
print("\nExemplo de Encapsulamento:")
class ContaBancaria():
  def __init__(self, saldo) -> None:
    self.__saldo = saldo # Atributo privado
    
  def depositar(self, valor):
    if valor > 0:
      self.__saldo += valor
      return f"Seu novo saldo é: {self.__saldo}"
      
  def sacar(self, valor):
    if self.__saldo >= valor:
      self.__saldo -= valor
      return f"Seu novo saldo é: {self.__saldo}"
    
  def consultar_saldo(self):
    return f"Saldo: {self.__saldo}"
  
conta = ContaBancaria(1000)
print(conta.consultar_saldo())
print(conta.depositar(1000))
print(conta.consultar_saldo())
print(conta.sacar(200))
print(conta.consultar_saldo())

print("\nExemplo de abstração:")
from abc import ABC, abstractmethod

class Veiculo(ABC):
  
  @abstractmethod
  def ligar(self):
    pass
  
  @abstractmethod
  def desligar(self):
    pass

class Carro(Veiculo):
  
  def ligar(self):
    return f"O carro ligou"
  
  def desligar(self):
    return  f"O carro desligou"
  
carro = Carro()
print(carro.ligar())
print(carro.desligar())  
    
  
    