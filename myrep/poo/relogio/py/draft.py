class Watch:
    def __init__(self, hora=0, minuto=0, segundo=0):
        self.hora = hora
        self.minuto = minuto
        self.segundo = segundo
    
    def setHora(self, valor: int):
        if 0 <= valor <= 23:
            self.hora = valor
        else:
            self.hora = 0
    
    def setMinuto(self, valor: int):
        if 0 <= valor <= 59:
            self.minuto = valor
        else:
            self.minuto = 0
    
    def setSegundo(self, valor: int):
        if 0 <= valor <= 59:
            self.segundo = valor
        else:
            self.segundo = 0

    def nextSegundo(self):
        self.segundo += 1
        if self.segundo >= 60:
            self.segundo = 0
            self.minuto += 1
            if self.minuto >= 60:
                self.minuto = 0
                self.hora += 1
                if self.hora >= 24:
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
