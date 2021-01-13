from art import logo

print(logo)

continue_auction = True
person = {}
highest_bid = 0

while continue_auction:
    name = input("What's your name? ")
    bid = int(input("What's you bid? "))

    person[name] = bid

    answer = input("Are there any other bridders?\nType 'q' to exit or anything else to continue the auction\n").lower()
    if answer == "q".lower():
        continue_auction = False

for name_person in person:
    actual_bid = person[name_person]
    if actual_bid > highest_bid:
        highest_bid = actual_bid
        winner = name_person

print(f"The winner is {winner.title()} with a bid of ${highest_bid}")