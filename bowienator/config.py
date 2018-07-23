import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
	"""
	Config class
	
	Contains path information for the face detection cascade and the Bowie image.
	"""	
	CASCADE_PATH = os.environ.get('CASCADE_PATH') or os.path.join(basedir,'data','cascade.xml')
	BOWIE_PATH = os.environ.get('BOWIE_PATH') or os.path.join(basedir,'data','bowie.png')