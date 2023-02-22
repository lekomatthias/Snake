import pygame
from pygame.locals import *
from random import randrange

def main():

    def hit(pos):
        if pos[0]>=largura or pos[0]<0 or pos[1]>=altura or pos[1]<0:
            return True
        else:
            return False

    def back(pos):
        if pos[0]>=largura:
            return [0, pos[1]]
        elif pos[0]<0:
            return [largura-pix, pos[1]]
        elif pos[1]>=altura:
            return [pos[0], 0]
        elif pos[1]<0:
            return [pos[0], altura-pix]
        else:
            return pos

    def snake(cobra):
        for xy in cobra:
            pygame.draw.rect(tela, Verde, [xy[0], xy[1], pix, pix])

    def apple(ax, ay):
        pygame.draw.rect(tela, Vermelho, [ax, ay, pix, pix])

    def text(msg, cor):
        texto1 = font.render(msg, True, cor)
        tela.blit(texto1, [int(largura/12*3), int(altura/2)])

    def playing():
        pos = [int(largura/2), int(altura/2)]
        direx = 0
        direy = 0
        cobrab = []
        tam = 1
        apple_pos = [randrange(0, largura-pix, pix), randrange(0, altura-pix, pix)]
        sair = False
        FimDeJogo = False

        while sair != True:
            
            while FimDeJogo == True:
                tela.fill(Preto)
                text("Fim de jogo, deseja continuar?[s/n]", Vermelho)
                pygame.display.update()
                for event in pygame.event.get():
                    if event.type is pygame.QUIT:
                        sair = True
    
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_s:
                            pos = [int(largura/2), int(altura/2)]
                            direx = 0
                            direy = 0
                            cobrab = []
                            tam = 1
                            apple_pos = [randrange(0, largura-pix, pix), randrange(0, altura-pix, pix)]
                            sair = False
                            FimDeJogo = False
                        if event.key == pygame.K_n:
                            sair = True
                            FimDeJogo = False
                        if event.key == pygame.K_ESCAPE:
                            sair = True
                            FimDeJogo = False

            if sair is True:
                continue
            timer.tick(fps)
            tela.fill(Marrom)
            apple(apple_pos[0], apple_pos[1])
            cobra = []
            cobra.append(pos[0])
            cobra.append(pos[1])
            cobrab.append(cobra)
            snake(cobrab)
            if len(cobrab) >= tam:
                del cobrab[0]
            if any(bloco == cobra for bloco in cobrab[:-1]):
                FimDeJogo = True
            if pos == apple_pos:
                apple_pos = [randrange(0, largura-pix, pix), randrange(0, altura-pix, pix)]
                tam += 1
        
            for event in pygame.event.get():
                if event.type is QUIT:
                    sair = True

                
                if event.type == pygame.KEYDOWN:
                    if event.key is pygame.K_ESCAPE:
                        sair = True
                    if event.key == pygame.K_LEFT and direx != pix:
                        direx = -pix
                        direy = 0
                    if event.key == pygame.K_RIGHT and direx != -pix:
                        direx = pix
                        direy = 0
                    if event.key == pygame.K_UP and direy != pix:
                        direx = 0
                        direy = -pix
                    if event.key == pygame.K_DOWN and direy != -pix:
                        direx = 0
                        direy = pix

            pos[0] += direx
            pos[1] += direy
            if hit(pos):
                pos = back(pos)
            pygame.display.update()

    pygame.init()

    largura = 640
    altura = 480
    pix = int(10)
    Marrom = (150, 100, 50)
    Verde = (0, 255, 0)
    Vermelho = (255, 0, 0)
    Preto = (0, 0, 0)
    tela = pygame.display.set_mode((largura, altura))
    pygame.display.set_caption('Snake')
    timer = pygame.time.Clock()
    fps = 30
    pygame.font.init()
    font = pygame.font.SysFont(None, 25)

    playing()

    pygame.font.quit()
    pygame.quit()

main()