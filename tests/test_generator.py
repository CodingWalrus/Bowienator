import pytest, os

import numpy as np

import bowienator

global faces

def test_generator_face_list():
	global faces
	faces = bowienator.face_list(os.path.join(os.path.dirname(os.path.realpath(__file__)),'data','james.png'))
	assert np.all(faces) == np.all([[482, 201, 330, 330]])
	
def test_generator_bowie_draw():
	global faces
	drawn = bowienator.bowie_draw(os.path.join(os.path.dirname(os.path.realpath(__file__)),'data','james.png'),faces)
	assert drawn == True