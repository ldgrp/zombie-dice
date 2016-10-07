from models import Player, Dice, Cup

def create_green_dice():
	return Dice('Green Dice', 
				['shotgun','brain','brain','footprint','footprint','shotgun'])
def create_yellow_dice():
	return Dice('Yellow Dice', 
				['brain','brain','footprint','footprint','shotgun','shotgun'])
def create_red_dice():
	return Dice('Red Dice', 
				['brain','footprint','footprint','shotgun','shotgun','shotgun'])

def create_hunk_dice():
	return Dice('Hunk Dice', 
				['shotgun','double_shotgun','footprint','footprint','shotgun','double_brain'])
def create_hottie_dice():
	return Dice('Hottie Dice', 
				['brain','shotgun','shotgun','footprint','footprint','footprint'])
def create_santa_dice():
	return Dice('Santa Dice',
				['energy_drink','footprint','shotgun','double_brain','brain','helmet'])
def create_normal_cup():
	return Cup('Normal',
			   [create_green_dice(), create_green_dice(), create_green_dice(), create_green_dice(),
			    create_green_dice(), create_green_dice(), create_yellow_dice(), create_yellow_dice(),
			    create_yellow_dice(), create_yellow_dice(), create_red_dice(), create_red_dice(), create_red_dice()])

def create_action_cup():
	return Cup('Big Summer Action Movie',
			   [create_green_dice(), create_green_dice(), create_green_dice(), create_green_dice(),
			    create_green_dice(), create_green_dice(), create_yellow_dice(), create_yellow_dice(),
			    create_hunk_dice(), create_red_dice(), create_red_dice(), create_red_dice(), create_hottie_dice()])
def create_santa_cup():
	return Cup('Santa Claus Meets The Zombies',
		[create_red_dice(), create_green_dice(), create_green_dice(), create_green_dice(),
		create_green_dice(), create_green_dice(), create_yellow_dice(), create_yellow_dice(),
		create_yellow_dice(), create_yellow_dice(), create_red_dice(), create_santa_dice(), create_red_dice()])
def create_dtv_cup():
	return Cup('Santa Claus Meets The Zombies',
		[create_red_dice(), create_green_dice(), create_green_dice(), create_green_dice(),
		create_green_dice(), create_green_dice(), create_hottie_dice(), create_yellow_dice(),
		create_hunk_dice(), create_yellow_dice(), create_red_dice(), create_santa_dice(), create_red_dice()])
def create_players():
	players = []
	for i in range(0, int(input("Input player count: "))):
		name = input("Input Player {}'s name: ".format(i+1))
		players.append(Player(i, name))
	return players

def create_cup():
	game_type = str(input("Input game type ([N]ormal, [A]ction Movie, [S]anta, [D]-T-V Sequel): ")).lower()[0]
	if game_type == 'n':
		return create_normal_cup()
	elif game_type == 'a':
		return create_action_cup()
	elif game_type == 's':
		return create_santa_cup()
	elif game_type == 'd':
		return create_dtv_cup()
	else:
		pass
def leaderboard(players):
	print("\n{0}".format('*'*30))
	print("Leaderboard".upper())
	print("{0}".format('*'*30))
	
	for p in players:
		print("\t---\t{}:\t{}".format(p.name,p.score))
	print("{0}\n".format('*'*30))

def die_table_to_cup(name, x, y):
	x.extend([die for die, face in y if die.name == name])
	y = [(die, face) for die, face in y if die.name != name]
	return x, y

def face_table_to_cup(face, x, y):
	x.extend([die for die, face in y if face == face])
	y = [(die, face) for die, face in y if face != face]
	return x, y
