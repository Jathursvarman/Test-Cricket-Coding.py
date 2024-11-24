import random

# Initialize teams and scores
teams = ["Team A", "Team B"]
scores = {"Team A": 0, "Team B": 0}
wickets = {"Team A": 0, "Team B": 0}
innings = 2  # Each team gets two innings
overs_per_inning = 5  # Number of overs per inning (you can adjust this)
balls_per_over = 6

def play_innings(team_name):
    print(f"\n{team_name} is batting now!")
    team_score = 0
    team_wickets = 0
    
    for over in range(1, overs_per_inning + 1):
        if team_wickets >= 10:
            print(f"All out! {team_name}'s innings ends early.")
            break
        print(f"\nOver {over}:")
        for ball in range(1, balls_per_over + 1):
            if team_wickets >= 10:
                break
            batsman_score = random.randint(0, 6)  # Random score for the batsman
            bowler_delivery = random.randint(1, 6)  # Random delivery by bowler
            if batsman_score == bowler_delivery:
                team_wickets += 1
                print(f"Ball {ball}: OUT! Wickets: {team_wickets}/10")
            else:
                team_score += batsman_score
                print(f"Ball {ball}: Scored {batsman_score} runs. Total: {team_score}/{team_wickets}")
    print(f"\n{team_name} ends their innings with {team_score}/{team_wickets}.")
    return team_score, team_wickets

def play_match():
    print("Welcome to the Python Test Match Game!")
    for inning in range(1, innings + 1):
        print(f"\n--- Inning {inning} ---")
        for team in teams:
            print(f"\n{team}'s Turn:")
            score, wicket = play_innings(team)
            scores[team] += score
            wickets[team] += wicket
            print(f"\n{team} has scored {scores[team]} in total after {inning} innings.")
    
    # Decide the winner
    print("\n--- Match Results ---")
    print(f"{teams[0]}: {scores[teams[0]]} runs")
    print(f"{teams[1]}: {scores[teams[1]]} runs")
    if scores[teams[0]] > scores[teams[1]]:
        print(f"{teams[0]} wins the match by {scores[teams[0]] - scores[teams[1]]} runs!")
    elif scores[teams[0]] < scores[teams[1]]:
        print(f"{teams[1]} wins the match by {scores[teams[1]] - scores[teams[0]]} runs!")
    else:
        print("The match is a draw!")

if __name__ == "__main__":
    play_match()
