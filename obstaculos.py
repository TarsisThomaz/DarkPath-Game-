from imports import *
from random import randint

rel = 0
rel2 = 0

def cria_obstaculos(janela,obstaculos,obstaculos2,lbarras,dif,pontos):
    global rel
    r = randint(1,3)
    rel += janela.delta_time()
    aumenta_dif = pontos
    if aumenta_dif >= 150:
        aumenta_dif = 150
    if dif == "easy":
        delay = 2 - aumenta_dif/200
    elif dif == "medium":
        delay = 1.5 - aumenta_dif/200
    elif dif == "hard":
        delay = 1 - aumenta_dif/200

    if rel >= delay: # soma pontos com o passar do tempo, dificuldades mais altas somam pontos mais rapido
        pontos += 1

    #obstaculos2 eh uma lista com sprites com uma hitbox que funciona melhor para o tamanho que eh desenhado da lista obstaculos
    if r == 1 and rel >= delay:
        spikes = Sprite("imagens/obstaculos/spikes.png")
        spikes2 = Sprite("imagens/obstaculos/spikes2.png")
        spikes.x = janela.width -50
        spikes.y = janela.height - spikes.height
        spikes2.x = spikes.x + spikes2.width/2 - 30
        spikes2.y = spikes.y + spikes.height/2
        obstaculos.append(spikes)
        obstaculos2.append(spikes2)
        rel = 0
    elif r == 2 and rel >= delay:
        blade = Sprite("imagens/obstaculos/blade.png")
        blade2 = Sprite("imagens/obstaculos/blade2.png")
        blade.x = janela.width -50
        blade.y = janela.height - blade.height/2
        blade2.x = blade.x + blade2.width/2 - 30
        blade2.y = blade.y + 50
        obstaculos.append(blade)
        obstaculos2.append(blade2)
        rel = 0
    elif r == 3 and rel >= delay:
        barra = Sprite("imagens/obstaculos/barra.png")
        barra.x = janela.width -50
        barra.y = -160
        obstaculos.append(barra)
        lbarras.append(barra) # lista para tratar a colisao das barras de forma diferentes aos outros obstaculos
        rel = 0
    
    return obstaculos,obstaculos2,lbarras,pontos

def desenha_obstaculos(obstaculos,janela,obstaculos2,lbarras,dif,pontos):
    
    aumenta_dif = pontos
    if aumenta_dif >= 150:
        aumenta_dif = 150

    if dif == "easy":
        vel_obstaculo = (-500 - 2*aumenta_dif) * janela.delta_time()
    elif dif == "medium":
        vel_obstaculo = (-600 - 2*aumenta_dif) * janela.delta_time()
    elif dif == "hard":
        vel_obstaculo = (-700 - 2*aumenta_dif) * janela.delta_time()

    for i in range(len(obstaculos)): # MOVE E DESENHA OS OBSTACULOS
        obstaculos[i].draw()
        obstaculos[i].move_x(vel_obstaculo)
    for i in range(len(obstaculos2)): # LISTA DAS HITBOXES ACOMPANHA O OBSTACULO REAL
        obstaculos2[i].move_x(vel_obstaculo)
    for i in range(len(lbarras)):
        lbarras[i].move_x(vel_obstaculo/2) #MOVE INDIVIDUALMENTE AS BARRAS FAZENDO ELAS SEREM MAIS RAPIDAS QUE OS OUTROS OBSTACULOS

def cria_bolas(bolas,janela,dif):
    global rel2
    rel2 += janela.delta_time()

    if dif == "easy":
        delay = 2
    elif dif == "medium":
        delay = 1.5
    elif dif == "hard":
        delay = 1

    if rel2 > delay:
        x = randint(50,janela.width-200)
        bola = Sprite("imagens/obstaculos/bola-de-fogo.png")
        bola.x = x
        bola.y = -bola.height
        bolas.append(bola)
        rel2 = 0
    
    return bolas

def desenha_bolas(bolas,janela):
    vel_bolas = 500 * janela.delta_time()
    for i in range(len(bolas)):
        bolas[i].draw()
        bolas[i].move_y(vel_bolas)