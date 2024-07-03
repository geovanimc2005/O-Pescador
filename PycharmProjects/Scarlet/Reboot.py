import array, os, sys
import time, datetime
import MySQLdb as sq
import sqlite3 as sql
from tqdm import *
import random
import json, pickle
#Prazo de termino: 2000 linhas de codigo, Autor: Geovani Moura Coratti, 19 anos
class Reboot:
    def __init__(self):
        self.acionado = False
        self.nome = "Otto"
        self.input = input("Digite: ")
        self.contador = 0
        self.opções = ["Salvar", "Deletar", "Fechar"]
        self.elementos = ["Fogo", "Agua", "Terra", "Ar"]
        self.dicts = {0 : "Calor", 1 : "mutação", 2: "Pacividade", 3 : "Força e imponencia"}
        self.input_numerico = [str(input(f"Digite A operação Matematica {i}")) for i in ["+", "-", "*", "/"] if self.input == "Matematica"]
        self.count = 0
        self.correto = False
        self.chances = 0
        self.respostas = ["Não sei", "Dificil dizer"]
        self.enigmas = {"Como Resolver o meu problema?":"Como Vou saber", "Que dia é Hoje?" : "Problemas"}
    def fechar(self):
        return quit()
    def banco_de_dados(self):
        pass
    def charadas(self):
        respostas_input = str(input("Qual é a Resposta ? "))
        rand = random.randint(0, len(self.enigmas))
        print(self.enigmas[rand])
        for i, e in enumerate(self.enigmas.keys()):
            print(self.enigmas.keys())

    def analisador(self, elem : array):
        for i in elem:
            if i == elem[0]:
                print("Tudo ativado")
        try:
            if self.input == "Perguntas":
                self.charadas()
            if self.input == " ":
                print("Espaços vazios")
            for i in range(len(self.opções)):
                if self.input == self.opções[0]:
                    self.save()
                elif self.input == self.opções[2]:
                    self.fechar()
        except Exception as exc:
            print(exc)
    def save(self):
        with open("damocles", "w") as file:
            file.write(str(self.input))
            if file.close() is True:
                print("Ele Ainda não existe")
    def horas(self, dia_de_aniversario):
        date = datetime.date
        dados_de_tempo = ""
        if date.today().day == dia_de_aniversario:
            print(f"{date.today()}, então está de parabéns")
        else:
            if date.today().weekday() == "Monday":
                dados_de_tempo.join(date.day)
    def temporizador(self):
        if self.contador == 0:
            for i in range(len(self.elementos)):
                self.contador += 1
                time.sleep(2)
                if self.contador >= 20:
                    self.acionado = False
                    break
                if self.contador >= i and self.contador <= 30:
                    return True
                elif self.contador == 20:
                    return False
    def main(self):
        count = 0
        if self.temporizador():
            self.acionado = True
        while self.acionado:
            self.horas(27)
            count += 1
            self.analisador(self.elementos)
            if count == 5:
                self.acionado = False
                break

if __name__ == "__main__":
    reboot = Reboot()
    reboot.main()
