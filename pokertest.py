suit = ['clubs','hearts','spades','diamonds']
numbers = ['ace','2','3','4','5','6','7','8','9','10','jack','queen','king']



def flush(cards1,cards2,cards3,cards4,cards5):
    for i in suit:
        if cards1[1] == i and cards2[1] == i and cards3[1] == i and cards4[1] == i and cards5[1] == i:
            return pokerCombo['flush']

pokerCombo = {'Four of a Kind':8,
              'Full House':7,
              'flush':6,
              'Straight':5,
              'Three of a Kind':4,
              'Two Pair':3,
              'Pair':2,
              'High Card':1,}

c1 = ['ace','hearts']
c2 = ['2','hearts']
c3 = ['2','hearts']
c4 = ['ace','hearts']
c5 = ['ace','hearts']



def pair(card1, card2, card3, card4, card5):
    # Собираем все карты в список
    cards = [card1, card2, card3, card4, card5]
    
    # Извлекаем только ранги (первый элемент каждой карты)
    ranks = [card[0] for card in cards]
    
    # Подсчёт количества каждого ранга
    rank_counts = {}
    for rank in ranks:
        rank_counts[rank] = rank_counts.get(rank, 0) + 1
    
    # Проверка на наличие пары
    has_pair = any(count == 2 for count in rank_counts.values())
    if has_pair:
        return pokerCombo['Pair']

def Three(card1, card2, card3, card4, card5):
    # Собираем все карты в список
    cards = [card1, card2, card3, card4, card5]
    
    # Извлекаем только ранги (первый элемент каждой карты)
    ranks = [card[0] for card in cards]
    
    # Подсчёт количества каждого ранга
    rank_counts = {}
    for rank in ranks:
        rank_counts[rank] = rank_counts.get(rank, 0) + 1
    
    # Проверка на наличие пары
    has_pair = any(count == 3 for count in rank_counts.values())
    if has_pair:
        return pokerCombo['Three of a Kind']

def Four(card1, card2, card3, card4, card5):
    # Собираем все карты в список
    cards = [card1, card2, card3, card4, card5]
    
    # Извлекаем только ранги (первый элемент каждой карты)
    ranks = [card[0] for card in cards]
    
    # Подсчёт количества каждого ранга
    rank_counts = {}
    for rank in ranks:
        rank_counts[rank] = rank_counts.get(rank, 0) + 1
    
    # Проверка на наличие пары
    has_pair = any(count == 4 for count in rank_counts.values())
    if has_pair:
        return pokerCombo['Four of a Kind']

# Пример использования
cards1 = ['ace', 'hearts']
cards2 = ['king', 'spades']
cards3 = ['ace', 'diamonds']
cards4 = ['queen', 'clubs']
cards5 = ['jack', 'hearts']

if pair(cards1, cards2, cards3, cards4, cards5):
    print("Есть пара!")
else:
    print("Пар нет.")

pokerCombo = {'Four of a Kind':8,
              'Full House':7,
              'flush':6,
              'Straight':5,
              'Three of a Kind':4,
              'Two Pair':3,
              'Pair':2,
              'High Card':1}

n = 'e'
n = flush(c1,c2,c3,c4,c5)
k = pair(c1,c2,c3,c4,c5)
t = (['ace', 'hearts', 13], ['jack', 'clubs', 10], ['king', 'diamonds', 51], ['10', 'spades', 35], ['queen', 'spades', 37])




def is_straight(card1, card2, card3, card4, card5):
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
            return True
    
    # Проверка на стрит с тузом как младшей картой (A-2-3-4-5)
    if set(['ace', '2', '3', '4', '5']).issubset(ranks):
        return pokerCombo['Straight'],True

    return 0,False

print(is_straight(['ace', 'hearts', 13], ['jack', 'clubs', 10], ['king', 'diamonds', 51], ['10', 'spades', 35], ['queen', 'spades', 37]),'3')
print(n)
print(k)