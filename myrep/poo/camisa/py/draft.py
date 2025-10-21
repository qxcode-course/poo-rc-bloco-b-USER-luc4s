class Camisa:
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

roupa = Roupa()

while roupa.getTamanho() == "":
    print("Digite seu tamanho de roupa")
    tamanho = input()
    roupa.setTamanho(tamanho)

print("Parabens, você comprou uma roupa tamanho", roupa.getTamanho())