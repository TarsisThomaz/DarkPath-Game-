from imports import *

running = True
jumping = False
sliding = False
attacking = False
at_ground = True
tempo_aa = 0

def player(slide,jump,run,attack,janela,teclado,py):
    vel_player = 400*janela.delta_time()
    mouse = Window.get_mouse()
    ###### MOVIMENTACAO HORIZONTAL DO JOGADOR ######
    if run.x >= 0 and run.x <= janela.width - run.width:

        if teclado.key_pressed("D"):
            run.move_x(vel_player)
        if teclado.key_pressed("A"):
            run.move_x(-vel_player)
        
        if run.x < 0:
            run.x = 0                        # OS FRAMES DA ANIMAÇÃO N POSSUEM EXATAMENTE O MESMO
        if run.x > janela.width - run.width: # TAMANHO, LOGO ESSA CORREÇÃO DE POSIÇÃO IMPEDE QUE
            run.x = janela.width - run.width # O PLAYER GRUDE NA PAREDE

    global running
    global jumping
    global sliding
    global attacking
    global at_ground

    if teclado.key_pressed("W") and jump.y + jump.height >= janela.height and not sliding: #segunda condicao impede pulo infinito
        running = False
        jump.set_curr_frame(0)
        jumping = True
        at_ground = False
        attacking = False

    if teclado.key_pressed("S") and at_ground and not attacking:
        run.hide()
        running = False
        sliding = True
    elif at_ground:
        running = True
        sliding = False

    if mouse.is_button_pressed(1):
        attacking = True
        running = False

    
    if jumping:
        run.hide()
        jump.draw()
        if jump.y + jump.width >= 600:
            jump.move_y(-vel_player*2)
        else:
            jumping = False
        try:
            jump.update()
        except IndexError:
            pass
    else:
        if jump.y < janela.height - jump.height:
            jump.draw()
            jump.move_y(vel_player*2)
        else:
            running = True
            at_ground = True
            #jump.y == run.y

    if not jumping and not sliding and not attacking:
        run.unhide()

    jump.x = run.x
    if running:
        run.y = py
        run.draw()
        run.update()

    slide.x = run.x + 30
    if sliding:
        run.y = py #- 50
        run.hide()
        slide.draw()

    if at_ground:
        run.y = py
    else:
        run.y = jump.y

    attack.x = run.x
    global tempo_aa
    if attacking and jump.y >= janela.height - jump.height:
        run.hide()
        attack.draw()
        attack.update()
        tempo_aa += janela.delta_time()
        if tempo_aa >= 0.3:
            attacking = False
            running = True
            tempo_aa = 0

    return attacking

def colisao_player_obstaculo(player,obstaculos2,lbarras,bolas,teclado,janela,escudo,vidas):
    global HIT
    global TEMPO_INVENCIVEL

    if HIT == False:
        for i in range(len(obstaculos2)): # colisao com os obstaculos terrestres
            if (player.x + 70 < obstaculos2[i].x + obstaculos2[i].width and
            player.x + player.width  - 70 > obstaculos2[i].x and
            player.y < obstaculos2[i].y + obstaculos2[i].height and
            player.y + player.height > obstaculos2[i].y):
                vidas -= 1
                HIT = True
                #return "menu",[],[],[]
        for i in range(len(lbarras)): # colisao com as barras penduradas
            if player.x + player.width -70 >= lbarras[i].x and player.x +70 <= lbarras[i].x + lbarras[i].width:
                if teclado.key_pressed("S"):
                    return "jogo",obstaculos2,lbarras,bolas,vidas
                else:
                    vidas -= 1
                    HIT = True
                    #return "menu",[],[],[]
        
        for i in range(len(bolas)):
            if player.collided(bolas[i]):
                vidas -= 1
                HIT = True
                #print(vidas)
                break
                #return "menu",[],[],[]
    else: #HIT == True
        TEMPO_INVENCIVEL += janela.delta_time()
        escudo.x = player.x-50
        escudo.y = player.y-20
        escudo.draw()
        if TEMPO_INVENCIVEL >= 3:
            TEMPO_INVENCIVEL = 0
            HIT = False

    if vidas == 0:
        return "menu",[],[],[],vidas
    
    return "jogo",obstaculos2,lbarras,bolas,vidas

def colisao_atck2Boss_player(player,atk,vidas,janela,escudo):
    global HIT
    global TEMPO_INVENCIVEL
    if HIT == False:
        for i in range(len(atk)):
            # if (player.x + 70 < atk[i].x + atk[i].width and
            #     player.x + player.width  - 70 > atk[i].x and
            #     player.y < atk[i].y + atk[i].height and
            #     player.y + player.height > atk[i].y):
            if (player.x + player.width - 60 < atk[i].x + atk[i].width and
                player.x + 60 > atk[i].x and
                player.y < atk[i].y + atk[i].height and
                player.y + player.height > atk[i].y + 90):

                vidas -= 1
                HIT = True
    
    else:
        TEMPO_INVENCIVEL += janela.delta_time()
        escudo.x = player.x-50
        escudo.y = player.y-20
        escudo.draw()
        if TEMPO_INVENCIVEL >= 3:
            TEMPO_INVENCIVEL = 0
            HIT = False

    return vidas


def reinicia(vidas, pontos):
    #obstaculos,obstaculos2,lbarras,bolas = [],[],[],[]
    if vidas == 0:
        vidas = 3
        pontos = 0

    return vidas,pontos

# def colisao_bossAtck1_player():
