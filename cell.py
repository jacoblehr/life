import pygame, random, enum

class CellState(enum.Flag):
	ALIVE = True
	DEAD = False

class Cell:
	# Attributes
	universe = None
	x = 0
	y = 0
	state = CellState.DEAD
	next_state = None

	# Initialiser
	def __init__(self, universe, x, y, size, state = CellState.DEAD):
		self.universe = universe
		self.x = x
		self.y = y
		self.size = size
		self.state = state

	# Render function
	def render(self):
		pygame.draw.rect(
			self.universe.surface, 
			(0, 0, 0), 
			(
				self.x * self.universe.cell_size + self.universe.offset_x, 
				self.y * self.universe.cell_size + self.universe.offset_y, 
				self.size, 
				self.size
			),
			0 if self.state else 1
		)

	def update_state(self, num_neighbours):
		self.next_state = self.state
		if(self.state):
			if(num_neighbours < 2 or num_neighbours > 3):
				self.next_state = CellState.DEAD
		else:
			if(num_neighbours == 3):
				self.next_state = CellState.ALIVE

	def update(self):
		self.state = self.next_state
	