'''
    black jack game
    user draws a card
    dealaer draws a card

    user draws another card
    checks if the sum is less than 21 or equal to 21
    if the sum is greater than 21 user is out no matter what the dealer has

    if the sum is less than or equal to 21 
    the dealer draws another card

    the "A" card or 1 might have value 1 or 11 depending on your score

'''

import random

cards = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

player_cards = []
dealer_cards = []

def draw_card():
    return random.choice(cards)

def get_player_choice():
    a = input("Draw a card? (y / n): ")
    return a

def print_cards():
    print(f"\nPlayer Cards: {player_cards}")
    print(f"Dealer Cards: {dealer_cards}")

def check_win_condition():

    if sum(dealer_cards) < 21: 
        if sum(player_cards) > sum(dealer_cards) and sum(player_cards) <= 21:
            return True

def check_win():
    if 1 in player_cards:
        if sum(player_cards) < 21:
            if (sum(player_cards) + 10) < 21:
                index = player_cards.index(1)
                player_cards[index] = 11

    if check_win_condition():
        print("You won !!!!")
    else:
        print("You lost !!")

def main():
    start_flag = False

    x = input("Do you want to play BlackJack? (y / n):  ")

    if x.lower() == 'y':
        start_flag = True
        player_cards.append(draw_card())
        dealer_cards.append(draw_card())
        print_cards()

    
    while start_flag:
        player_choice = input("Do you want to draw one more card ? (y / n):  ")

        if player_choice.lower() == 'y':
            player_cards.append(draw_card())

            if sum(player_cards) > 21:
                print_cards()
                check_win()
                start_flag = False

            dealer_cards.append(draw_card())
            print(f"\nPlayer Cards: {player_cards}")
        elif player_choice.lower() == 'n':
            print_cards()
            check_win()
            start_flag = False





if __name__ == '__main__':
    main()