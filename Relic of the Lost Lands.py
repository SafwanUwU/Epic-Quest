import random

# Player class
class Player:
    def __init__(self, name, player_class):
        self.name = name
        self.player_class = player_class
        self.health = 100
        self.mana = 100
        self.level = 1
        self.experience = 0
        self.gold = 100
        self.inventory = {"potions": 3}
        self.abilities = self.init_abilities()

    def init_abilities(self):
        if self.player_class == "Warrior":
            return {"Slash": 10, "Block": 5}
        elif self.player_class == "Mage":
            return {"Fireball": 15, "Heal": 10}
        elif self.player_class == "Rogue":
            return {"Backstab": 12, "Dodge": 8}

    def attack(self, enemy):
        ability = random.choice(list(self.abilities.keys()))
        print(f"{self.name} uses {ability}!")
        damage = self.abilities[ability]
        enemy.health -= damage
        print(f"{self.name} dealt {damage} damage to {enemy.name}!")

    def take_damage(self, damage):
        self.health -= damage
        print(f"{self.name} takes {damage} damage! Current HP: {self.health}")

    def heal(self):
        if self.inventory["potions"] > 0:
            self.health += 20
            self.inventory["potions"] -= 1
            print(f"{self.name} used a potion. Health restored! Current HP: {self.health}")
        else:
            print("No potions left!")

    def level_up(self):
        self.level += 1
        self.health += 20
        self.mana += 10
        print(f"{self.name} leveled up! Level: {self.level}, HP: {self.health}, Mana: {self.mana}")

# Enemy class
class Enemy:
    def __init__(self, name, health, attack_power):
        self.name = name
        self.health = health
        self.attack_power = attack_power

    def attack(self, player):
        print(f"{self.name} attacks!")
        player.take_damage(self.attack_power)

# Quest class
class Quest:
    def __init__(self, name, description, reward):
        self.name = name
        self.description = description
        self.reward = reward

    def complete_quest(self, player):
        print(f"Quest '{self.name}' completed!")
        player.gold += self.reward
        player.experience += 50
        print(f"Received {self.reward} gold. Current gold: {player.gold}")

# Combat system
def combat(player, enemy):
    print(f"A wild {enemy.name} appears!")
    while player.health > 0 and enemy.health > 0:
        print(f"{player.name} HP: {player.health}, {enemy.name} HP: {enemy.health}")
        action = input("Choose an action (attack/heal): ").lower()

        if action == "attack":
            player.attack(enemy)
            if enemy.health > 0:
                enemy.attack(player)
        elif action == "heal":
            player.heal()
        else:
            print("Invalid action. Choose 'attack' or 'heal'.")

        if player.health <= 0:
            print("You have been defeated!")
            break
        elif enemy.health <= 0:
            print(f"You defeated {enemy.name}!")
            player.level_up()
            break

# Exploration system
def explore(player):
    locations = ["forest", "village", "dungeon"]
    current_location = random.choice(locations)
    print(f"You are exploring the {current_location}.")

    if current_location == "forest":
        enemy = Enemy("Goblin", 50, 8)
        combat(player, enemy)
    elif current_location == "village":
        print("You meet a merchant who sells potions.")
        buy_potions(player)
    elif current_location == "dungeon":
        enemy = Enemy("Dragon", 120, 20)
        combat(player, enemy)

# Shop system
def buy_potions(player):
    print(f"Welcome to the shop! You have {player.gold} gold.")
    choice = input("Do you want to buy a potion for 50 gold? (yes/no): ").lower()
    if choice == "yes" and player.gold >= 50:
        player.inventory["potions"] += 1
        player.gold -= 50
        print(f"Potion added to your inventory. You have {player.inventory['potions']} potions now.")
    else:
        print("Not enough gold or you chose not to buy.")

# Main game loop
def start_game():
    print("Welcome to the Quest for the Ancient Relic!")
    name = input("Enter your character's name: ")
    print("Choose your class: Warrior, Mage, Rogue")
    player_class = input("Enter your class: ")

    player = Player(name, player_class)

    quests = [
        Quest("Find the Lost Amulet", "Retrieve the lost amulet from the cave.", 100),
        Quest("Defeat the Goblin King", "Defeat the Goblin King terrorizing the village.", 150)
    ]

    while True:
        print("\nWhat would you like to do?")
        choice = input("Explore / Check Inventory / View Quests / Exit: ").lower()

        if choice == "explore":
            explore(player)
        elif choice == "check inventory":
            print(f"Inventory: Potions: {player.inventory['potions']}, Gold: {player.gold}")
        elif choice == "view quests":
            for quest in quests:
                print(f"{quest.name}: {quest.description}")
            quest_choice = int(input("Enter the number of the quest you want to complete (1 or 2): "))
            quests[quest_choice - 1].complete_quest(player)
        elif choice == "exit":
            print("Thanks for playing!")
            break
        else:
            print("Invalid choice. Try again.")

# Start the game
start_game()
