from art import logo, vs
from game_data import data
from random import randint


def random_topic():
    topic_list = []
    random_position = randint(0, len(data)-1)

    for value in data[random_position].values():
        topic_list.append(value)

    return topic_list


def check_choice(choice, first, last):
    first_followers = first[1]
    last_followers = last[1]
    win = False

    if choice == "a":
        choice = first_followers
    elif choice == "b":
        choice = last_followers
    else:
        print("\n\nIncorrect option!")

    max_num_followers = max(first_followers, last_followers) 

    if choice == max_num_followers:
        win = True

    return win


def game():
    print(logo)

    score = 0
    continue_game = True

    first_comparison = random_topic()

    while continue_game:
        last_comparison = random_topic()  

        if first_comparison == last_comparison:
            first_comparison = random_topic()

        print(f"\n\nCompare A: {first_comparison[0]}, a {first_comparison[2]}, from {first_comparison[3]}.")

        print(vs)

        print(f"\n\nCompare B: {last_comparison[0]}, a {last_comparison[2]}, from {last_comparison[3]}.")

        # Hint
        # print(first_comparison[1], last_comparison[1])

        choice = input("\n\nWho has more followers? Type 'A' or 'B': ").lower()

        result = check_choice(choice, first_comparison, last_comparison)

        if result == True:
            score += 1

            if choice == "a":
                last_comparison = first_comparison
            else:
                first_comparison = last_comparison

            print(f"\n\nYou're right! Current score: {score}.")

        else:
            print(f"\n\nSorry, that's wrong. Final score: {score}.")
            game = input("\n\nDo you want to play again? type 'n' to exit or anything else to restart: ")

            if game == "n":
                continue_game = False
            else:
                score = 0

game()