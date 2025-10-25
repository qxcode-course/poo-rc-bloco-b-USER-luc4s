class Watch:
    def __init__(self, hora=0, minuto=0, segundo=0):
        self.hora: int = 0
        self.minuto: int = 0
        self.segundo: int = 0
        self.setHora(hora)
        self.setMinuto(minuto)
        self.setSegundo(segundo)
    
    def setHora(self, valor: int):
        if valor >= 0 and valor <= 23:
            self.hora = valor
        elif valor > 24:
            print("fail: hora invalida")
        else:
            print("fail: hora invalida")
    
    def setMinuto(self, valor: int):
        if 0 <= valor <= 59:
            self.minuto = valor
        else:
            print("fail: minuto invalido")
    
    def setSegundo(self, valor: int):
        if 0 <= valor <= 59:
            self.segundo = valor
        else:
            print("fail: segundo invalido")

    def nextSegundo(self):
        self.segundo += 1
        if self.segundo == 60:
            self.segundo = 0
            self.minuto += 1
        if self.minuto == 60:
            self.minuto = 0
            self.hora += 1
        if self.hora == 24:
            self.hora = 0

    def __str__(self):
        return f"{self.hora:02d}:{self.minuto:02d}:{self.segundo:02d}"


def main():
    watch = Watch()

    while True:
        line = input()
        print(f"${line}")
        args = line.split()

        if args[0] == "end":
            break
        elif args[0] == "init":
            watch = Watch(int(args[1]), int(args[2]), int(args[3]))
        elif args[0] == "set":
            watch.setHora(int(args[1]))
            watch.setMinuto(int(args[2]))
            watch.setSegundo(int(args[3])) 
        elif args[0] == "show":
            print(watch)
        elif args[0] == "next":
            watch.nextSegundo()
        else:
            print("comando invalido")

main()
