from abc import ABC


class VideoGameMode(ABC):
    pass


class OnlineMultiplayer(VideoGameMode):
    def play(self):
        print("Playing multiplayer mode...")


class MultiPlayer(VideoGameMode):
    def play(self):
        print("Playing multiplayer mode... ")


class Single(VideoGameMode):

    def play(self):
        print("Playing single mode... ")

class GameModeFacade:
    def selectSinglePlayer(self):
        g.setStrategy(Single)
        print("You select single player.")
        GameplayModeContext(Single).strategy.play(self)

    def selectMultiplayer(self):
        print("You select Multi player.")

        GameplayModeContext(MultiPlayer).strategy.play(self)


    def selectOnlineMultiplayer(self):
        print("You select Online Multiplayer.")
        GameplayModeContext(OnlineMultiplayer).strategy.play(self)

    # def show_option(self):
    #     choice=0
    #     print(f"Press 1 to play single\n"
    #           f"Press 2 to play Mulitiplayer\n"
    #           f"Press 3 to play Online Multiplayer\n")
    #     choice=int(input("Enter your choice: "))
    #     print("_" * 100)
    #     if choice==1:
    #         self.selectSinglePlayer()
    #     elif choice==2:
    #         self.selectMultiplayer()
    #     elif choice==3:
    #         self.selectOnlineMultiplayer()

class GameplayModeContext:
    def __init__(self, setStrategy):
        self.strategy = setStrategy
        self.gamemode=GameModeFacade()


    def play(self):
        return self.strategy.play(self)
    def selectmultiplayer(self):
        return self.gamemode.selectMultiplayer()
    def setStrategy(self, strategy):
        self.strategy = strategy
g=GameplayModeContext(MultiPlayer)
g1=GameplayModeContext(Single)
g.play()
g1.play()
aa = GameModeFacade()
print("_"*100)
aa.selectSinglePlayer()
# aa.selectMultiplayer()
# aa.selectOnlineMultiplayer()
# aa.selectSinglePlayer()
