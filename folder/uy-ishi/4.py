
import random

def game(n):
    player = "Sardor"
    p = 1
    while p < n:
        multiplier = random.randint(2, 9)
        p *= multiplier
        player = "Odina" if player == "Sardor" else "Sardor"
    player = player if p == n else "Sardor" if player == "Odina" else "Odina"
    print(f"{player} win!")

# print(random.randint(2, 100))
game(10)