def rps(p1, p2):
    if p1=="rock" and p2=="paper":
        return "Player 2 won!"
    elif p2=="rock" and p1=="paper":
        return "Player 1 won!"
    elif p2=="scissors" and p1=="paper":
        return "Player 2 won!"
    elif p2=="rock" and p1=="rock":
        return "Draw!"
    elif p2=="paper" and p1=="scissors":
        return "Player 1 won!"
    elif p2=="paper" and p1=="paper":
        return "Draw!"
    elif p2=="rock" and p1=="scissors":
        return "Player 2 won!"
    elif p2=="scissors" and p1=="rock":
        return "Player 1 won!"
    else:
        return "Draw!"