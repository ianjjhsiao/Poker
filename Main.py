import Game
import tkinter
game = Game.Game(200)
game.shuffleCards()
# for x in game.deck:
#     print(x)
game.addPlayer("Player One")
game.addPlayer("Player Two")
game.addPlayer("Player Three")
game.addPlayer("Player Four")
game.addPlayer("Player Five")
game.deal()
for y in range(len(game.players)):
    print(game.players[y].name, end=":\n")
    print(str(game.players[y].hand[0]), end=", ")
    print(str(game.players[y].hand[1]))

for x in game.board:
    print(str(x),end=" ")

