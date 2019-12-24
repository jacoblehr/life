import math, pygame
from cell import Cell

class Universe:

	# Attributes
	width = 0
	height = 0
	cell_size = 0
	state = None
	offset_x = 0
	offset_y = 0
	cell_hover = None

	# Initialiser
	def __init__(self, surface, offset_x=0, offset_y=0):
		self.surface = surface
		self.offset_x = offset_x
		self.offset_y = offset_y

	def populate(self, width, height, cell_size=30):
		self.width = width
		self.height = height
		self.cell_size = cell_size
		self.state = list(range(0, width))

		for x in range(width):
			self.state[x] = list(range(0, height))
			for y in range(height):
				self.state[x][y] = Cell(self, x, y, cell_size)

	# Render function
	def render(self):
		pygame.draw.rect(
			self.surface, 
			(0, 0, 0), 
			(
				self.offset_x - 1, 
				self.offset_y - 1, 
				self.width * self.cell_size + 2, 
				self.height * self.cell_size + 2
			),
			1
		)
		for x in range(self.width):
			for y in range(self.height):
				current_cell = self.state[x][y]
				current_cell.render()
		
	# Simulate a generation
	def simulate(self):
		for x in range(self.width):
			for y in range(self.height):
				current_cell = self.state[x][y]
				num_neighbours = 0

				for ix in range(-1, 2):
					for iy in range(-1, 2):
						if(not (ix == 0 and iy == 0)):
							try:
								x_index = x + ix
								y_index = y + iy
								if(x_index >= 0 and y_index >= 0):
									next_cell = self.state[x + ix][y + iy]
									if(next_cell.state):
										num_neighbours = num_neighbours + 1
							except Exception:
								pass
				self.state[x][y].update_state(num_neighbours)
		self.update_cells()
		self.render()

	def handle_event(self, event):
		if(event.type == pygame.MOUSEBUTTONDOWN):
			cell = self.get_cell(event.pos[0], event.pos[1])
			if(cell != None):
				cell.state = not cell.state
		if(event.type == pygame.MOUSEMOTION and pygame.mouse.get_pressed()[0]):
			cell = self.get_cell(event.pos[0], event.pos[1])
			if(cell != None and self.cell_hover != cell):
				self.cell_hover = cell
				cell.state = not cell.state

	def get_cell(self, x, y):
		x_index = math.floor((x - self.offset_x) / self.cell_size)
		y_index = math.floor((y - self.offset_y) / self.cell_size)

		if(0 <= x_index < self.width and 0 <= y_index < self.height):
			return self.state[x_index][y_index]
		else:
			return None

	def update_cells(self):
		for x in range(self.width):
			for y in range(self.height):
				self.state[x][y].update()

