import random
import json
import time

# Define the global state
class GameState:
    def __init__(self):
        self.current_quest = None
        self.quests_completed = []
        self.player = None
        self.time_of_day = "Day"
        self.weather = "Clear"

    def update_time(self):
        self.time_of_day = "Night" if self.time_of_day == "Day" else "Day"

    def update_weather(self):
        self.weather = random.choice(["Clear", "Rain", "Storm"])

# Status effects
STATUS_EFFECTS = {
    'Poison': {'duration': 3, 'damage': 5, 'cure': 'Antidote'},
    'Burn': {'duration': 2, 'damage': 10, 'cure': 'Burn Heal'},
    'Paralysis': {'duration': 1, 'damage': 0, 'cure': 'Paralyze Heal'},
    'Freeze': {'duration': 1, 'damage': 0, 'cure': 'Ice Heal'}
}

# Equipment classes
class Equipment:
    def __init__(self, name, attack_bonus=0, defense_bonus=0, effects=None):
        self.name = name
        self.attack_bonus = attack_bonus
        self.defense_bonus = defense_bonus
        self.effects = effects if effects else {}

class Weapon(Equipment):
    pass

class Armor(Equipment):
    pass

# Skill system
class Skill:
    def __init__(self, name, power, cost, element=None):
        self.name = name
        self.power = power
        self.cost = cost
        self.element = element

    def use(self, user, target):
        if user.mana >= self.cost:
            user.mana -= self.cost
            damage = self.power + random.randint(-5, 5)
            if self.element and target.armor and self.element in target.armor.effects:
                damage -= target.armor.effects[self.element]
            target.take_damage(damage)
            print(f"{user.name} uses {self.name} on {target.name}, dealing {damage} damage!")
        else:
            print(f"Not enough mana to use {self.name}!")

# Character base class
class Character:
    def __init__(self, name, hp, attack, defense, weapon=None, armor=None):
        self.name = name
        self.max_hp = hp
        self.hp = hp
        self.attack = attack
        self.defense = defense
        self.weapon = weapon
        self.armor = armor
        self.status_effects = []
        self.skills = []
        self.mana = 50

    def take_damage(self, damage):
        actual_damage = max(0, damage - self.defense - (self.armor.defense_bonus if self.armor else 0))
        self.hp -= actual_damage
        print(f"{self.name} takes {actual_damage} damage! HP is now {self.hp}.")
        return self.hp <= 0

    def apply_status_effects(self):
        for effect in self.status_effects[:]:
            effect_data = STATUS_EFFECTS.get(effect['name'], {})
            self.hp -= effect_data.get('damage', 0)
            effect['duration'] -= 1
            print(f"{self.name} suffers {effect_data.get('damage', 0)} damage from {effect['name']}! {effect['duration']} turns left.")
            if effect['duration'] <= 0:
                self.status_effects.remove(effect)

    def add_status_effect(self, effect_name):
        if effect_name in STATUS_EFFECTS:
            self.status_effects.append({'name': effect_name, 'duration': STATUS_EFFECTS[effect_name]['duration']})
            print(f"{self.name} is afflicted with {effect_name}!")

    def attack_target(self, target):
        damage = random.randint(1, self.attack + (self.weapon.attack_bonus if self.weapon else 0))
        if target.take_damage(damage):
            print(f"{target.name} is defeated!")
            return True
        return False

# Player class
class Player(Character):
    def __init__(self, name):
        super().__init__(name, 100, 20, 5)
        self.level = 1
        self.experience = 0
        self.gold = 50
        self.potions = 3
        self.inventory = []
        self.skills = [Skill("Fireball", 30, 10, element='fire'), Skill("Heal", 0, -20)]
        self.reputation = {}
        self.quests = []

    def level_up(self):
        self.level += 1
        self.hp += 20
        self.attack += 5
        self.defense += 2
        self.mana += 10
        print(f"{self.name} leveled up to level {self.level}!")
        print(f"Stats: HP: {self.hp}, Attack: {self.attack}, Defense: {self.defense}, Mana: {self.mana}")

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

    def add_item(self, item):
        self.inventory.append(item)
        print(f"{self.name} found {item}!")

    def use_item(self, item_name):
        for item in self.inventory:
            if item.name == item_name:
                if item_name in STATUS_EFFECTS:
                    self.hp += 50
                    self.status_effects = []
                    print(f"{self.name} used {item_name} and restored 50 HP and cured all status effects!")
                self.inventory.remove(item)
                return
        print(f"{item_name} is not in the inventory!")

    def visit_shop(self):
        print(f"Welcome to the shop! You have {self.gold} gold.")
        print("[1] Buy Potion (10 gold) \n[2] Upgrade Attack (20 gold) \n[3] Upgrade Defense (20 gold) \n[4] Buy Elixir (30 gold) \n[5] Leave shop")
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
        elif choice == '4' and self.gold >= 30:
            self.add_item("Elixir")
            self.gold -= 30
        elif choice == '5':
            print("Leaving the shop.")
        else:
            print("Invalid choice or not enough gold.")

# Monster class with special abilities
class Monster(Character):
    def __init__(self, name, hp, attack, defense, xp_reward, gold_reward, special=None):
        super().__init__(name, hp, attack, defense)
        self.xp_reward = xp_reward
        self.gold_reward = gold_reward
        self.special = special

    def use_special(self, target):
        if self.special:
            print(f"{self.name} uses {self.special['name']}!")
            target.add_status_effect(self.special['effect'])

# Quests
class Quest:
    def __init__(self, title, description, reward):
        self.title = title
        self.description = description
        self.reward = reward

    def complete(self, player):
        player.gold += self.reward['gold']
        player.gain_experience(self.reward['xp'])
        print(f"Quest '{self.title}' completed! You received {self.reward['gold']} gold and {self.reward['xp']} XP.")

# Game loop
def game_loop():
    game_state = GameState()
    player = Player(name="Hero")
    game_state.player = player

    print("Welcome to the Advanced RPG Game!")
    print("Your journey begins...")

    while True:
        if player.hp <= 0:
            print("Game Over! You have been defeated.")
            break

        game_state.update_time()
        game_state.update_weather()

        print(f"Current time: {game_state.time_of_day}, Weather: {game_state.weather}")

        print("\n[1] Explore \n[2] Check Status \n[3] Visit Shop \n[4] Save Game \n[5] Load Game \n[6] Exit")
        choice = input("Choose an action: ").strip()

        if choice == '1':
            # Example exploration logic
            print("You venture into the wild...")
            encounter = random.choice(["Monster", "Treasure", "Nothing"])
            if encounter == "Monster":
                monster = Monster("Goblin", 30, 10, 2, xp_reward=20, gold_reward=10)
                print(f"A wild {monster.name} appears!")
                while monster.hp > 0 and player.hp > 0:
                    print("\n[1] Attack \n[2] Use Skill \n[3] Use Potion")
                    action = input("Choose your action: ").strip()
                    if action == '1':
                        if player.attack_target(monster):
                            print(f"You defeated the {monster.name}!")
                            player.gain_experience(monster.xp_reward)
                            player.gold += monster.gold_reward
                            break
                    elif action == '2':
                        print("[1] Fireball \n[2] Heal")
                        skill_choice = input("Choose a skill: ").strip()
                        if skill_choice == '1':
                            player.skills[0].use(player, monster)
                        elif skill_choice == '2':
                            player.skills[1].use(player, player)
                    elif action == '3':
                        player.use_potion()
                    monster.use_special(player)
                    player.apply_status_effects()
                    if player.hp <= 0:
                        print("You have been defeated!")
                        break
            elif encounter == "Treasure":
                treasure = random.choice(["Gold", "Potion", "Weapon", "Armor"])
                if treasure == "Gold":
                    found_gold = random.randint(10, 50)
                    player.gold += found_gold
                    print(f"You found {found_gold} gold!")
                elif treasure == "Potion":
                    player.potions += 1
                    print("You found a potion!")
                elif treasure == "Weapon":
                    new_weapon = Weapon("Sword", attack_bonus=5)
                    player.add_item(new_weapon)
                    player.weapon = new_weapon
                    print("You found a Sword!")
                elif treasure == "Armor":
                    new_armor = Armor("Shield", defense_bonus=5)
                    player.add_item(new_armor)
                    player.armor = new_armor
                    print("You found a Shield!")
            else:
                print("You found nothing.")
        elif choice == '2':
            print(f"Status: HP: {player.hp}/{player.max_hp}, Attack: {player.attack}, Defense: {player.defense}, Gold: {player.gold}, Potions: {player.potions}")
        elif choice == '3':
            player.visit_shop()
        elif choice == '4':
            with open("save_game.json", "w") as save_file:
                json.dump(game_state.__dict__, save_file)
            print("Game Saved!")
        elif choice == '5':
            with open("save_game.json", "r") as load_file:
                loaded_state = json.load(load_file)
                game_state.__dict__ = loaded_state
                print("Game Loaded!")
        elif choice == '6':
            print("Exiting the game. Goodbye!")
            break
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    game_loop()

