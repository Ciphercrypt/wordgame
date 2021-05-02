import pygame
import random
import time

pygame.init()
WIDTH = 800
HEIGHT = 600
black = (100, 100, 100)
gameScreen = pygame.display.set_mode((WIDTH, HEIGHT))  
pygame.display.set_caption('wordgame by avishkar mohite')
background = pygame.image.load('main.png')
background = pygame.transform.scale(background, (WIDTH, HEIGHT)) 
font = pygame.font.Font('comic.ttf', 40)

word_speed = 0.5
score = 0


def new_word():
    global showword, newword, x_cor, y_cor, text, word_speed
    x_cor = random.randint(300, 700)  
    y_cor = 200  # y-cor
    word_speed += 0.10
    newword = ''
    words = open("wordlist.txt").read().split(', ')
    showword = random.choice(words)


new_word()

font_name = pygame.font.match_font('comic.ttf')


def draw_text(display, text, size, x, y):
    font = pygame.font.Font(font_name, size)
    text_surface = font.render(text, True, black)
    text_rect = text_surface.get_rect()
    text_rect.midtop = (x, y)
    gameScreen.blit(text_surface, text_rect)


def game_front_screen():
    gameScreen.blit(background, (0, 0))
    if not game_over:
        draw_text(gameScreen, "GAME OVER!", 90, WIDTH / 2, HEIGHT / 4)
        draw_text(gameScreen, "Score : " + str(score), 70, WIDTH / 2, HEIGHT / 2)
    else:
        draw_text(gameScreen, "Press any key to begin!", 54, WIDTH / 2, 500)
    pygame.display.flip()
    waiting = True
    while waiting:

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
            if event.type == pygame.KEYUP:
                waiting = False


# main loop
game_over = True
game_start = True
while True:
    if game_over:
        if game_start:
            game_front_screen()
        game_start = False
    game_over = False

    background = pygame.image.load('background.jpg')
    background = pygame.transform.scale(background, (WIDTH, HEIGHT))
    character = pygame.image.load('char.jpg')
    character = pygame.transform.scale(character, (50, 50))
    wood = pygame.image.load('wood.png')
    wood = pygame.transform.scale(wood, (90, 50))

    gameScreen.blit(background, (0, 0))

    y_cor += word_speed
    gameScreen.blit(wood, (x_cor - 50, y_cor + 15))
    gameScreen.blit(character, (x_cor - 100, y_cor))
    draw_text(gameScreen, str(showword), 40, x_cor, y_cor)
    draw_text(gameScreen, 'Score:' + str(score), 40, WIDTH / 2, 5)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        elif event.type == pygame.KEYDOWN:
            newword += pygame.key.name(event.key)

            if showword.startswith(newword):
                if showword == newword:
                    score += len(showword)
                    new_word()
            else:
                game_front_screen()
                time.sleep(20)
                pygame.quit()

    if y_cor < HEIGHT - 5:
        pygame.init()
        pygame.display.update()
    else:
        game_front_screen()

