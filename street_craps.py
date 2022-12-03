from sc_game_pkg import menu

import random


menu.show_menu()

database = {"name": "bankroll"}
ante = []
point = int()


class Game():
    def __init__(self, name):
        self.name = name


class shooter():
    def __init__(self, name):
        # super().__init__(name)

        while True:
            # show_homepage()
            global point

            selection = input("Choose an option")
            if selection == "1":
                player = input("Enter your name").lower()
                money = int(input("Enter amount of bet"))
                AUTHORIZED_USER = (database, player.lower(), money)
            elif selection == "2":
                print('''Street Craps Rules

    The human player will be the shooter.
    The shooter will then need to make a bet followed by the CPU player. The CPU 
    player must have enough money in its bankroll to match the shooter's bet.
    If the CPU cannot match the shooter's bet, then the shooter wins the game.

    The come out roll comes next. This is the game’s first roll and it could end
    the game if it is a 7, 11, 2, 3 or 12. The shooter and any other player who bet
    in favor of the shooter win the game if a 7 or 11 is rolled. If a 2, 3 or 12
    come up when the dice are rolled the shooter and other players who bet for him
    lose.

    A Point number, which is a number other than those mentioned above, must be set up.
    So if the come out roll is not any of those numbers listed above that number will
    be designated as the point number.

    The roll is next and the goal is for the shooter to roll the number identified as the
    point before he rolls a 7. The 7 is referred to an “Out 7” and once the shooter gets
    this before rolling the point he loses the game.

    Rolling dice proceeds until a 7 or the Point is rolled. The shooter loses if the 7 comes
    up and wins if the Point is rolled. If other numbers are rolled the shooter continues
    rolling the dice. The round ends only after a 7 or the point is rolled.
''')

            def bets():
                cpu_bet = random.randint(1, 100)
                print("The CPU bets", cpu_bet)

            def dice_roll():

                #point = int()
                dice_1 = random.randint(1, 6)
                dice_2 = random.randint(1, 6)
                total = dice_1 + dice_2
                print("\nYou rolled a...", dice_1, "\nYou rolled a...", dice_2)
                if total == 7 or 11:
                    print("You win!")
                elif total == 2 or total == 3 or total == 12:
                    print("You lose.")
                else:
                    if total == 4 or total == 5 or total == 6 or total == 8 or total == 9 or total == 10:
                        print("The point is", total)
                        total = point
                        # point_roll(point)

            def point_roll(total):
                total = point
                dice_1 = random.randint(1, 6)
                dice_2 = random.randint(1, 6)
                total = dice_1 + dice_2
                print("\nYou rolled a...", dice_1, "\nYou rolled a...", dice_2)
                print("\nYou have rolled a total of:", total)


name = "Joe"
shooter(name)
