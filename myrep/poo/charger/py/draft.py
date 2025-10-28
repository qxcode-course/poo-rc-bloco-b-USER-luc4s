class Notebook:
    def __init__(self):
        self._ligado: bool = False
        self._bateria: Bateria

    def ligar(self):
        if not self._ligado:
            self._ligado = True
            print("Notebook: ligado")
        else:
            print("Notebook: desligado")
    
    def desligar(self):
        if self._ligado:
            self._ligado = False
            print("Notebook: desligado")
        else:
            print("Notebook: ja esta desligado")

    def mostrar(self):
        if self._ligado:
            status = "Ligado"
        else:
            status = "Desligado"
        print(f"Status: {status}")
    
    def usar(self, valor: int):
        if self._ligado:
            self.gastar_bateria(valor)
        else:
            print("Notebook: esta desligado, nao pode usar")
