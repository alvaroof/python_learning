# -*- coding: utf-8 -*-
import random


class Game:
    is_over = False

    def play():
        player1 = Player(id=1)
        player2 = Player(id=2)
        while not Game.is_over:
            print(player1)
            player1.play_turn()

            print(player2)
            player2.play_turn()

            if player1.wins >= 100 or player2.wins >= 100:
                Game.is_over = True

        print(player1)
        print(player2)

        if player1.wins > player2.wins:
            print("Player 1 Wins")
        elif player1.wins < player2.wins:
            print("Player 2 Wins")
        else:
            print("It's a draw.")


class Player:
    def __init__(self, id: int):
        self.id = id
        self.wins = 0

    def play_turn(self):
        self.wins += random.randint(1, 6)

    def __str__(self):
        return f"Player {self.id} has a total of {self.wins} Wins"


if __name__ == "__main__":
    Game.play()
