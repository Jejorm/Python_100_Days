from art import logo
import random


def deal_card():
    """
    Return a random card (int) from the cards.
    """
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    random_card = random.choice(cards)

    return random_card


def calculate_score(cards_list):
    """
    Takes in a list of cards and return the score calculated from the cards.   
    """
    # Blackjack
    if sum(cards_list) == 21 and len(cards_list) == 2:
        return 0

    if 11 in cards_list and sum(cards_list) > 21:
        cards_list.remove(11)
        cards_list.append(1)

    return sum(cards_list)


def compare(user_score, computer_score):
    """
    Takes in the user score and computer score (both ints), and return the result of the game. 
    """
    if user_score > 21 and computer_score > 21:
        return "You went over. You lose."
    if user_score == computer_score:
        return "Draw."
    elif computer_score == 0:
        return "Lose, opponent has Blackjack."
    elif user_score == 0:
        return "Win with a Blackjack."
    elif user_score > 21:
        return "You went over. You lose."
    elif computer_score > 21:
        return "Opponent went over. You win."
    elif user_score > computer_score:
        return "You win."
    else:
        return "You lose."
        

def play_game():
    """
    Main function of the program.
    """
    print(logo)

    user_cards = []
    computer_cards = []

    game_over = False

    for _ in range(2):
        user_cards.append(deal_card())
        computer_cards.append(deal_card())


    while not game_over:
        user_score = calculate_score(user_cards)
        computer_score = calculate_score(computer_cards)
        print(f"\n\n\t\tYour cards: {user_cards}; current score: {user_score}")
        print(f"\n\n\t\tComputer first card: {computer_cards[0]}")    

        if user_score == 0 or computer_score == 0 or user_score > 21:
            game_over = True
        else:
            continue_game = input("\n\nType 'y' to get another card, type 'n' to pass: ").lower()
            if continue_game == 'y':
                user_cards.append(deal_card())
            else:
                game_over = True


    while computer_score != 0 and computer_score < 17:
        computer_cards.append(deal_card())
        computer_score = calculate_score(computer_cards)


    print(f"\n\n\n\tYour final hand: {user_cards}; final score: {user_score}")
    print(f"\n\n\n\tComputer's final hand: {computer_cards}; final score: {computer_score}")
    print(f"\n\n\n{compare(user_score, computer_score)}")


while input("\n\n\n\nDo you want to play a game of Blackjack? Type 'y' or 'n': ").lower() == "y": 
    play_game()

else:
    print("\n\nGoodbye.")
