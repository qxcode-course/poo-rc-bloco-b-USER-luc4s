class Roupa:
    def __init__(self):
        self._tamanho: str = ""
    
    def __str__(self) -> str:
       
        return f"size: ({self._tamanho})"
    def getTamanho(self) -> str:
        return self._tamanho
    def setTamanho(self, valor: str):
        tamanhos_validos = ["PP", "P", "M", "G", "GG", "XG"]

        if valor in tamanhos_validos:
            self._tamanho = valor
        else:
            print("fail: Valor inválido, tente PP, P, M, G, GG ou XG")
    
def main():
    roupa = Roupa()

    while True :
        line = input("")
        print(f"${line}")
        args = line.split(' ')
        if args[0] == "end":
            break
        elif args[0] == "size":
            roupa.setTamanho(args[1])
        elif args[0] == "show":
            print(roupa)
        else:
            print("comando invalido")
main()