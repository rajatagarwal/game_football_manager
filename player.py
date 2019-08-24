import names, random

class Player:
	"""
	A player is on a single team with other players,
	A player plays in a game for a team
	"""

	def __init__(self, name, skill):
		self.name = name

		# Players gonna have rankings
		self.skill = skill


	def salary(self):
		return 5000 + self.skill * 100


	def __str__(self):
		return f"{self.name} | {self.skill} | {self.salary()}"

def generate_player():
	full_name = names.get_full_name(gender="male")

	# Generate skill
	skill = 10 + random.randint(0, 90)

	return Player(full_name, skill)

