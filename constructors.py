import random


class Fruit:
    def __init__(self, name, heal_amount, cost):
        self.name = name
        self.heal_amount = heal_amount
        self.cost = cost


class Player:
    def __init__(self, name):
        self.name = name
        self.level = 1
        self.hp = 100
        self.max_hp = 100
        self.gold = 50

    def level_up(self):
        self.level += 1
        self.max_hp += 20
        self.hp = self.max_hp
        self.gold += random.randint(10, 30)
        print(
            f"✨Congratulations {self.name}! You reached level {self.level}. Your HP reset to 100 and your current gold is {self.gold}.")

    def taken_dmg(self):
        dmg_taken = random.randint(5, 25)
        self.hp -= dmg_taken
        print(f"💥You took {dmg_taken} damage!")
        if self.hp <= 0:
            print(f"😭 {self.name} You hit 0 HP! ")

            # if they hit 0 they drop a level(can't go below level 1)
            if self.level > 1:
                self.level -= 1
                self.hp = 100
                print(f"📉 You dropped a level! HP reset to 100")
            else:
                self.hp = 100
                print(f"{self.name} you are level 1. HP reset to 100!")

    def eats_fruit(self, fruit):
        if self.gold < fruit.cost:
            print(f"{self.name} not enough gold to heal. {fruit.name} costs {fruit.cost}g. (You have: {self.gold}g) ")
            return
        if self.hp >= self.max_hp:
            print(f"🤢 You are already at max health ({self.hp}/{self.max_hp})")

        self.gold -= fruit.cost
        self.hp += fruit.heal_amount

        if self.hp > self.max_hp:
            self.hp = self.max_hp

        print(
            f"You ate {fruit.name}! Healed for {fruit.heal_amount} HP: {self.hp}/{self.max_hp} | Gold left: {self.gold}  ")

    def stats(self):
        print(f"""
=======================
Player : {self.name}
Level  : {self.level}
HP     : {self.hp}/{self.max_hp}
Gold   : {self.gold} 
======================= 
""")


berries = Fruit("🫐 Wild Berries", 5, 3)
apple = Fruit("🍎 Red Apple", 20, 15)
mango = Fruit("🥭 Golden Mango", 40, 30)
melon = Fruit("🍉 Water Melon", 75, 60)

hero = Player(input("Enter your name : "))

while True:
    choice = input("Did you take any damage (yes(y)/no(n)) (heal(h)/quit(q)) and (stats(s)) : ").lower()

    if choice == "y":
        hero.taken_dmg()
    elif choice == "n":
        hero.level_up()
    elif choice == "h":
        print(f"""
🛒 --- Welcome to the shop --- 🛒 
1. {berries.name} (+{berries.heal_amount} HP) - Cost {berries.cost}g
2. {apple.name} (+{apple.heal_amount} HP) - Cost {apple.cost}g
3. {mango.name} (+{mango.heal_amount} HP) - Cost {mango.cost}g
4. {melon.name} (+{melon.heal_amount} HP) - Cost {melon.cost}g

""")
        shop_choice = input("Which fruit would you like to buy? (Enter 1-4): ")

        if shop_choice == "1":
            hero.eats_fruit(berries)
        elif shop_choice == "2":
            hero.eats_fruit(apple)
        elif shop_choice == "3":
            hero.eats_fruit(mango)
        elif shop_choice == "4":
            hero.eats_fruit(melon)
        else:
            print(f"Pls enter no (1-4) only. Enter h to return to shop")

    elif choice == "s":
        hero.stats()
    elif choice == "q":
        print(f"Thanks for playing !")
        break
    else:
        print("Please enter y, n, q, h or s as your input")
