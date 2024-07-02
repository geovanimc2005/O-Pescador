import math, struct, ctypes, datetime
class Historinha(str):
    def __init__(self):
        self.array = []
        self.add = set()
        self.mensagem = ""
        self.ações_basicas = ["Andar", "Pescar", "Items"]
    def __add__(self, other):
        if not self.add.clear():
            self.add.add(other)
            return True
        else:
            print("Ainda não está bom")
    def situação_inicial(self, input):
        index = 0
        while len(self.ações_basicas) > 0:
            index += 1
            if input == self.ações_basicas[index]:
                print("Você Já tomou esta ação")
            for i in range(len(self.ações_basicas)):
                if input == self.ações_basicas[i]:
                    print("Boa")
                    return self
                elif input not in self.ações_basicas:
                    self.mensagem += "Nada Ainda"
        return self.mensagem
class Principal:
    def __init__(self):
        self.ativar = True
        self.maior = lambda x: x > 0
        self.historia = Historinha()
    def main(self):
        if self.ativar:
            while True:
                pass
if __name__ == "__main__":
    principal = Principal()
    principal.main()
