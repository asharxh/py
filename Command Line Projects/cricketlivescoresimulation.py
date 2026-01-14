def cricket_live_score_simulation():
    match = {
        "team1": {"name": "Team A", "players": ["Player A1", "Player A2", "Player A3", "Player A4", "Player A5"], "runs": 0, "wickets": 0, "balls": 0, "extras": 0, "player_scores": {}},
        "team2": {"name": "Team B", "players": ["Player B1", "Player B2", "Player B3", "Player B4", "Player B5"], "runs": 0, "wickets": 0, "balls": 0, "extras": 0, "player_scores": {}}
    }

    for player in match["team1"]["players"]:
        match["team1"]["player_scores"][player] = 0
    for player in match["team2"]["players"]:
        match["team2"]["player_scores"][player] = 0

    print("Welcome to Cricket Live Score Simulation!")
    print("Teams:", match["team1"]["name"], "vs", match["team2"]["name"])
    batting_team_key = "team1"
    bowling_team_key = "team2"

    while True:
        print("\nCurrent Score Board:")
        batting_team = match[batting_team_key]
        print(f"{batting_team['name']} - Runs: {batting_team['runs']}, Wickets: {batting_team['wickets']}, Overs: {batting_team['balls']//6}.{batting_team['balls']%6}, Extras: {batting_team['extras']}")
        print("Player Scores:")
        for player, score in batting_team["player_scores"].items():
            print(f"{player}: {score} runs")
        
        action = input("\nEnter action (ball/run/wicket/extra/switch/exit): ")

        if action.lower() == "exit":
            print("Ending simulation.")
            break
        elif action.lower() == "switch":
            batting_team_key, bowling_team_key = bowling_team_key, batting_team_key
            print(f"Switched batting team. Now {match[batting_team_key]['name']} is batting.")
            continue
        elif action.lower() == "wicket":
            if batting_team["wickets"] >= len(batting_team["players"]) - 1:
                print("All out! Switching innings.")
                batting_team_key, bowling_team_key = bowling_team_key, batting_team_key
                continue
            batting_team["wickets"] += 1
            batting_team["balls"] += 1
            print("Wicket fallen!")
        elif action.lower() == "extra":
            extra_runs_input = input("Enter extra runs (wide/no-ball etc.): ")
            if extra_runs_input.isdigit():
                extra_runs = int(extra_runs_input)
                batting_team["runs"] += extra_runs
                batting_team["extras"] += extra_runs
                print(f"Added {extra_runs} extras.")
            else:
                print("Invalid input for extras.")
        elif action.lower() == "run":
            player_name = input("Enter batsman name: ")
            if player_name not in batting_team["player_scores"]:
                print("Invalid player name.")
                continue
            runs_input = input("Enter runs scored: ")
            if not runs_input.isdigit():
                print("Invalid run input.")
                continue
            runs = int(runs_input)
            batting_team["runs"] += runs
            batting_team["balls"] += 1
            batting_team["player_scores"][player_name] += runs
        else:
            print("Invalid action. Use ball/run/wicket/extra/switch/exit.")

        overs_completed = batting_team["balls"] / 6
        run_rate = batting_team["runs"] / overs_completed if overs_completed > 0 else 0
        print(f"Current Run Rate: {run_rate:.2f} runs per over")

    print("\nFinal Score Summary:")
    for team_key in ["team1", "team2"]:
        team = match[team_key]
        print(f"\n{team['name']} - Runs: {team['runs']}, Wickets: {team['wickets']}, Overs: {team['balls']//6}.{team['balls']%6}, Extras: {team['extras']}")
        print("Player Scores:")
        for player, score in team["player_scores"].items():
            print(f"{player}: {score} runs")

cricket_live_score_simulation()