import os
import json


def _load_configurations():
	config = None
	with open(os.path.join(os.getcwd(), "config.json")) as conf_file:
		config = json.load(conf_file)
	return config

def main_screen_dimensions():
	config = _load_configurations()
	assert config is not None
	return (int(config["MAIN_SCREEN"]["WIDTH"]), int(config["MAIN_SCREEN"]["HEIGHT"]))	

def screen_title():
	config = _load_configurations()
	assert config is not None
	return config["MAIN_SCREEN"]["TITLE"]

def get_frame_rate():
	config = _load_configurations()
	assert config is not None
	try:
		return int(config["FRAME_RATE"])
	except ValueError:
		return None

def get_screen_origin():
	return (0, 0)
