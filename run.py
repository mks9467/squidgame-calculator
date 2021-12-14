import main

counter = 0
average = 0
total = 0
games = 100000
threesTotal = 0

for i in range(0, games):
    game = main.Game(i)
    game.setup_game()
    game.play_game()
    for j in range(1, 17):
        if game.results[j] == True:
            counter += 1
    total = total + counter
    if counter == 3:
        threesTotal += 1
    counter = 0

average = total / games

print('Total Games: ' + str(games))
print('Average survived: ' + str(round(average, 5)))
print('Percentage of games with 3 winners: ' + str(round(threesTotal/games * 100, 5)) + '%')