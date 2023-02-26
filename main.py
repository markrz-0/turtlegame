from engine.basegame import BaseGame
from scenes.error import ErrorScene
from scenes.matchmaking import MatchmakingScreen
from scenes.menu import MainMenuScene
from scenes.play import PlayScene


class TurtleGame(BaseGame):
    def __init__(self):
        super().__init__()
        self.add_scene(MainMenuScene)
        self.add_scene(MatchmakingScreen)
        self.add_scene(PlayScene)
        self.add_scene(ErrorScene)
        self.title("Turtle Game")



def main():
    game = TurtleGame()
    game.loop()

if __name__ == '__main__':
    main()
