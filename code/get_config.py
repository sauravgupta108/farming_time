import os
import json


def _load_configurations():
	"""
	Loads the configuration file
	:return: dictionary of config values
	"""
	config = None
	with open(os.path.join(os.getcwd(), "config.json")) as conf_file:
		config = json.load(conf_file)
	return config


def main_screen_dimensions():
	"""
	:return: tuple (i.e. (int, int)) of main screen's size. (width, height)
	"""
	config = _load_configurations()
	assert config is not None
	return int(config["MAIN_SCREEN"]["WIDTH"]), int(config["MAIN_SCREEN"]["HEIGHT"])


def screen_title():
	"""
	:return: str - Title of screen defined in configuration file.
	"""
	config = _load_configurations()
	assert config is not None
	return config["MAIN_SCREEN"]["TITLE"]


def get_frame_rate():
	"""
	:return: int - Frames per cycle defined in configuration file.
	"""
	config = _load_configurations()
	assert config is not None
	try:
		return int(config["FRAME_RATE"])
	except ValueError:
		return None


def get_screen_origin():
	return 0, 0


def get_map_pos_var_name():
	"""
	:return: str, name of environment variable to hold latest position
	"""
	config = _load_configurations()
	assert config is not None
	return config["MAP"]["ENV_VAR_NAME"]


def get_initial_map_pos():
	"""
	:return: x, y - initial position of map as per configuration file
	"""
	config = _load_configurations()
	assert config is not None
	try:
		return int(config["MAP"]["INITIAL"]["X_POS"]), int(config["MAP"]["INITIAL"]["Y_POS"])
	except ValueError:
		return None, None


def get_actual_map_size():
	return 12000, 10000

