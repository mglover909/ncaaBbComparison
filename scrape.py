import pandas as pd
from tabulate import tabulate

def load_data(file_path):
    return pd.read_csv(file_path)

def get_team_stats(df, team_name):
    # Retrieve the row corresponding to the team name
    team_data = df[df['School'].str.contains(team_name, case=False, na=False)]
    if not team_data.empty:
        return team_data.iloc[0].to_dict()
    return None

def print_comparison_table(stats_team1, stats_team2, stats_to_compare, color_logic):
    table_data = [["Stat", "Team 1", "Team 2"]]
    
    for stat in stats_to_compare:
        value_team1 = float(stats_team1[stat])
        value_team2 = float(stats_team2[stat])

        # Determine colors based on the comparison and logic specified
        if stat == "TOV%":
            if color_logic == "reversed":
                # For opponent stats, higher TOV% is green
                color_team1 = '\033[92m' if value_team1 > value_team2 else '\033[91m'
                color_team2 = '\033[92m' if value_team2 > value_team1 else '\033[91m'
            else:
                # For team stats, lower TOV% is green
                color_team1 = '\033[91m' if value_team1 > value_team2 else '\033[92m'
                color_team2 = '\033[91m' if value_team2 > value_team1 else '\033[92m'
        else:
            if color_logic == "normal":
                color_team1 = '\033[92m' if value_team1 > value_team2 else '\033[91m'
                color_team2 = '\033[92m' if value_team2 > value_team1 else '\033[91m'
            else:  # color_logic == "reversed"
                color_team1 = '\033[91m' if value_team1 > value_team2 else '\033[92m'
                color_team2 = '\033[91m' if value_team2 > value_team1 else '\033[92m'

        value_team1_colored = f"{color_team1}{value_team1}\033[0m"
        value_team2_colored = f"{color_team2}{value_team2}\033[0m"

        table_data.append([stat, value_team1_colored, value_team2_colored])

    table = tabulate(table_data, headers="firstrow", tablefmt="grid")
    print(table)

def main():
    # Load data
    df1 = load_data('bballRefSpread.csv')
    df2 = load_data('bballRefSpreadOpp.csv')

    # User input
    team1_name = input("Enter the name of the first school: ")
    team2_name = input("Enter the name of the second school: ")

    # Retrieve stats
    stats_team1 = get_team_stats(df1, team1_name)
    stats_team2 = get_team_stats(df1, team2_name)

    if stats_team1 is None or stats_team2 is None:
        print("One or both of the schools were not found in the dataset.")
        return

    # Stats to compare
    stats_to_compare = ["SRS", "SOS", "ORtg", "FTr", "TS%", "TOV%", "ORB%"]

    # Print comparison table for the first spreadsheet
    print("\nTeam Stats Comparison (bballRefSpread):")
    print_comparison_table(stats_team1, stats_team2, stats_to_compare, "normal")

    # Retrieve stats for opponent comparison
    stats_team1_opponent = get_team_stats(df2, team1_name)
    stats_team2_opponent = get_team_stats(df2, team2_name)

    if stats_team1_opponent is None or stats_team2_opponent is None:
        print("One or both of the schools were not found in the opponent dataset.")
        return

    # Print comparison table for the second spreadsheet
    print("\nOpponent Stats Comparison (bballRefSpreadOpp):")
    print_comparison_table(stats_team1_opponent, stats_team2_opponent, ["ORtg", "FTr", "TS%", "TOV%", "ORB%"], "reversed")

if __name__ == "__main__":
    main()
