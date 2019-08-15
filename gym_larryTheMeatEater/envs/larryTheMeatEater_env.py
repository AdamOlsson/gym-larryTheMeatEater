import gym
from gym import error, spaces, utils
from gym.utils import seeding
import keyboard, time, curses
#import arcade

class larryTheMeatEater_env(gym.Env):
	metadata = {'render.modes': ['human']}

	def __init__(self):
		
		# World
		self.world_size = [8,8]
		self.world = []
		self.start_pos = None
		self.end_pos = None
		self.death_pos = []

		self.player_pos = [0, 0]
		self.player_previous_pos = [0, 0]

		# RL params
		self.game_over = False
		self.reward = 0

		# printing
		curses.initscr()
		self.screen = curses.newwin(10,10)
		self.screen.keypad(True)
		curses.curs_set(0) 
		curses.noecho()
		curses.cbreak()


	def step(self, action):

		self.player_previous_pos[0] = self.player_pos[0]
		self.player_previous_pos[1] = self.player_pos[1]

		if action == 'w':
			self.player_pos[1] = max(0, self.player_pos[1]-1)
		elif action == 's':
			self.player_pos[1] = min(self.world_size[1]-1, self.player_pos[1]+1)
		elif action == 'a':
			self.player_pos[0] = max(0, self.player_pos[0]-1)
		elif action == 'd':
			self.player_pos[0] = min(self.world_size[0]-1, self.player_pos[0]+1)
		
		if self.player_pos == self.end_pos:
			self.game_over = True
			#self.reset()
		self.render()

		return [self.world, self.reward, self.game_over, None]

	def reset(self):

		## TODO:: Add a load map fcn	

		self.screen.clear()
		self.screen.border(0)

		self.start_pos = [0,0]
		self.end_pos = [self.world_size[0]-1, self.world_size[1]-1]

		#resets to state
		self.world = []
		for x in range(self.world_size[0]*self.world_size[1]):
			self.world.append(' ')

		# To pevent same address
		self.player_pos[0] = self.start_pos[0]
		self.player_pos[1] = self.start_pos[1]
		self.player_previous_pos[0] = self.start_pos[0]
		self.player_previous_pos[1] = self.start_pos[1]

		self.world[self.player_pos[0] + self.player_pos[1]*8] = 'H'

		# Put win location on board
		win_pos = self.end_pos[0] + self.end_pos[1]*8
		self.world[win_pos] = 'X'

		## TODO: Put death locations on board
		
		self.game_over = False
		self.reward = 0
		
		return self.world


	def loadMap(self):
		pass


	def render(self, mode='human', close=False):

		# Remove old pos from board
		player_prev_world_pos = self.player_previous_pos[0] + self.player_previous_pos[1]*8
		self.world[player_prev_world_pos] = ' '

		# Put in new pos on board
		player_world_pos = self.player_pos[0] + self.player_pos[1]*8
		self.world[player_world_pos] = 'H'

		for y in range(self.world_size[0]):
			for x in range(self.world_size[1]):
				self.screen.addstr(1+y,1+x, self.world[y*8 + x])

		## TODO: Add a game info box

		#self.screen.addstr(4,2, "({},{})".format(self.end_pos[0], self.end_pos[1]))
		#self.screen.addstr(5,2, "({},{})".format(self.player_pos[0], self.player_pos[1]))

		#self.screen.addstr(8,8, u"\u2588")

		self.screen.refresh()

	def quit(self):
		curses.nocbreak()
		self.screen.keypad(False)
		curses.echo()
		curses.curs_set(1)
		curses.endwin()
		

if __name__=='__main__':

	env = larryTheMeatEater_env()
	env.reset()
	env.render()
	try:
		while True:
			action = env.screen.getkey()
			state = env.step(action)
			if state[2] == True:
				break
		env.quit()
	except Exception as e:
		env.quit()
		print(e)
	
