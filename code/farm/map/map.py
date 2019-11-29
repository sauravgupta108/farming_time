import os
import json
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
		self.pathways = None

	def show(self):
		self._draw_pathways()

	def _draw_pathways(self):
		self._load_pathways_from_config()
		assert self.pathways is not None

		pathways = self.pathways["pathways"]
		point_format = self.pathways["point_format"]
		length_units = self.pathways["units"]
		width = self.pathways["width"]

		for pathway in pathways:
			pathway_rect = self._get_rect_of_pathway(pathway, length_units, point_format, width)
			if self.path_in_viewable_map(pathway_rect):
				self._draw_pathway(pathway, pathway_rect)

	def _load_pathways_from_config(self):
		with open(os.path.join(os.getcwd(), "farm/map/map_config/pathways.json")) as pathways:
			self.pathways = json.load(pathways)

	def _draw_pathway(self, pathway, pathway_rect):
		rect_in_map = self._get_rect_in_map(pathway_rect)

	@staticmethod
	def _get_rect_of_pathway(pathway, length_units, point_format, width):
		multiplier = 0
		if length_units == "feet":
			multiplier = 12
		elif length_units == "inches":
			multiplier = 1

		assert multiplier != 0

		if point_format == "end_2":
			pass

		starting_point_x = int(pathway["pos_x"]) * multiplier
		starting_point_y = int(pathway["pos_y"]) * multiplier
		length_of_pathway = int(pathway["length"]) * multiplier
		width = int(width) * multiplier
		direction_x = int(pathway["direction"]["x_axis"])
		direction_y = int(pathway["direction"]["y_axis"])

		top_left = None
		rect_width, rect_height = None, None

		if direction_x == -1 and direction_y == 0:
			top_left = (starting_point_x - length_of_pathway, starting_point_y - width)
			rect_width = length_of_pathway
			rect_height = width

		elif direction_x == 0 and direction_y == -1:
			top_left = (starting_point_x - width, starting_point_y - length_of_pathway)
			rect_width = width
			rect_height = length_of_pathway
		return pygame.Rect(top_left[0], top_left[1], rect_width, rect_height)

	@staticmethod
	def path_in_viewable_map(path_rect):
		cur_map_rect = conf.get_current_map_rect()

		if path_rect.x + path_rect.width <= cur_map_rect.x or \
			path_rect.y + path_rect.height <= cur_map_rect.y or \
			cur_map_rect.x + cur_map_rect.width <= path_rect.x or \
			cur_map_rect.y + cur_map_rect.height <= path_rect.y:
			return False

		return True

	def _get_rect_in_map(self, path_rect):
		cur_map_rect = conf.get_current_map_rect()
		print(cur_map_rect.colliderect(path_rect))
		return False
