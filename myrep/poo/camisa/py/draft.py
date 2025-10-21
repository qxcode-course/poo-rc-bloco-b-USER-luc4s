<<<<<<< HEAD
class Roupa:
=======
class Camisa:
>>>>>>> b84b69d (Camisa)
    def __init__(self):
        self._tamanho: str = ""
    
    def getTamanho(self) -> str:
        return self._tamanho
    def setTamanho(self, valor: str):
        tamanhos_validos = ["P", "PP", "M", "G", "GG", "XG"]

        if valor in tamanhos_validos:
            self._tamanho = valor
            print(f"Tamanho definido como: {self._tamanho}")
        else:
            print(f"Tamanho inválido! Os tamanhos permitidos são: {', '.join(tamanhos_validos)}")
<<<<<<< HEAD
=======

>>>>>>> b84b69d (Camisa)
roupa = Roupa()

while roupa.getTamanho() == "":
    print("Digite seu tamanho de roupa")
    tamanho = input()
    roupa.setTamanho(tamanho)
<<<<<<< HEAD
    print("Parabens, você comprou uma roupa tamanho", roupa.getTamanho())
=======

print("Parabens, você comprou uma roupa tamanho", roupa.getTamanho())
>>>>>>> b84b69d (Camisa)
