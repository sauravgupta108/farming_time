import pygame

from get_config import get_frame_rate
from .map import MapHandler


class LetsFarm:
	def __init__(self, screen, clock):
		self.land = screen
		self.clock = clock

	def start(self):
		is_farming = True
		# try:
		while is_farming:
			self.clock.tick(get_frame_rate())
			for action in pygame.event.get():
				if action.type == pygame.QUIT:
					is_farming = False

				elif action.type == pygame.KEYDOWN:
					if action.key == pygame.K_l:
						self.get_map()

				elif action.type == pygame.MOUSEBUTTONDOWN:
					# Just to reset the relative position.
					pygame.mouse.get_rel()

				elif bool(pygame.mouse.get_pressed()[0]):
					if action.type == pygame.MOUSEMOTION:
						self.update_map(pygame.mouse.get_rel(), pygame.mouse.get_pos())

		pygame.quit()
		return 0
		# except:
		# 	return 1

	def get_map(self):
		from .map import MapHandler
		is_map_loaded = MapHandler(self.land).load_map()
		print("Map Loaded: ", is_map_loaded)

	def update_map(self, relative_pos, absolute_pos):
		from .map import MapHandler
		is_updated = MapHandler(self.land).update_map(relative_pos, absolute_pos)
