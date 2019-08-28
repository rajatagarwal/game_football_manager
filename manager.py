from helpers import select_from_menu

class TeamManager:
	"""
	A manager runs a team
	"""
	def __init__(self, team, league):
		self.team = team
		self.league = league

		self.inputs = {
			1: self.view_players,
			2: self.view_market,
			3: self.trade_players,
			4: self.next_round
		}

		self.finished = False

		print("You are a manager.")
		print(f"You manage {self.team}")
		print("Good Luck.")


	def get_team_status(self):
		print("")
		print(f"Your team is {self.team}")
		print(f"""Your team status out of {self.league.round_played} round(s):
			Played {self.team.wins + self.team.draw + self.team.losses} game(s)
			{self.team.wins} win(s)
			{self.team.draw} draw(s)
			{self.team.losses} loss(es)""")
		
		print(f"You currently have ${self.team.money}")
		print(f"Your team weekly salary is ${self.team.weekly_salary()}.")		
		print("")


	def manage(self):
		"""
		Before every round we can
		make changes as a manager.
		"""
		self.finished = False
		
		self.get_team_status()

		while not self.finished:
			self.print_menu()
			select_from_menu(self.inputs)

		print("")


	def print_menu(self):
		print("1. View your team players")
		print("2. View players on the market")
		print("3. Trade players")
		print("4. Play the next round")


	def view_players(self):
		print("Player Name | Skill | Salary")
		for idx, player in enumerate(self.team.players):
			print(f"{idx}: {player}")


	def next_round(self):
		print("Next round")
		self.finished = True


	def view_market(self):
		for idx, player in enumerate(self.league.players):
			print(f"{idx}: {player}")


	def trade_players(self):
		"""
		Switch a player from your team
		for a free agent.
		"""
		# select a player from your team
		self.view_players()
		player_index = int(input("Which player do you want to switch:"))

		# select a player from free agent
		self.view_market()
		market_index = int(input("Which player do you want to hire:"))
		print("")

		# switch them
		print(f"Switching {self.team.players[player_index]} for {self.league.players[market_index]}")
	
		# Remove your player from your team
		# and free agent you chose from the 
		# market		
		player_from_team = self.team.players.pop(player_index)
		player_from_market = self.league.players.pop(market_index)

		# Now add each player to there new list
		self.team.players.append(player_from_market)
		self.league.players.append(player_from_team)
