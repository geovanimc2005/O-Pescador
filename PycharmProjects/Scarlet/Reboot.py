import array, os, sys
import time
from MySQLdb import *
class Reboot:
    def __init__(self):
        self.acionado = False
        self.input = input("Digite: ")
        self.contador = 0
        self.elementos = ["Fogo", "Agua", "Terra", "Ar"]
        self.dicts = {0 : "Calor", 1 : "mutação", 2: "Pacividade", 3 : "Força e imponencia"}
    def analisador(self, elem : array):
        for i in elem:
            if i == elem[0]:
                print("Tudo ativado")
    def temporizador(self):
        if self.contador == 0:
            for i in range(len(self.elementos)):
                self.contador += 1
                if self.contador >= 20:
                    self.acionado = False
                    break
                if self.contador >= i and self.contador <= 30:
                    return True
                elif self.contador == 20:
                    return False
    def main(self):
        if self.temporizador():
            self.acionado = True
        while self.acionado:
            self.analisador(self.elementos)
            if self.contador >= 10 and self.acionado:
                self.acionado = False
                break

if __name__ == "__main__":
    reboot = Reboot()
    reboot.main()