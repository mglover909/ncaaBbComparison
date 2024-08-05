import requests
from bs4 import BeautifulSoup
from tabulate import tabulate

def scrape_team_stats(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    # Extract relevant data from the table
    header_row = soup.find('thead').find_all('tr')[1]
    stat_headers = [th.text.strip() for th in header_row.find_all('th')]

    data_rows = soup.find('tbody').find_all('tr')
    team_stats = {}

    for row in data_rows:
        school_name = row.find('th').text.strip()
        stats = [td.text.strip() for td in row.find_all('td')]
        team_stats[school_name] = dict(zip(stat_headers[1:], stats))

    return team_stats

def compare_teams(team_stats, team1, team2, stats_to_compare):
    table_data = [["Stat", team1, team2]]

    for stat in stats_to_compare:
        value_team1 = float(team_stats[team1][stat])
        value_team2 = float(team_stats[team2][stat])

        # Determine color based on comparison (swapped logic for both tables)
        color_team1 = '\033[91m' if stat != "TOV%" and value_team1 < value_team2 else '\033[92m'
        color_team2 = '\033[91m' if stat != "TOV%" and value_team2 < value_team1 else '\033[92m'

        # Special color logic for TOV%
        if stat == "TOV%":
            color_team1 = '\033[92m' if value_team1 < value_team2 else '\033[91m'
            color_team2 = '\033[92m' if value_team2 < value_team1 else '\033[91m'

        # Add colors to the values
        value_team1_colored = f"{color_team1}{value_team1}\033[0m"
        value_team2_colored = f"{color_team2}{value_team2}\033[0m"

        table_data.append([stat, value_team1_colored, value_team2_colored])

    table = tabulate(table_data, headers="firstrow", tablefmt="grid")
    print(table)

def compare_opponent_stats(team_stats, team1, team2, stats_to_compare):
    table_data = [["Stat", team1, team2]]

    for stat in stats_to_compare:
        value_team1 = float(team_stats[team1][stat])
        value_team2 = float(team_stats[team2][stat])

        # Determine color based on comparison (swapped logic for both tables)
        color_team1 = '\033[92m' if stat != "TOV%" and value_team1 < value_team2 else '\033[91m'
        color_team2 = '\033[92m' if stat != "TOV%" and value_team2 < value_team1 else '\033[91m'

        # Special color logic for TOV%
        if stat == "TOV%":
            color_team1 = '\033[91m' if value_team1 < value_team2 else '\033[92m'
            color_team2 = '\033[91m' if value_team2 < value_team1 else '\033[92m'

        # Add colors to the values
        value_team1_colored = f"{color_team1}{value_team1}\033[0m"
        value_team2_colored = f"{color_team2}{value_team2}\033[0m"

        table_data.append([stat, value_team1_colored, value_team2_colored])

    table = tabulate(table_data, headers="firstrow", tablefmt="grid")
    print(table)

if __name__ == "__main__":
    # Scrape team stats
    url_team_stats = "https://www.sports-reference.com/cbb/seasons/men/2024-advanced-school-stats.html"
    team_stats = scrape_team_stats(url_team_stats)

    # Compare team stats
    team1 = input("Enter the name of the first school: ")
    team2 = input("Enter the name of the second school: ")

    stats_to_compare = ["SRS", "SOS", "ORtg", "FTr", "TS%", "TOV%", "ORB%"]

    print("\nTeam Stats Comparison:")
    compare_teams(team_stats, team1, team2, stats_to_compare)

    # Scrape opponent stats
    url_opponent_stats = "https://www.sports-reference.com/cbb/seasons/men/2024-advanced-opponent-stats.html"
    opponent_stats = scrape_team_stats(url_opponent_stats)

    # Compare opponent stats
    print("\nOpponent Stats Comparison:")
    compare_opponent_stats(opponent_stats, team1, team2, stats_to_compare[2:])  # Exclude SRS and SOS




