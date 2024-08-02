import pygame

#===================================================

# Iniciar o jogo com pygame.init

#===================================================

pygame.init()

#===================================================
#                  Configurações de tela

tamanho_tela = (800,800)
tela = pygame.display.set_mode(tamanho_tela)

#===================================================
#                  Titulo

Titulo_jogo = "Jogo da bolinha"
pygame.display.set_caption(Titulo_jogo)

#===================================================
#                  Elementos

tamanho_bola = 15
bola = pygame.Rect(100,500,tamanho_bola,tamanho_bola)
tamanho_jogador = 100
jogador = pygame.Rect(0,700,tamanho_jogador, 15)

qtde_de_blocos_por_linha = 8
qtde_de_linhas = 5
qtde_total_de_blocos = qtde_de_blocos_por_linha * qtde_de_linhas

#===================================================

#           Funçoes ( Funcionalidades e movimentos )

#===================================================

def criar_blocos(qtde_de_blocos_por_linha,qtde_de_linhas):
    altura_tela = tamanho_tela[1]
    largura_tela = tamanho_tela[0]
    distancia_entre_blocos = 10
    largura_bloco = (largura_tela / 8) - distancia_entre_blocos
    altura_bloco = 15
    distancia_entre_linhas = altura_bloco + 10

    blocos=[]

    for i2 in range(qtde_de_linhas):
        for i in range(qtde_de_blocos_por_linha):
            bloco = pygame.Rect(i * (largura_bloco + distancia_entre_blocos),i2 * distancia_entre_linhas,largura_bloco,altura_bloco)
            blocos.append(bloco)
    
    return blocos

def criar_tela_inicial_do_jogo():
    tela.fill(cores["preto"])
    pygame.draw.rect(tela,cores["azul"],jogador)
    pygame.draw.rect(tela,cores["branco"],bola)

def desenhar_blocos(blocos):
    for bloco in blocos:
        pygame.draw.rect(tela,cores["vermelho"],bloco)

def movimentar_jogador(event):
    if event.type == pygame.KEYDOWN:
        if event.key == pygame.K_RIGHT:
            if (jogador.x + tamanho_jogador) < tamanho_tela[0]:
                jogador.x = jogador.x + 3
        if event.key == pygame.K_LEFT:
            if jogador.x > 0:
                jogador.x = jogador.x - 3
            
def movimentar_bola(bola):
    movimento = movimento_bola
    bola.x = bola.x + movimento[0]
    bola.y = bola.y + movimento[1]

    if bola.x <= 0:
        movimento[0] = - movimento[0]

    if bola.y <= 0:
        movimento[1] = - movimento[1]

    if  (bola.x + tamanho_bola) >= tamanho_tela[0]:
        movimento[0] = - movimento[0]

    if  (bola.y + tamanho_bola) >= tamanho_tela[1]:
        movimento = None

    if jogador.collidepoint(bola.x,bola.y):
        movimento[1] = - movimento[1]

    for bloco in blocos:
        if bloco.collidepoint(bola.x,bola.y):
            blocos.remove(bloco)
            movimento[1] = - movimento[1]

    return movimento

def atualizar_pontuacao(pontuacao):
    fonte = pygame.font.Font(None, 30)
    texto = fonte.render(f"Pontos: {pontuacao}",1,cores["verde"])
    tela.blit(texto,(0,770))
    if pontuacao >= qtde_total_de_blocos:
        return True
    else:
        return False

#===================================================

#                    Cores 

#===================================================

cores = {
    "branco":(255,255,255),
    "preto":(0,0,0),
    "verde":(0,255,0),
    "vermelho":(255,0,0),
    "azul":(0,0,255),
}

#===================================================
#                  Configurações de jogo

game_over = False
pontuacao = 0
movimento_bola = [2,-1]

#===================================================

#                    Tela do jogo

#===================================================

blocos = criar_blocos(qtde_de_blocos_por_linha,qtde_de_linhas)

while not game_over:
    criar_tela_inicial_do_jogo()
    desenhar_blocos(blocos)
    game_over = atualizar_pontuacao(qtde_total_de_blocos - len(blocos))
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            game_over = True
    movimentar_jogador(evento)
    movimento_bola = movimentar_bola(bola)
    if not movimento_bola:
        game_over = True
        
    pygame.time.wait(1)
    pygame.display.flip()


#===================================================

# Encerrar o jogo com pygame.quit

#===================================================

pygame.quit()