import os
import pygame

import get_config as conf


class MapHandler:
	def __init__(self, screen):
		self.screen = screen
		self.farm_map = _FarmMap(self.screen)

	def load_map(self):
		self.farm_map.show()
		return True

	def update_map(self, relative_pos, absolute_pos):
		self._set_current_map_position(relative_pos, absolute_pos)
		self.farm_map.show()
		return True

	def _set_current_map_position(self, relative_pos, absolute_pos):
		"""
		It sets the environment variable with map's current starting position.
		:param relative_pos: relative value after a mouse motion event.
		:param absolute_pos: absolute value of mouse motion event.
		:return: True if set successfully else False
		"""
		new_pos_x, new_pos_y = self._calculate_new_position(relative_pos)
		os.environ[conf.get_map_pos_var_name()] = "%d$%d" % (new_pos_x, new_pos_y)
		return True

	def _calculate_new_position(self, relative_pos):
		assert isinstance(relative_pos, tuple) and len(relative_pos) == 2

		prvs_pos_x, prvs_pos_y = map(int, os.environ[conf.get_map_pos_var_name()].split("$"))
		rel_pos_x, rel_pos_y = relative_pos[0], relative_pos[1]

		new_pos_x = prvs_pos_x + rel_pos_x
		new_pos_y = prvs_pos_y + rel_pos_y

		new_pos_x, new_pos_y = self._check_map_boundary(new_pos_x, new_pos_y)
		return new_pos_x, new_pos_y

	@staticmethod
	def _check_map_boundary(pos_x, pos_y):
		size_x, size_y = conf.get_actual_map_size()
		screen_x, screen_y = conf.main_screen_dimensions()

		max_size_x, max_size_y = size_x - screen_x, size_y - screen_y

		if pos_x < 0:
			pos_x = 0
		elif pos_x >= max_size_x:
			pos_x = max_size_x

		if pos_y < 0:
			pos_y = 0
		elif pos_y >= max_size_y:
			pos_y = max_size_y

		return pos_x, pos_y


class _FarmMap:
	def __init__(self, screen):
		self.screen = screen

	def show(self):
		start_x, start_y = map(int, os.environ[conf.get_map_pos_var_name()].split("$"))
		print(start_x, start_y)
