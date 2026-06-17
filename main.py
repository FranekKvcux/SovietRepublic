from colorama import init, Fore
import os
from time import sleep


class Game:
    def __init__(self):
        self.username = ""

        self.happiness = 70     # in percentage
        self.food = 50          # in quantity
        self.economy = 50       # in quantity
        self.army = 50          # in quantity

    def clear(self):
        os.system("cls" if os.name == "nt" else "clear")
        print(Fore.YELLOW + " ★ " + Fore.LIGHTRED_EX + "--- SOVIET REPUBLIC --- " + Fore.YELLOW + "★\n")

    def formatUsername(self)->str:
        return Fore.LIGHTYELLOW_EX + self.username + Fore.WHITE
    
    def colorStats(self, text: str)->str:
        return Fore.LIGHTGREEN_EX + text + Fore.WHITE

    def start(self):
        init(autoreset=True)
        self.clear()
        sleep(1)

        self.username = input(" What is your name? > " + Fore.LIGHTYELLOW_EX)
        self.clear()

        sleep(1)
        print(f"Hello {self.formatUsername()} and Welcome to the " + Fore.LIGHTRED_EX + "SOVIET REPUBLIC!")
        sleep(1)
        print(f"Now this is your own country where you have to take care of the {self.colorStats('happiness')} of its citizens, {self.colorStats('food')} supplies, {self.colorStats('economy')} and {self.colorStats('army')}.")
        sleep(1)
        print(f"If any statistic drops to zero, you {Fore.RED + 'lose' + Fore.WHITE}.\n")

        input("Click enter to continue")

if __name__ == "__main__":
    game = Game()
    game.start()