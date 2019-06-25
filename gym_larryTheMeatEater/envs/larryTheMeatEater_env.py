import gym
from gym import error, spaces, utils
from gym.utils import seeding
import keyboard, time, curses
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
		self.game_over = False
		self.reward = 0

		# printing
		curses.initscr()
		self.screen = curses.newwin(10,10)
		self.screen.keypad(True)
		curses.noecho()
		curses.cbreak()


	def step(self, action):

		action = self.screen.getkey() # temporary for testing

		# returns a list containing new state, the reward for current state, a bool saying game over and 
		# additional info of our problem
		if action == 'w':
			self.player_pos += -8
		elif action == 's':
			self.player_pos += 8
		elif action == 'a':
			self.player_pos += -1
		elif action == 'd':
			self.player_pos += 1
		
		#self.world[self.player_pos[0]][[self.player_pos[1]]] = 'H'
		#self.world[self.player_previous_pos[0]][self.player_previous_pos[1]] = ' '

		self.render()

		return [self.world, self.reward, self.game_over, None]

	def reset(self):

		self.screen.clear()
		self.screen.border(0)

		#resets to state
		self.world = []
		for x in range(self.world_size[0]*self.world_size[1]):
			self.world.append(' ')

		self.player_pos = self.start_pos
		self.player_previous_pos = self.player_pos
		self.world[self.player_pos] = 'H'

		#self.world[self.end_pos[0]][self.end_pos[1]] = 'R' # R for reward
		
		self.game_over = False
		self.reward = 0
		

		return self.world

	def render(self, mode='human', close=False):

		self.world[self.player_previous_pos] = ' '
		self.world[self.player_pos] = 'H'
		self.player_previous_pos = self.player_pos

		for y in range(self.world_size[0]):
			for x in range(self.world_size[1]):
				self.screen.addstr(1+y,1+x, self.world[y*8 + x] )

		self.screen.refresh()

	def quit(self):
		curses.nocbreak()
		self.screen.keypad(False)
		curses.echo()

		curses.endwin()
		

if __name__=='__main__':

	env = larryTheMeatEater_env()
	env.reset()
	env.render()
	try:
		for x in range(5):
			env.step('d')
		env.quit()
	except:
		env.quit()
	
