import random
import time

# ------------------------------
# Simple Text Adventure Game
# ------------------------------

class Player:
    def __init__(self, name):
        self.name = name
        self.health = 100
        self.gold = 0
        self.inventory = []

    def is_alive(self):
        return self.health > 0

    def take_damage(self, amount):
        self.health -= amount
        print(f"{self.name} took {amount} damage! Health now: {self.health}")

    def heal(self, amount):
        self.health += amount
        print(f"{self.name} healed by {amount}. Health now: {self.health}")

    def add_gold(self, amount):
        self.gold += amount
        print(f"{self.name} earned {amount} gold. Total: {self.gold}")

    def add_item(self, item):
        self.inventory.append(item)
        print(f"{self.name} picked up {item}.")

class Enemy:
    def __init__(self, name, health, damage):
        self.name = name
        self.health = health
        self.damage = damage

    def is_alive(self):
        return self.health > 0

    def attack(self, player):
        print(f"{self.name} attacks!")
        player.take_damage(self.damage)

def encounter_enemy(player):
    enemy_types = [
        ("Goblin", 30, 10),
        ("Skeleton", 40, 12),
        ("Wolf", 25, 8),
        ("Bandit", 35, 15),
    ]
    name, health, damage = random.choice(enemy_types)
    enemy = Enemy(name, health, damage)
    print(f"A wild {enemy.name} appears!")

    while enemy.is_alive() and player.is_alive():
        action = input("Do you [a]ttack or [r]un? ").lower()
        if action == "a":
            dmg = random.randint(5, 20)
            enemy.health -= dmg
            print(f"You hit {enemy.name} for {dmg} damage.")
            if enemy.is_alive():
                enemy.attack(player)
        elif action == "r":
            if random.random() < 0.5:
                print("You escaped successfully!")
                return
            else:
                print("You failed to run away!")
                enemy.attack(player)
        else:
            print("Invalid action.")
    if player.is_alive():
        reward = random.randint(10, 50)
        player.add_gold(reward)
        loot = random.choice(["Potion", "Sword", "Shield"])
        player.add_item(loot)

def find_treasure(player):
    gold = random.randint(20, 100)
    print("You discovered a hidden treasure chest!")
    player.add_gold(gold)
    item = random.choice(["Magic Ring", "Armor", "Gemstone"])
    player.add_item(item)

def random_event(player):
    event = random.choice(["enemy", "treasure", "nothing"])
    if event == "enemy":
        encounter_enemy(player)
    elif event == "treasure":
        find_treasure(player)
    else:
        print("The path is quiet... nothing happens.")

def game_loop():
    print("Welcome to the Adventure Game!")
    name = input("Enter your hero's name: ")
    player = Player(name)

    turns = 0
    while player.is_alive() and turns < 10:
        print(f"\n--- Turn {turns + 1} ---")
        random_event(player)
        turns += 1
        time.sleep(1)

    print("\nGame Over!")
    if player.is_alive():
        print(f"Congratulations {player.name}, you survived with {player.health} health and {player.gold} gold!")
    else:
        print(f"Alas, {player.name} has fallen in battle...")

if __name__ == "__main__":
    game_loop()
