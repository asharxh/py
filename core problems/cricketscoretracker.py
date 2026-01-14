def cricket_score_tracker():
    players = {}
    total_players_input = input("Enter number of players: ")
    total_players = int(total_players_input)
    count = 0
    while count < total_players:
        player_name = input("Enter player name: ")
        runs_input = input("Enter runs scored by " + player_name + ": ")
        runs = int(runs_input)
        players[player_name] = runs
        count = count + 1
    print("Cricket Scoreboard:")
    for name in players:
        print(name, "scored", players[name], "runs")
    total_runs = 0
    for name in players:
        total_runs = total_runs + players[name]
    print("Total Team Runs:", total_runs)

cricket_score_tracker()