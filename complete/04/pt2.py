

with open("input.txt") as f:
    content = f.readlines()
    #content = [int(x) for x in f.readlines()]

bingo = [int(x) for x in content[0].strip().split(',')]

cards = []
card = []
for line in content[1::]:
    if line.strip() == "":
        if len(card) > 0:
            cards.append(card)
            card = []
    else:
        card.append([int(x) for x in line.strip().split()])
cards.append(card)

def call_number(card, number):
    for r in range(len(card)):
        line = card[r]
        for c in range(len(line)):
            cell = line[c]
            if cell == number:
                card[r][c] = -1
    return card

def check(card):
    for line in card:
        if line.count(-1) == len(line):
            return True
    for i in range(len(card[0])):
        count = 0
        for line in card:
            if line[i] == -1:
                count += 1
        if count == len(card):
            return True

    return False


def sum_card(card):
    total = 0
    for line in card:
        for cell in line:
            if cell != -1:
                total += cell
    return total


for draw in bingo:
    new_cards = cards.copy()
    for c in range(len(cards)):
        card = cards[c]
        cards[c] = call_number(card, draw)
        if check(card):
            if len(new_cards) > 1:
                new_cards.remove(card)
            else:
                sc = sum_card(card)
                print(draw, sc, sc * draw)
                exit()
    cards = new_cards
