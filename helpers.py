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
