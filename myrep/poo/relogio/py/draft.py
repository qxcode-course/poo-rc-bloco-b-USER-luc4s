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
    def nextSegundo(self):
        self.segundo += 1
        if(self.segundo >=60):
            self.minuto +=1
            self.segundo = 0
            if(self.minuto >=60):
                self.hora +=1
                self.minuto=0
                if(self.hora >= 24):
                    self.hora = 0

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
            watch.set.Hora(int(args[1]))
            watch.set.Minuto(int(args[2]))
            watch.set.Segundo(int(args[3])) 
        elif args[0] == "show":
            print(watch)
        elif args[0] == "next":
            watch.nextSegundo()
        else:
            print("comando invalido")
main()