import random

class Character:
    def __init__(self, name, hp, attack, defense):
        self.name = name
        self.hp = hp
        self.attack = attack
        self.defense = defense

    def take_damage(self, damage):
        actual_damage = max(0, damage - self.defense)
        self.hp -= actual_damage
        return self.hp <= 0

    def attack_target(self, target):
        damage = random.randint(1, self.attack)
        target_dead = target.take_damage(damage)
        print(f"{self.name} attacks {target.name} for {damage} damage!")
        return target_dead

class Player(Character):
    def __init__(self, name):
        super().__init__(name, 100, 20, 5)
        self.level = 1
        self.experience = 0
        self.gold = 50
        self.potions = 3

    def level_up(self):
        self.level += 1
        self.hp += 20
        self.attack += 5
        self.defense += 2
        print(f"{self.name} leveled up to level {self.level}!")
        print(f"Stats: HP: {self.hp}, Attack: {self.attack}, Defense: {self.defense}")

    def gain_experience(self, amount):
        self.experience += amount
        if self.experience >= self.level * 50:
            self.experience -= self.level * 50
            self.level_up()

    def use_potion(self):
        if self.potions > 0:
            self.hp += 30
            self.potions -= 1
            print(f"{self.name} used a potion and restored 30 HP!")
        else:
            print("No potions left!")

    def visit_shop(self):
        print("Welcome to the shop! You have {self.gold} gold.")
        print("[1] Buy Potion (10 gold) \n[2] Upgrade Attack (20 gold) \n[3] Upgrade Defense (20 gold) \n[4] Leave shop")
        choice = input("Choose an option: ").strip()
        if choice == '1' and self.gold >= 10:
            self.potions += 1
            self.gold -= 10
            print("You bought a potion!")
        elif choice == '2' and self.gold >= 20:
            self.attack += 2
            self.gold -= 20
            print("Your attack increased!")
        elif choice == '3' and self.gold >= 20:
            self.defense += 2
            self.gold -= 20
            print("Your defense increased!")
        elif choice == '4':
            print("Leaving the shop.")
        else:
            print("Invalid choice or not enough gold.")

class Monster(Character):
    def __init__(self, name, hp, attack, defense, xp_reward, gold_reward):
        super().__init__(name, hp, attack, defense)
        self.xp_reward = xp_reward
        self.gold_reward = gold_reward

def battle(player, monster):
    print(f"A wild {monster.name} appears!")
    while player.hp > 0 and monster.hp > 0:
        action = input("Do you want to [A]ttack, [H]eal, or [R]un? ").lower()
        if action == 'a':
            if player.attack_target(monster):
                print(f"{monster.name} is defeated! You gain {monster.xp_reward} XP and {monster.gold_reward} gold.")
                player.gain_experience(monster.xp_reward)
                player.gold += monster.gold_reward
                break
        elif action == 'h':
            player.use_potion()
        elif action == 'r':
            if random.random() < 0.5:
                print(f"You successfully ran away from the {monster.name}.")
                break
            else:
                print(f"You failed to run away!")
        else:
            print("Invalid action. Please choose [A]ttack, [H]eal, or [R]un.")

        if monster.attack_target(player):
            print("You have been defeated! Game over.")
            break

        print(f"{player.name} HP: {player.hp}")
        print(f"{monster.name} HP: {monster.hp}")

def game():
    player = Player(input("Enter your character's name: "))
    monsters = [
        Monster("Goblin", 50, 15, 5, 20, 10),
        Monster("Orc", 80, 20, 10, 40, 20),
        Monster("Dragon", 150, 30, 15, 100, 50)
    ]

    for monster in monsters:
        battle(player, monster)
        if player.hp <= 0:
            break
        print("Do you want to visit the shop? [Y]es or [N]o")
        if input().lower() == 'y':
            player.visit_shop()
    
    if player.hp > 0:
        print(f"Congratulations, {player.name}! You defeated all the monsters!")

if __name__ == "__main__":
    game()
