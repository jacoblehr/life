from universe import Universe
import pygame, sys, time

def main():
	width, height = 600, 600
	bg = [255, 255, 255]
	fps = 10
	clock = pygame.time.Clock()

	print("Building universe...")

	screen = pygame.display.set_mode([width, height])
	universe = Universe(pygame.display.get_surface(), 150, 100)
	universe.populate(width=10, height=10, cell_size=30)

	while 1:
		handle_events(universe)
		screen.fill(bg)
		universe.render()
		pygame.display.update()
		clock.tick(fps)

def handle_events(universe):
	for event in pygame.event.get():
		if(event.type == pygame.QUIT):
			print("Destroying universe...")
			sys.exit()
		elif(event.type == pygame.MOUSEBUTTONDOWN):
			universe.handle_event(event)
		elif(event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE):
			universe.simulate()

if(__name__ == "__main__"):
	application = main()