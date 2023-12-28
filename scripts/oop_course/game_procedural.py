# -*- coding: utf-8 -*-
import random

if __name__ == "__main__":
    is_over = False
    player1 = 0
    player2 = 0
    while not is_over:
        print(f"Player 1: {player1}")
        print(f"Player 2: {player2}")
        player1 += random.randint(1, 6)
        player2 += random.randint(1, 6)
        if player1 >= 100 or player2 >= 100:
            is_over = True
    print(f"Player 1: {player1}")
    print(f"Player 2: {player2}")
