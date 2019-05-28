import gym
from gym import error, spaces, utils
from gym.utils import seeding
import keyboard
#import arcade

class larryTheMeatEater_env(gym.Env):
	metadata = {'render.modes': ['human']}

	def __init__(self):
		
		# World
		self.world_size = (8,8)
		self.world = None
		self.start_pos = (0,0)
		self.end_pos = [7,7]
		self.death_objects_pos = []
		self.player_pos = self.start_pos
		self.player_previous_pos = None

		# RL params
		self.game_over = False
		self.reward = 0

		# printing
		self.flatten = lambda l: [item for sublist in l for item in sublist]


	def step(self, action):
		# returns a list containing new state, the reward for current state, a bool saying game over and 
		# additional info of our problem
		if action == 'u':
			self.player_pos += (0,1)
		elif action == 'd':
			self.player_pos += (0,-1)
		elif action == 'l':
			self.player_pos += (-1,0)
		elif action == 'r':
			self.player_pos += (0,1)
		
		self.world[self.player_pos[0]][[self.player_pos[1]]] = 'H'
		self.world[self.player_previous_pos[0]][self.player_previous_pos[1]] = ' '

		return [self.world, self.reward, self.game_over, None]

	def reset(self):
		#resets to state
		self.world = []
		for y in range(self.world_size[0]):
			self.world.append([])
			for x in range(self.world_size[1]):
				self.world[y].append(' ')

		self.player_pos = self.start_pos
		self.world[self.end_pos[0]][self.end_pos[1]] = 'R' # R for reward
		self.world[self.player_pos[0]][self.player_pos[1]] = 'H'
		self.game_over = False
		self.reward = 0
		self.player_previous_pos = None

		return self.world

	def render(self, mode='human', close=False):
		# basically print the board
		#for y in reversed(self.world):
		#	for x in y:
		#		print("[{}]".format(x), end ='')
		#	print('\n')

		flat = self.flatten(self.world)

		# This will make the output overwritten in the terminal
		print(	"[{}][{}][{}][{}][{}][{}][{}][{}]\n"
			  	"[{}][{}][{}][{}][{}][{}][{}][{}]\n"
				"[{}][{}][{}][{}][{}][{}][{}][{}]\n"
				"[{}][{}][{}][{}][{}][{}][{}][{}]\n"
				"[{}][{}][{}][{}][{}][{}][{}][{}]\n"
				"[{}][{}][{}][{}][{}][{}][{}][{}]\n"
				"[{}][{}][{}][{}][{}][{}][{}][{}]\n"
				"[{}][{}][{}][{}][{}][{}][{}][{}]\n".format(
					flat[56],flat[57],flat[58],flat[59],flat[60],flat[61],flat[62],flat[63],
					flat[48],flat[49],flat[50],flat[51],flat[52],flat[53],flat[54],flat[55],
					flat[40],flat[41],flat[42],flat[43],flat[44],flat[45],flat[46],flat[47],
					flat[32],flat[33],flat[34],flat[35],flat[36],flat[37],flat[38],flat[39],
					flat[24],flat[25],flat[26],flat[27],flat[28],flat[29],flat[30],flat[31],
					flat[16],flat[17],flat[18],flat[19],flat[20],flat[21],flat[22],flat[23],
					flat[8] ,flat[9] ,flat[10],flat[11],flat[12],flat[13],flat[14],flat[15],
					flat[0] ,flat[1] ,flat[2] ,flat[3] ,flat[4] ,flat[5] ,flat[6] ,flat[7],), end='\r')

if __name__=='__main__':
	env = larryTheMeatEater_env()
	env.reset()
	env.render()

	#while True:
	#	pass
	
