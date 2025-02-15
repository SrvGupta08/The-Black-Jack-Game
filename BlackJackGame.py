# The Black Jack game

import art
import random

def deal_card():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    return random.choice(cards)

def count_score(cards):
    if sum(cards) == 21 and len(cards) == 2:
        return 0
    
    if 11 in cards and sum(cards) > 21:
        cards.remove(11)
        cards.append(1)

    return sum(cards)

def compare(my_score1, computer_score1):
    if my_score1 == computer_score1:
        return "Draw"
    elif computer_score1 == 0:
        return "Lose, opponent has Balckjack"
    elif my_score1 == 0:
        return "Win with a Blackjack"
    elif my_score1 > 21:
        return "You went over. You lose"
    elif computer_score1 > 21:
        return "Opponent went over. You win"
    elif my_score1 > computer_score1:
        return "You win"
    else:
        return "You lose"

def play_game():
    print(art.logo)
    my_cards = []
    computer_cards = []
    my_score = 0
    computer_score = -1
    is_game_over = False

    for i in range(2):
        my_cards.append(deal_card())
        computer_cards.append(deal_card())

    while not is_game_over:
        my_score = count_score(my_cards)
        computer_score = count_score(computer_cards)

        print(f"Your cards: {my_cards}, current score: {my_score}")
        print(f"Computer's first card: {computer_cards[0]}")

        if my_score == 0 or computer_score == 0 or my_score > 21:
            is_game_over = True
        else:
            should_continue = input("Type 'y' to draw another card, type 'n' to pass: ").lower()
            if should_continue == 'y':
                my_cards.append(deal_card())
            else:
                is_game_over = True

    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = count_score(computer_cards)

    print(f"Your final hand: {my_cards}, final score: {my_score}")
    print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")
    print(compare(my_score, computer_score))

while input("Do you want to play a game of Blackjack/ Type 'y' or 'n': ") == "y":
    print("\n" * 20)
    play_game()
