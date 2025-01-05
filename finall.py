import pygame
import sys


pygame.init()

WIDTH, HEIGHT = 1250, 900

WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
RED = (255, 0,0)
GREEN = (0,255,0)
YELLOW = (255, 255, 0)


FONT_SIZE = 120

font = pygame.font.Font(None, FONT_SIZE)  # None использует шрифт по умолчанию

FONT_SIZE = 60

font2 = pygame.font.Font(None, FONT_SIZE)
# Текст
textMid = "Wait"  # Текст для отображения

# Рендеринг текста
textMid_surface = font.render(textMid, True, GREEN)  # Создаём поверхность с текстом
textMid_rect = textMid_surface.get_rect(center=(WIDTH // 2, HEIGHT // 2))
clock = pygame.time.Clock()

textRightScore = "0"  # Текст для отображения

# Рендеринг текста
textRightScore_surface = font.render(textRightScore, True, RED)  # Создаём поверхность с текстом
textRightScore_rect = textRightScore_surface.get_rect(center=(WIDTH -250, HEIGHT // 2))
clock = pygame.time.Clock()




textLefttScore = "0"  # Текст для отображения

# Рендеринг текста
textLefttScore_surface = font.render(textLefttScore, True, BLUE)  # Создаём поверхность с текстом
textLefttScore_rect = textLefttScore_surface.get_rect(center=(WIDTH // 4, HEIGHT // 2))
clock = pygame.time.Clock()





textRightCombo = "Wait"  # Текст для отображения

# Рендеринг текста
textRightCombo_surface = font2.render(textRightCombo, True, RED)  # Создаём поверхность с текстом
textRightCombo_rect = textRightCombo_surface.get_rect(center=(WIDTH -250, HEIGHT // 4))
clock = pygame.time.Clock()




textLefttCombo = "Wait"  # Текст для отображения

# Рендеринг текста
textLefttCombo_surface = font2.render(textLefttCombo, True, BLUE)  # Создаём поверхность с текстом
textLefttCombo_rect = textLefttCombo_surface.get_rect(center=(WIDTH // 4, HEIGHT // 4))
clock = pygame.time.Clock()



screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Finall")


while True:
    # События
    screen.fill((0, 0, 0))  # Чёрный фон
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
                player1 = open('combo1.txt','r')
                player2 = open('combo2.txt','r')
                lines1 = player1.read()
                lines1 = lines1.split('\n')
                #print(lines1,'1')
                #lines2 = player2.readlines()
                lines2 = player2.read()
                lines2 = lines2.split('\n')

                if float(lines1[1]) > float(lines2[1]):
                    
                    textMid = 'win1'
                    textMid_surface = font.render(textMid, True, BLUE)
                    print('win1')
                elif float(lines1[1]) < float(lines2[1]):
                    textMid = 'win2'
                    print('win2')
                    textMid_surface = font.render(textMid, True, RED)
                else:
                    textMid = 'Draw'
                    print('draw')
                    textMid_surface = font.render(textMid, True, YELLOW)
                print(lines2[1])
                textRightScore = str(lines2[1])
                textRightScore_surface = font.render(textRightScore, True, RED)
                
                textLefttScore = str(lines1[1])
                textLefttScore_surface = font.render(textLefttScore, True, BLUE)

                textRightCombo = str(lines2[0])
                textRightCombo_surface = font2.render(textRightCombo, True, RED)
                
                textLefttCombo = str(lines1[0])
                textLefttCombo_surface = font2.render(textLefttCombo, True, BLUE)



    screen.blit(textMid_surface, textMid_rect)
    screen.blit(textRightScore_surface, textRightScore_rect)
    screen.blit(textLefttScore_surface, textLefttScore_rect)
    screen.blit(textRightCombo_surface, textRightCombo_rect)
    screen.blit(textLefttCombo_surface, textLefttCombo_rect)

    pygame.display.update()  # Обновляем экран
    clock.tick(60)  # Ограничение FPS