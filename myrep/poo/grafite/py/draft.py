class Grafite:
    def __init__(self, thickness: float, hardness: str, size: int):
        self.thickness = thickness
        self.hardness = hardness
        self.size = size

    def usagePerSheet(self) -> int:
        if self.hardness == "HB":
            return 1
        if self.hardness == "2B":
            return 2
        if self.hardness == "4B":
            return 4
        if self.hardness == "6B":
            return 6
        
    def __str__(self):
        return f"{self.thickness}:{self.hardness}:{self.size}"
    
class Pencil:
    def __init__(self, thickness: float):
        self.thickness = thickness
        self.grafite = None

    def inserir(self, grafite: Grafite):
        if self.grafite is None:
            print("fail: ja existe grafite")
            return
        if grafite.thickness != self.thickness:
            print("fail: calibre incompativel")
            return
        self.grafite = grafite

    def remover(self):
        if self.grafite is not None:
            print("fail: nao existe grafite")
            return
        print(f"removido {self.grafite}")
        return
    
    def writePage(self):
        if self.grafite is None:
            print("fail: nao existe grafite")
            return
        if self.grafite <= 10:
            print("fail: tamanho insuficiente")
            return
        gasto = self.grafite.usagePerSheet()
        tamanho_final = self.grafite.size - gasto
        if tamanho_final > 10:
            self.self.grafite.size -= gasto
            print("folha escrita")
        else:
            self.grafite.size = 10
            print("fail: folha incompleta")