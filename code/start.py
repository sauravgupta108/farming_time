import pygame
import os

import get_config as conf
from farm import LetsFarm


def _set_main_screen(dimensions, title="default"):
	assert isinstance(dimensions, tuple)
	assert len(dimensions) == 2
	assert dimensions[0] != 0 and dimensions[1] != 0

	pygame.display.set_caption(title)

	# Set initial map position.
	initial_pos = conf.get_initial_map_pos()
	os.environ[conf.get_map_pos_var_name()] = "%d$%d" % (initial_pos[0], initial_pos[1])

	return pygame.display.set_mode(dimensions)


def _game_clock():
	return pygame.time.Clock()


def _show_splash_screen(screen):
	assert isinstance(screen, pygame.Surface)
	splash_win = pygame.image.load("assets/agriculture.jpg")
	screen.blit(splash_win, conf.get_screen_origin())
	pygame.display.flip()


def start_app():
	pygame.init()
	main_screen = _set_main_screen(conf.main_screen_dimensions(), title=conf.screen_title())
	clock = _game_clock()
	_show_splash_screen(main_screen)
	exit_code = LetsFarm(main_screen, clock).start()

	if exit_code == 0:
		print("Break Time.")
	else:
		print("Problem....")
	

if __name__ == '__main__':
	start_app()