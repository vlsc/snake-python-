import pygame
import func
from pygame.locals import *
# inicializando tudo que necessita de inicialização no pygame
pygame.init()
# setando uma tela com tamanho 600x600
screen = pygame.display.set_mode((600, 600))
# definindo o nome da janela
pygame.display.set_caption('Snake')
# cores úteis:
BLACK = [0, 0, 0]
WHITE = [255, 255, 255]
# instanciando o clock para controle de fps
clock = pygame.time.Clock()
# definindo fontes e seus tamanhos
font = pygame.font.SysFont('couriernew',55)
little = pygame.font.SysFont('couriernew', 20)
hscore = pygame.font.SysFont('couriernew', 25)
score = pygame.font.SysFont('couriernew', 35)

# definindo a cobra inicial
snake = [(200, 200), (210, 200), (220, 200)]
snake_skin = pygame.Surface((10, 10))
snake_skin.fill([255, 255, 255])
# definindo a maçã
apple = pygame.Surface((10, 10))
apple.fill([255, 0, 0])
# a função intrand() serve para que sempre se tenha um valor aleatório multiplo de 10
ax = func.intRand()
ay = func.intRand()
# a posição da maçã é sempre gerada aleatoriamente
posapple = (ax, ay)
# definições úteis
UP = 1
RIGHT = 2
DOWN = 3
LEFT = 4
# a variável ant serve para que a cobra não faça um movimento exatamente oposto ao seu atual
ant = RIGHT
# a variável flag ajuda a saber quando o jogo acabou
flag = 0
# direção inicial
d = RIGHT
# a variável cont nos ajuda a saber quando a cobra bateu em si mesma
cont = 0
# a variável pontos é o score do jogador
pontos = 0
# a variável record vai receber a maior pontuação
record = func.getScore()


while True:
    # definindo o fps
    clock.tick(10)
    # capturando os eventos
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
        if event.type == KEYDOWN:
            if event.key == K_UP:
                if ant != DOWN:
                    d = UP
                    ant = UP
            if event.key == K_DOWN:
                if ant != UP:
                    d = DOWN
                    ant = DOWN
            if event.key == K_LEFT:
                if ant != RIGHT:
                    d = LEFT
                    ant = LEFT
            if event.key == K_RIGHT:
                if ant != LEFT:
                    d = RIGHT
                    ant = RIGHT
            # este funciona apenas quando o jogo é terminado e é perguntado se o jogador deseja
            # jogar novamente
            if event.key == K_SPACE:
                if flag == 1:
                    flag = 0
                    pontos = 0
                    cont = 0
                    d = RIGHT
                    screen.fill([0, 0, 0])
                    snake = [(200, 200), (210, 200), (220, 200)]
                    for pos in snake:
                        screen.blit(snake_skin, pos)

    # checa se comeu a maçã
    if func.eat(snake, ax, ay):
        pontos += 1
        snake.append((0, 0))
        ax = func.intRand()
        ay = func.intRand()
        posapple = (ax, ay)

    # verifica se houve colisão com os limites da tela
    if snake[0][0] > 590 or snake[0][0] < 0:
        flag = 1
    if snake[0][1] > 590 or snake[0][1] < 0:
        flag = 1

    if flag != 1:
        for i in range(len(snake) - 1, 0, -1):
            if snake[0] == snake[i]:
                cont += 1
                # verifica se houve colisão entre a cobra e ela mesma
                if cont >= 2:
                    flag = 1
                    break

    for i in range(len(snake) - 1, 0, -1):
        snake[i] = (snake[i-1][0], snake[i-1][1])

    if flag != 1:
        if d == UP:
            snake[0] = (snake[0][0], snake[0][1] - 10)
        if d == DOWN:
            snake[0] = (snake[0][0], snake[0][1] + 10)
        if d == LEFT:
            snake[0] = (snake[0][0] - 10, snake[0][1])
        if d == RIGHT:
            snake[0] = (snake[0][0] + 10, snake[0][1])
        screen.fill(BLACK)
        screen.blit(apple, posapple)
        for pos in snake:
            screen.blit(snake_skin, pos)
    else:
        # verifica se a pontuação feita ultrapassa a maior pontuação
        if pontos > record:
            # se sim, coloca o novo record no arquivo
            record = pontos
            func.setScore(pontos)
        # printa os textos necessários no fim do game
        text = font.render('Game Over', True, [255, 255, 255])
        screen.blit(text, [145, 250])
        text = little.render('Press START to play again', True, [255, 255, 255])
        screen.blit(text, [145, 500])
        text = score.render(f'Score: {pontos}', True, [255, 255, 255])
        screen.blit(text, [210, 200])
        text = hscore.render(f'High Score: {record}', True, [255, 255, 255])
        screen.blit(text, [10, 0])
    # faz um update a cada ciclo do While
    pygame.display.update()