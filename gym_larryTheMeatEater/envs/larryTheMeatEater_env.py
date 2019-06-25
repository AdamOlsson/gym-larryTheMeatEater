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
		self.start_pos = 0
		self.end_pos = self.world_size[0]*self.world_size[1]
		#self.death_objects_pos = []
		self.player_pos = self.start_pos
		self.player_previous_pos = None

		# RL params
		#self.game_over = False
		#self.reward = 0

		# printing
		#self.flatten = lambda l: [item for sublist in l for item in sublist]


	def step(self, action):
		# returns a list containing new state, the reward for current state, a bool saying game over and 
		# additional info of our problem
		if action == 'u':
			self.player_pos += 8
		elif action == 'd':
			self.player_pos += -8
		elif action == 'l':
			self.player_pos += 1
		elif action == 'r':
			self.player_pos += -1
		
		#self.world[self.player_pos[0]][[self.player_pos[1]]] = 'H'
		#self.world[self.player_previous_pos[0]][self.player_previous_pos[1]] = ' '

		return [self.world, self.reward, self.game_over, None]

	def reset(self):
		#resets to state
		self.world = []
		for x in range(self.world_size[0]*self.world_size[1]):
			self.world.append([' '])

		self.player_pos = self.start_pos
		self.player_previous_pos = self.player_pos
		self.world[self.player_pos] = 'H'

		#self.world[self.end_pos[0]][self.end_pos[1]] = 'R' # R for reward
		
		#self.game_over = False
		#self.reward = 0
		

		return self.world

	def render(self, mode='human', close=False):
		# basically print the board
		#for y in reversed(self.world):
		#	for x in y:
		#		print("[{}]".format(x), end ='')
		#	print('\n')

		#flat = self.flatten(self.world)

		self.world[self.player_previous_pos] = ' '
		self.world[self.player_pos] = 'H'
		self.player_previous_pos = self.player_pos

		# This will make the output overwritten in the terminal
		print(	"[{}][{}][{}][{}][{}][{}][{}][{}]\n"
			  	"[{}][{}][{}][{}][{}][{}][{}][{}]\n"
				"[{}][{}][{}][{}][{}][{}][{}][{}]\n"
				"[{}][{}][{}][{}][{}][{}][{}][{}]\n"
				"[{}][{}][{}][{}][{}][{}][{}][{}]\n"
				"[{}][{}][{}][{}][{}][{}][{}][{}]\n"
				"[{}][{}][{}][{}][{}][{}][{}][{}]\n"
				"[{}][{}][{}][{}][{}][{}][{}][{}]\n".format(
					self.world[56],self.world[57],self.world[58],self.world[59],self.world[60],self.world[61],self.world[62],self.world[63],
					self.world[48],self.world[49],self.world[50],self.world[51],self.world[52],self.world[53],self.world[54],self.world[55],
					self.world[40],self.world[41],self.world[42],self.world[43],self.world[44],self.world[45],self.world[46],self.world[47],
					self.world[32],self.world[33],self.world[34],self.world[35],self.world[36],self.world[37],self.world[38],self.world[39],
					self.world[24],self.world[25],self.world[26],self.world[27],self.world[28],self.world[29],self.world[30],self.world[31],
					self.world[16],self.world[17],self.world[18],self.world[19],self.world[20],self.world[21],self.world[22],self.world[23],
					self.world[8] ,self.world[9] ,self.world[10],self.world[11],self.world[12],self.world[13],self.world[14],self.world[15],
					self.world[0] ,self.world[1] ,self.world[2] ,self.world[3] ,self.world[4] ,self.world[5] ,self.world[6] ,self.world[7],), end='\r')

if __name__=='__main__':
	env = larryTheMeatEater_env()
	env.reset()
	env.render()

	#while True:
	#	pass
	
