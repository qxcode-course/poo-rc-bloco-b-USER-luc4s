class Chinela:
    def __init__(self, tamanho: int):
        self.tamanho = 0

    def getTamanho(self,valor: int):
        return self.tamanho
    
    def setTamanho(self, valor: int):
        if tamanho >= 20 and tamanho <= 50 and tamanho %2 == 0:
            self.tamanho += 1
chinela = Chinela()

while chinela.getTamanho() == 0:
    print("Insira o tamanho da sua chinela: ")
    tamanho = int(input())
    chinela.setTamanho(tamanho)
print(f"Parabens, você comprou uma chinela tamanho", {chinela.getTamanho})
     