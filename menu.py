from imports import *
 
dificuldade = "medium"

def menu(janela,perdeu,ult_pontuacao):
    #Inicializacao
    mouse = Window.get_mouse()
    fundo = GameImage("imagens/fundo2.png")
    play_button = Sprite("imagens/buttons/DP_PLAY.png")
    level_button = Sprite("imagens/buttons/DP_DIFFICULTY.png")
    quit_button = Sprite("imagens/buttons/DP_QUIT.png")
    easy_button = Sprite("imagens/buttons/DP_EASY.png")
    medium_button = Sprite("imagens/buttons/DP_MEDIUM.png")
    hard_button = Sprite("imagens/buttons/DP_HARD.png")
    back_button = Sprite("imagens/buttons/DP_BACK.png")
    title = Sprite("imagens/DP_TITLE.png")


    #Posicoes dos botoes
    play_button.x = janela.width/2 - 300
    play_button.y = janela.height -335

    level_button.x = janela.width/2 - 170
    level_button.y = janela.height -225

    quit_button.x = janela.width/2 - 170
    quit_button.y = janela.height - 115

    easy_button.x = janela.width/2 - 170
    easy_button.y = janela.height/2 - 140

    medium_button.x = janela.width/2 - 170
    medium_button.y = janela.height/2 - 30

    hard_button.x = janela.width/2 - 150
    hard_button.y = janela.height/2 + 80

    back_button.x = 10
    back_button.y = 10

    title.x = janela.width/2 - 370
    title.y = 100

    c_menu = "home"

    #Menu Loop
    while (True):
        #Menu State
        global dificuldade
        if c_menu == "home": # HOME DO MENU
            fundo.draw()
            play_button.draw()
            level_button.draw()
            quit_button.draw()
            if perdeu:
                janela.draw_text("ÚLTIMA PONTUAÇÃO: %d"%ult_pontuacao,janela.width/2-220,50,40,color=(150,0,0),font_name="Arial",bold=True)
            title.draw()
            if mouse.is_over_object(play_button):
                play_button.x = janela.width/2 - 160 #destaca botao quando mouse esta em cima
                if mouse.is_button_pressed(1):
                    c_menu = "play"
            elif mouse.is_over_object(level_button):
                level_button.x = janela.width/2 - 160 #destaca botao quando mouse esta em cima
                if mouse.is_button_pressed(1):
                    c_menu = "level"
            elif mouse.is_over_object(quit_button):
                quit_button.x = janela.width/2 -160 #destaca botao quando mouse esta em cima
                if mouse.is_button_pressed(1):
                    c_menu = "quit"
            else:
                #encerra o destaque dos botoes quando o mouse nao esta mais em cima deles
                play_button.x = janela.width/2 - 180 
                level_button.x = janela.width/2 - 180
                quit_button.x = janela.width/2 - 180

        elif c_menu == "play":
            return "jogo", dificuldade #esse retorno interfere na variavel de controle de jogo da main

        elif c_menu == "level": # TELA DE ESCOLHA DA DIFICULDADE
            fundo.draw()
            easy_button.draw()
            medium_button.draw()
            hard_button.draw()
            if mouse.is_over_object(easy_button):
                easy_button.x = janela.width/2 - 130  #destaca botao quando mouse esta em cima
                if mouse.is_button_pressed(1):
                    dificuldade = "easy"
                    c_menu = "home"
            elif mouse.is_over_object(medium_button):
                medium_button.x = janela.width/2 - 130 #destaca botao quando mouse esta em cima
                if mouse.is_button_pressed(1):
                    dificuldade = "medium"
                    c_menu = "home"
            elif mouse.is_over_object(hard_button):
                hard_button.x = janela.width/2 - 130 #destaca botao quando mouse esta em cima
                if mouse.is_button_pressed(1):
                    dificuldade = "hard"
                    c_menu = "home"
            else:
                #encerra o destaque dos botoes quando o mouse nao esta mais em cima deles
                easy_button.x = janela.width/2 - 150
                medium_button.x = janela.width/2 - 150
                hard_button.x = janela.width/2 - 150
        

        elif c_menu == "quit":
            quit()
        janela.update()