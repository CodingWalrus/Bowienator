import os
basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
	CASCADE_PATH = os.environ.get('CASCADE_PATH') or os.path.join(basedir,'data','cascade.xml')
	BOWIE_PATH = os.environ.get('BOWIE_PATH') or os.path.join(basedir,'data','bowie.png')
	SCALE_FACTOR = os.environ.get('SCALE_FACTOR') or 1.1
	MIN_NEIGHBORS = os.environ.get('MIN_NEIGHBORS') or 5
	MIN_SIZE = os.environ.get('MIN_SIZE') or (30,30)