#Classe
class Pessoa:
  def __init__(self, nome, idade):
    self.nome = nome
    self.idade = idade
    
  def saudacao(self):
    return f"Olá! Meu nome é {self.nome} e tenho {self.idade} anos."
  
#Objeto
pessoa1 = Pessoa("Arthur", 24)
pessoa2 = Pessoa("Math", 27)

print(f"Nome da pessoa1 é {pessoa1.nome}")
print(pessoa1.saudacao())
print(pessoa2.saudacao())  