############### Blackjack Project #####################

import random
from art import logo


def deal_card():
    cards= [11,2,3,4,5,6,7,8,9,10,10,10,10]
    random_card=random.choice(cards)
    return random_card


def calculate_score(cards):

            if sum(cards) == 21 and len(cards) == 2:
                return 0
        
            if 11 in cards and sum(cards)>21:
                cards.remove(11)
                cards.append(1)
            return sum(cards)

def compare(user_score,computer_score):

    if user_score > 21 and computer_score > 21:
        return "You went over. You lose 😤"

    if user_score == computer_score:
        return "Draw 🙃"
    elif computer_score == 0:
        return "Lose, opponent has Blackjack 😱"
    elif user_score == 0:
        return "Won with a Blackjack 😎"
    elif user_score > 21:
        return "You went over. You lose 😭"
    elif computer_score > 21:
        return "Opponent went over. You win 😁"
    elif user_score > computer_score:
        return "You win 😃"
    else:
        return "You lose 😤"



def play_game():
    print(logo)
    user_cards = []
    computer_cards = []
    game_end = False
    for _ in range(2):
        new_card = deal_card()
        user_cards.append(deal_card())
        computer_cards.append(deal_card())
    
    while not game_end:
        user_score =calculate_score(user_cards)
        computer_score =calculate_score(computer_cards)
        print(f"   Your cards: {user_cards}, current score: {user_score}")
        print(f"   Computer's first card: {computer_cards[0]}")
        if user_score == 0 or computer_score == 0 or user_score >21:
            game_end = True
        else:
            user_deal = input("Do you want another card ? Type 'y' for card or type 'n' for hand\n")
            if user_deal == "y":
                user_cards.append(deal_card())
            else:
                game_end = True
    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score= calculate_score(computer_cards)
    print(f"Your final hand: {user_cards}, final score: {user_score}")
    print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")
    print(compare(user_score, computer_score))

while input("Do you want to play THE BLACK JACK\n") == "y":
    play_game()
    