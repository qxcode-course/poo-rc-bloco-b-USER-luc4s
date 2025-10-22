class Watch:
    def __init__(self):
        self.hora = 0
        self.minuto = 0
        self.segundo = 0
    
    def setHora(self, valor: int):
        if valor >= 0 and valor <= 23:
            self.hora = valor
        elif valor > 23:
            self.hora = 0
    
    def setMinuto(self, valor: int):
        if valor >= 0 and valor <= 59:
            self.minuto = valor
        elif valor == 60:
            self.setHora(1)
    
    def setSegundo(self, valor: int):
        if valor >= 0 and valor <= 59:
            self.segundo = valor
        elif valor == 60:
            self.setMinuto(1)
    
    def getHora(self):
        return self.hora
    
    def getMinuto(self):
        return self.minuto
    
    def getSegundo(self):
        return self.segundo
    
    def __str__(self) -> str:
        return  f"{self.hora:02d}: {self.minuto:02d}: {self.segundo:02d}"
    
def main():
    watch = Watch()
    while True:
        line = input()
        print(f"${line}")
        args = line.split(" ")
        
        if args[0] == "end":
            break
        elif args[0] == "init":
            watch = Watch(int(args[1]), int(args[2]), int(args[3]))
        elif args[0] == "set":
            watch.setHora(int(args[1]))
            watch.setMinuto(int(args[2]))
            watch.setSegundo(int(args[3]))