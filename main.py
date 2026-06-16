from colorama import init, Fore
import os


class Game:
    def __init__(self):
        self.username = ""

    def clear(self):
        os.system("cls" if os.name == "nt" else "clear")
        print(Fore.YELLOW + " ★ " + Fore.LIGHTRED_EX + "--- SOVIET REPUBLIC --- " + Fore.YELLOW + "★\n")

    def getUsername(self)->str:
        return Fore.LIGHTYELLOW_EX + self.username + Fore.WHITE
    
    def colorStats(self, text: str)->str:
        return Fore.LIGHTGREEN_EX + text + Fore.WHITE

    def start(self):
        init(autoreset=True)
        self.clear()

        self.username = input(" What is your name? > " + Fore.LIGHTYELLOW_EX)
        self.clear()

        print(f"Hello {self.getUsername()} and Welcome to the " + Fore.LIGHTRED_EX + "SOVIET REPUBLIC!")
        print(f"Now this is your own country where you have to take care of the {self.colorStats('happiness')} of its citizens, {self.colorStats('food')} supplies, {self.colorStats('economy')} and {self.colorStats('military')}.\n")


if __name__ == "__main__":
    g1 = Game()
    g1.start()