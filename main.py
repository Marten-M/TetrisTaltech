"""Main code to execute."""
import pygame

def main():
    pygame.init()
    from src.lib.game import Game
    
    game = Game("TitleScreen")
    game.run()


if __name__ == "__main__":
    main()
