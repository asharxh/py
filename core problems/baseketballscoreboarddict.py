def basketball_scoreboard():
    team_scores = {}
    total_teams_input = input("Enter number of teams: ")
    total_teams = int(total_teams_input)
    team_count = 0
    while team_count < total_teams:
        team_name = input("Enter team name: ")
        points_input = input("Enter total points for " + team_name + ": ")
        points = int(points_input)
        team_scores[team_name] = points
        team_count = team_count + 1
    print("Basketball Scoreboard:")
    for team in team_scores:
        print(team, "has", team_scores[team], "points")
    highest_points = 0
    winner_team = ""
    for team in team_scores:
        if team_scores[team] > highest_points:
            highest_points = team_scores[team]
            winner_team = team
    print("Winning Team:", winner_team, "with", highest_points, "points")

basketball_scoreboard()
