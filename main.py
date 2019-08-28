import random

from team import League, Team
from player import generate_player
from manager import TeamManager

def main():
	# Set Up

	# Generate some players
	players = []
	for i in range(100):
		players.append(generate_player())


	# Set up 5 teams
	teams = [
		Team("Chelsea"),
		Team("Man City"),
		Team("Arsenal"),
		Team("West Ham"),
		Team("Man Utd"),
		Team("Hull City"),
	]

	# Giving players to team
	for team in teams:
		for player_num in range(11):
			selected_player = random.choice(players)
			team.players.append(selected_player)
			players.remove(selected_player)


	# We have a single league
	first_league = League("Premiership League", teams, players)
	first_league.set_teams(teams)

	# create the manager
	manager = TeamManager(random.choice(teams), first_league)

	print("Season begins...")
	for i in range(10):
		manager.manage()
		first_league.play_round()
	print("Season ends...")
	
	print("*" * 30)
	print("Your final score card.")
	manager.get_team_status()
	print("*" * 30)


if __name__ == "__main__":
	main()