import pygame
import sys
import random

pygame.init()

# Константы
WIDTH, HEIGHT = 1250, 900  # Размер экрана
#GRID_COLS, GRID_ROWS = 10, 5  # Количество колонок и строк в сетке
#WIDTHPLAYER, HEIGHTPLAYER = 1000,500
#CELL_WIDTH = WIDTH // GRID_COLS  # Ширина ячейки
#CELL_HEIGHT = HEIGHT // GRID_ROWS  # Высота ячейки
#IMAGE_SIZE = 50  #
cursor = pygame.image.load('Playing Cards/2_of_clubs.png')
cursor = pygame.transform.scale(cursor, (250,360))

suit = ['clubs','hearts','spades','diamonds']
numbers = ['ace','2','3','4','5','6','7','8','9','10','jack','queen','king']



cardsPhoto = [
   # pygame.image.load(f"sunf{i}.png") for i in range(3)
]

cards= []
deck = []

for i in suit:
    for j in numbers:
        card_image = pygame.image.load(f'Playing Cards/{j}_of_{i}.png')
        # Изменяем размер изображения на 250x362
        resized_card = pygame.transform.scale(card_image, (250, 362))
        # Добавляем измененное изображение в список
        cardsPhoto.append(resized_card)

n = 0

for i in suit:
    for j in numbers:
        cards.append([j,i,n])
        n+=1

n=0
for i in suit:
    for j in numbers:
        deck.append([j,i,n])
        n+=1


print(cards)
print(deck)
print(len(cards))
print(n)
clock = pygame.time.Clock()

screen = pygame.display.set_mode((WIDTH, HEIGHT))

r1 = 0#random.randint(0,len(cards)-1)
d1 = cards[r1][2]
cards.pop(r1)
r2 = 8#random.randint(0,len(cards)-1)
d2 = cards[r2][2]
cards.pop(r2)
r3 = 8#random.randint(0,len(cards)-1)
d3 = cards[r3][2]
cards.pop(r3)
r4 = 8#random.randint(0,len(cards)-1)
d4 = cards[r4][2]
cards.pop(r4)
r5 = 8#random.randint(0,len(cards)-1)
d5 = cards[r5][2]
cards.pop(r5)


score = {
      'ace':14,
      '2':2,
      '3':3,
      '4':4,
      '5':5,
      '6':6,
      '7':7,
      '8':8,
      '9':9,
      '10':10,
      'jack':11,
      'queen':12,
      'king':13
}
#'jack','queen','king'

pokerCombo = {'Straight Flush':9,
              'Four of a Kind':8,
              'Full House':7,
              'Flush':6,
              'Straight':5,
              'Three of a Kind':4,
              'Two Pair':3,
              'Pair':2,
              'High Card':1}



def flush(cards1,cards2,cards3,cards4,cards5):
    for i in suit:
        if cards1[1] == i and cards2[1] == i and cards3[1] == i and cards4[1] == i and cards5[1] == i:
            rank = max(score[cards1[0]],score[cards2[0]],score[cards3[0]],score[cards4[0]],score[cards5[0]])
            return pokerCombo['Flush'],True,rank
        else:
            #print(1)
            return 0,False, None


def two_pair(cards1, cards2, cards3, cards4, cards5):
    # Получаем все значения карт
    values = [cards1[0], cards2[0], cards3[0], cards4[0], cards5[0]]
    
    # Считаем количество каждой карты
    value_count = {value: values.count(value) for value in values}
    
    # Сортируем по количеству в убывающем порядке
    sorted_values = sorted(value_count.items(), key=lambda x: x[1], reverse=True)
    
    # Если есть каре (4 одинаковых карты)
    if sorted_values[0][1] == 4:
        return 0,False,None

    # Если есть две пары (по два одинаковых значения)
    elif len([pair for pair, count in value_count.items() if count == 2]) == 2:
        pairs = [pair for pair, count in value_count.items() if count == 2]
        highest_pair = max(score[pair] for pair in pairs)
#        kicker = max(score[value] for value in values if value not in pairs)
#        print(pokerCombo['Two Pair'], True, highest_pair, kicker)
        return pokerCombo['Two Pair'], True, highest_pair
    
    # Если нет ни двух пар, ни каре
    return 0, False, None


def HighCards(cards1,cards2,cards3,cards4,cards5):
      k = max(score[cards1[0]],score[cards2[0]],score[cards3[0]],score[cards4[0]],score[cards5[0]])
      k = k/100
      return k

def Pair(card1, card2, card3, card4, card5):
    # Собираем все карты в список
    cards2 = [card1, card2, card3, card4, card5]
    
    # Извлекаем только ранги (первый элемент каждой карты)
    ranks = [card[0] for card in cards2]
    
    # Подсчёт количества каждого ранга
    rank_counts = {}
    for rank in ranks:
        rank_counts[rank] = rank_counts.get(rank, 0) + 1
    
    # Проверка на наличие "Каре"
    for rank, count in rank_counts.items():
        if count == 2:
            # Возвращаем комбинацию, флаг наличия и ранг
            return pokerCombo['Pair'], True, rank
    
    # Если комбинация не найдена
    return 0, False, None

def Three(card1, card2, card3, card4, card5):
    # Собираем все карты в список
    cards2 = [card1, card2, card3, card4, card5]
    
    # Извлекаем только ранги (первый элемент каждой карты)
    ranks = [card[0] for card in cards2]
    
    # Подсчёт количества каждого ранга
    rank_counts = {}
    for rank in ranks:
        rank_counts[rank] = rank_counts.get(rank, 0) + 1
    
    # Проверка на наличие "Каре"
    for rank, count in rank_counts.items():
        if count == 3:
            # Возвращаем комбинацию, флаг наличия и ранг
            return pokerCombo['Three of a Kind'], True, rank
    
    # Если комбинация не найдена
    return 0, False, None


def Four(card1, card2, card3, card4, card5):
    # Собираем все карты в список
    cards2 = [card1, card2, card3, card4, card5]
    
    # Извлекаем только ранги (первый элемент каждой карты)
    ranks = [card[0] for card in cards2]
    
    # Подсчёт количества каждого ранга
    rank_counts = {}
    for rank in ranks:
        rank_counts[rank] = rank_counts.get(rank, 0) + 1
    
    # Проверка на наличие "Каре"
    for rank, count in rank_counts.items():
        if count == 4:
            # Возвращаем комбинацию, флаг наличия и ранг
            return pokerCombo['Four of a Kind'], True, rank
    
    # Если комбинация не найдена
    return 0, False, None



def straight(card1, card2, card3, card4, card5):
    # Собираем все карты в список
    cards = [card1, card2, card3, card4, card5]
    
    # Массив всех рангов в покере в порядке возрастания
    ranks_order = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'jack', 'queen', 'king', 'ace']
    
    # Извлекаем ранги карт
    ranks = [card[0] for card in cards]
    
    # Убираем дубли и сортируем ранги по порядку
    unique_ranks = sorted(set(ranks), key=lambda rank: ranks_order.index(rank))
    
    # Проверяем, содержат ли ранги 5 последовательных элементов
    for i in range(len(unique_ranks) - 4):
        # Берём 5 подряд и проверяем их последовательность
        if ranks_order.index(unique_ranks[i + 4]) - ranks_order.index(unique_ranks[i]) == 4:
            # Возвращаем тип комбинации, True и старшую карту
            return pokerCombo['Straight'], True, score[unique_ranks[i + 4]]
    
    # Проверка на стрит с тузом как младшей картой (A-2-3-4-5)
    if set(['ace', '2', '3', '4', '5']).issubset(ranks):
        return pokerCombo['Straight'], True, '5'

    # Если стрита нет
    return 0, False, None





GREEN = (0,200,0)
FONT_SIZE = 44
text = "ffff"  # Текст для отображения
font = pygame.font.Font(None, FONT_SIZE) 
# Рендеринг текста
text_surface = font.render(text, True, GREEN) 
text_rect = text_surface.get_rect(center=(WIDTH // 2, HEIGHT // 2))


textScore = "0"  # Текст для отображения
font = pygame.font.Font(None, FONT_SIZE) 
# Рендеринг текста
textScore_surface = font.render(textScore, True, GREEN) 
textScore_rect = textScore_surface.get_rect(center=(WIDTH // 2, HEIGHT - 550))


print(deck[r1][2])
pygame.display.set_caption("Poker2")
while True:
    # События
    screen.fill((0, 0, 0))  # Чёрный фон

    screen.blit(cardsPhoto[deck[d1][2]], (000,500))
    screen.blit(cardsPhoto[deck[d2][2]], (250,500))
    screen.blit(cardsPhoto[deck[d3][2]], (500,500))
    screen.blit(cardsPhoto[deck[d4][2]], (750,500))
    screen.blit(cardsPhoto[deck[d5][2]], (1000,500))
#    screen.blit(cardsPhoto[r2], (250,500))



    text_surface = font.render(text, True, GREEN) 
    screen.blit(text_surface, text_rect)

    textScore_surface = font.render(textScore, True, GREEN)
    screen.blit(textScore_surface, textScore_rect)
    
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_1:
                if len(cards)>5:
                    r1 = random.randint(0,len(cards)-1)
                    d1 = cards[r1][2]
                    cards.pop(r1)
                else:
                    print('empty')
            if event.key == pygame.K_2:
                            if len(cards)>5:
                                r2 = random.randint(0,len(cards)-1)
                                d2 = cards[r2][2]
                                cards.pop(r2)
                            else:
                                print('empty')
            if event.key == pygame.K_3:
                            if len(cards)>5:
                                r3 = random.randint(0,len(cards)-1)
                                d3 = cards[r3][2]
                                cards.pop(r3)
                            else:
                                print('empty')
            if event.key == pygame.K_4:
                            if len(cards)>5:
                                r4 = random.randint(0,len(cards)-1)
                                d4 = cards[r4][2]
                                cards.pop(r4)

                            else:
                                print('empty')

            if event.key == pygame.K_5:
                            if len(cards)>5:
                                r5 = random.randint(0,len(cards)-1)
                                d5 = cards[r5][2]
                                cards.pop(r5)
#                                print(r5)
                                print((deck[d1],deck[d2],deck[d3],deck[d4],deck[d5]))
                            else:
                                print('empty')
            if event.key == pygame.K_6:
                with open('combo2.txt', 'w') as file:
                    file.write(text)
                    file.write('\n')
                    file.write(textScore)


#    combo,g = flush(deck[d1],deck[d2],deck[d3],deck[d4],deck[d5])
    #print(g)
    g = False


    


    if g == False:

        combo,g1,score1 = flush(deck[d1],deck[d2],deck[d3],deck[d4],deck[d5])
        combo,g2,score1 = straight(deck[d1],deck[d2],deck[d3],deck[d4],deck[d5])

        if g1 == True and g2 == True:

#            print(1)
            g = True
            combo = 9
            if score1 == 14:
                 combo = 10



    if g == False:
        combo,g,score1 = Four(deck[d1],deck[d2],deck[d3],deck[d4],deck[d5])

    if g == False:
        combo,g,score1 = flush(deck[d1],deck[d2],deck[d3],deck[d4],deck[d5])

    if g == False:
        combo,g,score1 = straight(deck[d1],deck[d2],deck[d3],deck[d4],deck[d5])

    if g == False:
        combo,g,score1 = Three(deck[d1],deck[d2],deck[d3],deck[d4],deck[d5])
    if g == False:
        combo,g,score1 = two_pair(deck[d1],deck[d2],deck[d3],deck[d4],deck[d5])         

    if g == False:
        combo,g,score1 = Pair(deck[d1],deck[d2],deck[d3],deck[d4],deck[d5])

    HighCard = float(HighCards(deck[d1],deck[d2],deck[d3],deck[d4],deck[d5]))

    HighCardST = True
    if combo != None:
        if combo == 10:
            text = 'Flush Royale'
            HighCardST = False
        if combo == 9:
            text = 'Straight Flush'
            HighCardST = False

        if combo == 8:
            text = 'Four of a Kind'
            HighCardST = False

        if combo == 6:
            text = 'Flush'
            HighCardST = False
#            print(1)
        if combo == 5:
            text = 'Straight'
            HighCardST = False
#            print(1)
        
        if combo == 4:
            text = 'Three of a Kind'
            HighCardST = False
        if combo == 3:
             text = 'Two Pair'
             HighCardST = False
        
        if combo == 2:
            text = 'Pair'
            HighCardST = False

    else:
          combo=0
    
#    print(combo+score1)
    if HighCardST==False:
        if isinstance(score1, str):
            score1 = score[score1]
        textScore = str(combo*100+score1)
    
    if HighCardST==True:
          score1 = HighCard
          textScore = str(score1)
          text='HighCard'

    pygame.display.update()  # Обновляем экран
    clock.tick(60)  # Ограничение FPS