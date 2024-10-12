class Animal():
    def __init__(self, nome):
      self.nome = nome
      
    def emitir_som(self):
      pass
    
class Mamifero(Animal):
    
    def amamentar(self):
      return f"O {self.nome} está amamentando."

class Ave(Animal):
    def voar(self):
      return f"O {self.nome} está voando."
    
class Morcego(Mamifero, Ave):
    def emitir_som(self):
      return f"{self.nome} emitindo som."
    
morcego = Morcego("Batman")

  #Acessando os métodos da classe animal
print(f"Nome do morcego eh {morcego.nome}")
print(morcego.amamentar())
print(morcego.emitir_som())