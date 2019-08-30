import random

def select_from_menu(menu_options: dict):
	selection = input("Make selections:")
	# Do some dodgy things :)
	action = menu_options.get(int(selection), None)
	
	if action is None:
		print("Invalid selection")			
	else:
		print("")
		action()
		print("")


def goals_scored(rating):
	# rating * random number between 1 to 5 / rating
	return int(( rating * random.randint(1,5) / rating ))


def elo_rating(opponents_elo, wins, losses, games):
	"""
	https://en.wikipedia.org/wiki/Elo_rating_system
	
	Performance rating = Total of opponent's rating + 400 * (win - losses)
	                     -------------------------------------------------
	                                      Total Games
	""" 
	rating = (opponents_elo + (400 * (wins - losses))) // games
	return rating