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


# def adjust_ratings(rating, result):
# 	"""
# 	Logic to adjust rating based on the result

# 	"""
# 	if away.won:
# 		if away.rating > home.rating:
# 			diff = away.rating - home.rating
# 			# send positive number, which need to be added to the team
# 			return diff/22
# 		else:
# 			# high rating team lost to low rating team. more reward and penalty
# 			return diff/11 from higher team
# 			and may be diff/22 for lower team
