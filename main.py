from utils import create_players, create_cup, leaderboard, die_table_to_cup, face_table_to_cup

def main():
	players = create_players()
	cup = create_cup()
	print("\n"*20)
	game_won = False
	while(not game_won):
		for player in players:
			leaderboard(players)
			print("{}'s turn".format(player.name))

			loop = True
			dice = [cup.shake(), cup.shake(), cup.shake()]
			table = []
			shotguns = 0
			brains = 0
			energy_drink = False
			helmet = False

			while(loop):
				loop = False
				dice = [(die, die.roll()) for die in dice]
				[print("Rolled {} ({})".format(face, die)) for die, face in dice]
				table.extend(dice)
				

				for name, face in [(die.name, face) for die, face in dice]:
					if name == 'Hunk Dice' and (face == 'shotgun' or face == 'double_shotgun'):
						if ('Hottie Dice', 'brain') in [(die.name, face) for die, face in table]:
							print("Hottie returned to cup!")
							cup.dice, table = die_table_to_cup('Hottie Dice', cup.dice, table)
							brains -= 1
					elif name == 'Hottie Dice' and face == 'shotgun':
						if ('Hunk Dice', 'brain') in [(die.name, face) for die, face in table]:
							print("Hunk returned to cup!")
							cup.dice, table = die_table_to_cup('Hunk Dice', cup.dice, table)
							brains -= 1
						elif ('Hunk Dice', 'double_brain') in [(die.name, face) for die, face in table]:
							print("Hunk returned to cup!")
							cup.dice, table = die_table_to_cup('Hunk Dice', cup.dice, table)
							brains -= 2
					elif name == 'Santa Dice':
						if face == 'energy_drink':
							energy_drink = True
						elif face == helmet:
							helmet = True

				if energy_drink:
					for i, (die, face) in zip(range(len(dice)+1),dice):
						if die.name == 'Green Dice':
							dice[i]=(die,'brain')
				
				brains += len([face for die, face in dice if face == "brain"]) + 2*len([face for die, face in dice if face =="double_brain"])
				shotguns += len([face for die, face in dice if face == "shotgun"]) + 2*len([face for die, face in dice if face =="double_shotgun"])

				print("-"*10)
				print(cup.dice)
				# print(table)
				print(len(cup.dice)+len(table))
				print("-"*10)
				
				print("{0}'s brains: {1}\t{0}'s shotguns:{2}".format(player.name, brains, shotguns))

				if shotguns >= 3+int(helmet):
					break

				print("-"*10)
				dice.clear()
				if((input("Keep rolling [Y/N]?: ")).lower() == 'y'):
					loop = True
					dice.extend([die for die, face in table if face == "footprint"])
					table = [(die, face) for die, face in table if face != "footprint"]
					while(len(dice)<3):
						try:
							dice.append(cup.shake())
						except:
							print("Cup refilled w/ brains!")
							cup.dice.extend([die for die, face in table if face == "brain"])
							table = [(die, face) for die, face in table if face != "brain"]
				else:
					player.score += brains

			print("{}'s score: {}!".format(player.name, player.score))
			cup.dice.extend([die for die, face in table])
			if player.score >= 13:
				print("{} won!!".format(player.name))
				leaderboard(players)
				game_won = True
				break

if __name__ == "__main__":
	main()