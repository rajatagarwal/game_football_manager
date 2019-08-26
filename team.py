import random, copy
from helpers import goals_scored

class Team:
	"""
	A team has a manager. (1.1)
	A team has many players.(1.n)
	A team has ranking in a league. 
	A team plays game against other team.  
	"""
	def __init__(self, name):
		self.name = name
		self.players = []

		self.wins = 0
		self.losses = 0

		# budget at the beginning
		self.money = 1000000


	def weekly_salary(self):
		salary = 0
		for player in self.players:
			salary += player.salary()
		return salary


	def pay_players(self):
		self.money -= self.weekly_salary()

	def rating(self):
		"""
		What is the rating of the team
		"""
		rating = 0
		for player in self.players:
			rating += player.skill
		return rating


	def __str__(self):
		return f"{self.name}-{self.rating()}"


class Game:
	"""
	A game between 2 team
	A game belong to a league
	"""
	def __init__(self, league, home_team, away_team):
		self.league = league
		self.home_team = home_team
		self.away_team = away_team

		self.home_team_won = None
		self.away_team_won = None

		print(f" {self.home_team} vs. {self.away_team}")

	def play(self):
		"""
		Play a game and return who won
		True means home team won, otherwise
		Away team won
		"""
		print("play begins.")
		goals_by_home_team = goals_scored(self.home_team.rating())
		goals_by_away_team = goals_scored(self.away_team.rating())

		print(f"Home team scored {goals_by_home_team}")
		print(f"Away team scored {goals_by_away_team}")

		print("play ends.")

		if goals_by_home_team == goals_by_away_team:
			if self.home_team.rating() > self.away_team.rating():
				print(f"Match Draw. {self.home_team} wins based on rating.")
				self.home_team_won = True
			else:
				print(f"Match Draw. {self.away_team} wins based on rating.")
				self.away_team_won = True
		else:
			if goals_by_home_team > goals_by_away_team:
				print(f"{self.home_team} wins by {goals_by_home_team} - {goals_by_away_team}")
				self.home_team_won = True
			else:
				print(f"{self.home_team} wins by {goals_by_away_team} - {goals_by_home_team}")
				self.away_team_won = True


class League:
	"""
	A league has many teams
	Each team has ranking in the league
	"""
	def __init__(self, name, teams, players):
		self.name = name
		self.teams = teams
		self.players = players
		self.round_played = 0

	def set_teams(self, teams):
		self.teams = teams


	def play_round(self):
		"""
		Play a round, which is 3 games
		"""

		num_team = len(self.teams)
		num_games = num_team // 2

		# making copy of the list
		# doing copy.copy so it will not 
		# remove data from original list.
		# because in python if you just
		# assign a list to another list
		# like, teams_to_play = self.teams
		# then it would remove data from 
		# self.teams even if you try to 
		# delete data from teams_to_play
		teams_to_play = copy.copy(self.teams)

		print("Round begins...")
		for game_num in range(num_games):
			home_team = random.choice(teams_to_play)
			teams_to_play.remove(home_team)
			away_team = random.choice(teams_to_play)
			
			game = Game(self, home_team, away_team)
			game.play()
			self.resolve_game(game)

		print("Round ends...")
		print("")
		self.round_played += 1
		self.ladder()

	# ladder status
	

	def ladder(self):
		print("******* LADDER *******")
		for team in sorted(self.teams, key=lambda t: -t.wins):
			print(f"{team} {team.wins} wins.")
		print("**********************")


	def resolve_game(self, game):
		prize_amount = round(200000 * random.random())
		if game.home_team_won:
			# home team won
			game.home_team.wins += 1
			game.away_team.losses += 1
			# add prize money out of max 200000
			game.home_team.money += prize_amount
			print("")
			print(f"{game.home_team} won {prize_amount}.")
			print("")
		else:
			# away team won
			game.away_team.wins += 1
			game.home_team.losses += 1
			# add prize money out of max 200000
			game.away_team.money += round(20000 * random.random())
			print("")
			print(f"{game.away_team} won {prize_amount}.")
			print("")

		game.home_team.pay_players()
		game.away_team.pay_players()