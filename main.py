from imports import *
from player import *
from menu import *
from obstaculos import *
from boss import *

janela = Window(1600,900)
teclado = Window.get_keyboard()
janela.set_title("Dark Path")

os.chdir('C:/Users/T-Gamer/Desktop/CODES/VS code/LabJogos/ProjetoDarkPath')

player_running = Sprite("imagens/player/run.png",9)
player_running.set_total_duration(800)
player_running.x = 100
player_running.y = janela.height - player_running.height
py = janela.height - player_running.height

player_jump = Sprite("imagens/player/jumpp.png",7)
player_jump.set_total_duration(800)
player_jump.x = player_running.x
player_jump.y = player_running.y

player_sliding = Sprite("imagens/player/slide.png")
player_sliding.x = player_running.x
player_sliding.y = player_running.y + 50

player_attack = Sprite("imagens/player/attack3.png",6)
player_attack.set_total_duration(300)
player_attack.x = player_running.x
player_attack.y = player_running.y - 50

boss_final = Sprite("imagens/bosses/boss-final.png",8)
boss_final.x = janela.width - boss_final.width
boss_final.y = janela.height - boss_final.height
boss_final.set_total_duration(600)
protecao = Sprite("imagens/bosses/protecao.png",8)
protecao.set_total_duration(600)
protecao.x = boss_final.x - protecao.width - 10
protecao.y = janela.height - protecao.height

fundo = Sprite("imagens/fundo2.png")
fundo2 = Sprite("imagens/fundo2.png")
fundo.x = 0
fundo.y = 0
fundo2.x = 0
fundo2.y = 0
fx = 0

obstaculos = []
obstaculos2 = []
lbarras = []
bolas = []
boss_atck1 = []
boss_atck2 = []
pontos = 1
nVidas = 3

music_menu = Sound("musicas/Menu-Music.ogg")
music_fase = Sound("musicas/In-game-Running-music.ogg")
music_boss = Sound("musicas/Blackmoor-Colossus-Loop.ogg")
music_boss.set_repeat(True)
music_boss.set_volume(15)
music_fase.set_volume(5)
music_menu.set_repeat(True)
music_fase.set_repeat(True)

escudo = Sprite("imagens/escudo.png")

controle = "menu"
dif = "medium"
boss = False
rebate_ataque_boss = False
vida_boss_incremento = 20 # 20
vida_boss = vida_boss_incremento
fase_boss = 1
perdeu = False
ult_pontuacao = 0

while True:
    if controle == "menu":
        music_boss.stop()
        music_fase.stop()
        music_menu.play()
        controle, dif = menu(janela,perdeu,ult_pontuacao)
        nVidas,pontos = reinicia(nVidas,pontos)

        #obstaculos = []
    elif controle == "jogo":
        ### DESENHA FUNDO ###
        rel_x = fx % fundo.width
        fundo.x = rel_x - fundo.width
        if rel_x < janela.width:
            fundo2.x = rel_x
            fundo2.draw()
        fx -= 500 * janela.delta_time()
        fundo.draw()

        ### DESENHA PLAYER ###
        rebate_ataque_boss = player(player_sliding,player_jump,player_running,player_attack,janela,teclado,py)

        janela.draw_text("PONTOS: %d"%pontos,10,10,20,color=(150,150,150),font_name="Arial",bold=True)
        janela.draw_text("VIDAS RESTANTES: %d"%nVidas,10,30,20,color=(150,0,0),font_name="Arial",bold=True)

        if boss == False: # FASE
            boss = inicia_boss(pontos)
            ### MUSICA ###
            music_menu.stop()
            music_boss.stop()
            music_fase.play()

            ### DESENHA OBSTACULOS ###
            obstaculos,obstaculos2,lbarras,pontos = cria_obstaculos(janela,obstaculos,obstaculos2,lbarras,dif,pontos)
            bolas = cria_bolas(bolas,janela,dif)
            desenha_obstaculos(obstaculos,janela,obstaculos2,lbarras,dif,pontos)
            controle,obstaculos2,lbarras,bolas,nVidas = colisao_player_obstaculo(player_running,obstaculos2,lbarras,bolas,teclado,janela,escudo,nVidas)
            desenha_bolas(bolas,janela)
        elif boss == True: # LUTA BOSS
            music_fase.stop()
            music_menu.stop()
            music_boss.play()
            desenha_bossf(boss_final)
            boss_atck1,boss_atck2 = ataques_boss(boss_atck1,boss_atck2,protecao,dif,janela,boss_final,pontos)
            nVidas = rebate_ataque(player_running,rebate_ataque_boss,boss_atck1,janela,nVidas)
            vida_boss,pontos = colisao_rebatida_boss(boss_atck1,boss_final,vida_boss,janela,pontos)
            nVidas = colisao_atck2Boss_player(player_running,boss_atck2,nVidas,janela,escudo)
            if vida_boss == 0:
                fase_boss += 1
                vida_boss = vida_boss_incremento * fase_boss
                obstaculos2 = []
                obstaculos = []
                lbarras = []
                bolas = []
                boss_atck1 = []
                boss_atck2 = []
                boss = False

        if teclado.key_pressed("ESC"):
            controle = "menu"

        if nVidas == 0:
            perdeu = True
            ult_pontuacao = pontos
            obstaculos2 = []
            obstaculos = []
            lbarras = []
            bolas = []
            boss_atck1 = []
            boss_atck2 = []
            controle = "menu"
            

        janela.update()