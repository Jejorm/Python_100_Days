################### SCOPE ##################

enemies = 1

def increase_enemies():
    enemies = 2
    print(f"Enemies inside function: {enemies}")


increase_enemies()
print(f"Enemies outside function: {enemies}")


# Local Scope
def drink_potion():
    potion_strength = 2
    print(potion_strength)


drink_potion()
# Name Error
# print(potion_strength)


#Global Scope
player_health = 10

def game():
    player_health = 15
    def drink_potion2():
        pass
    print(player_health)

# Name Error
# drink_potion2()
game()
print(player_health)


# There is no Block Scope
game_level = 3
new_enemies = ["Skeleton", "Zombie", "Alien"]

def create_enemy():
    if game_level < 5:
        new_enemie = new_enemies[0]

    print(new_enemie)

# Name Error
# print(new_enemie)


# Modifying Global Scope
enemies2 = 1

def increase_enemies2():
    # Avoid use global!
    # global enemies2
    # enemies2 += 1 

    print(f"Enemies inside function: {enemies2}")
    return enemies2 + 1

enemies2 = increase_enemies2()
print(f"Enemies outside function: {enemies2}")


# Global Constants:
PI = 3.14159 
URL = "https://www.google.com"
