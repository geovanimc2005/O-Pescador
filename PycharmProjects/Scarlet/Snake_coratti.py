import pygame
import random
import time
import math
#Jogo programado por mim, Porém eu não criei nem detenho direitos sobre a criação "Snake", este jogo foi criado apenas por diversão em questão de uma hora... por favor, não entendam errado
#Jogo Originalmente criado por Dave Bresnin, da empresa Gremlin em 1982
class Program:
    def __init__(self):
        pygame.init()
        self.width = 300
        self.height = 300
        self.window = pygame.display.set_mode((self.width, self.height))
        pygame.display.set_caption("Snake")
        self.running = True
        self.x = 30
        self.y = 30
        self.w = 30
        self.h = 30
        self.corrida = pygame.Rect([self.x,self.y,self.w,self.h])
        self.x_array = [0,0,0,0]

        self.colisão = False
        self.keys = pygame.key.get_pressed()
        self.clock = pygame.time.Clock()
        self.maca = None
        self.macas = []
        self.xx = random.randint(0, self.width)
        self.yy = random.randint(0, self.height)
        self.coor_maça = [random.randint(0, self.width), random.randint(0, self.height)]
    def maça(self):
        self.maca = pygame.draw.rect(self.window, (200, 20, 20), (self.xx, self.yy, 30,30))
        return self.maca
    def cobra(self):
        keys = pygame.key.get_pressed()
        for i in range(len(self.x_array)):
            if keys[pygame.K_d]:
                self.corrida.x += 1
            if keys[pygame.K_s]:
                self.corrida.y -= 1
            if keys[pygame.K_a]:
                self.corrida.x -= 1
            if keys[pygame.K_w]:
                self.corrida.y += 1
            if keys[pygame.K_l]:
                self.x_array[i] += 1
            pygame.draw.rect(self.window, (20, 200, 20), (self.corrida.x, self.corrida.y, self.x_array[i] + 30, self.x_array[i] + 40))
            if self.corrida.x == self.xx or self.corrida.y == self.yy:
                self.x_array[i] += 10
                self.xx = random.randint(0, self.width)
                self.yy = random.randint(0, self.height)
    def main(self):
        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    quit()
            self.cobra()
            self.maça()
            pygame.display.update()
            self.window.fill((0,0,0))
            self.clock.tick(60)
if __name__ == "__main__":
    program = Program()
    program.main()
