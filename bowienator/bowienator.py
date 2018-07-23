"""
bowienator img_dir [-h] [-scale] [-minNeighbors] [-minSize]

Summary:
	The Bowienator is a script to detect faces in a photo and draw over them with a David Bowie face.
	
Args:	
	img_dir (str) - A string of the path to the image file you want Bowiefied
	-h - Displays the help arguments for the script
	-scale (float) - Used to set the scale of the image pyramid used by opencv
	-minNeighbors (int) - Determines the minimum number of neighboring rectangles before a candidate rectangle is detected
	-minSize (ints) - Determines the smallest window the cascade will detect
					- Note: the minSize is represented by two integers, which are turned into a tuple

Returns:
	True, and saves the Bowiefied copy of the picture to the same directory of the img_dir argument
	
Example:

>>> bowienator example/image -scale 1.2 -minNeighbors 3 -minSize 20 20
True
	
The image with Bowie drawn over top is saved in the same directory as example_image
"""

import cv2, os

from PIL import Image

def face_list(imagePath,scale_factor=1.1,min_neighbors=5,min_size=(30,30),cascade_path=os.path.join(os.path.dirname(__file__),'data','cascade.xml')):
	"""
	face_list(imagePath,scale_factor,min_neighbors,min_size,cascade_path)
	
	Summary: 
		Finds all faces in the provided photograph, returns a list of face data sets
	
	Args:
		imagePath (str) - A string of the path to the image file you want to read
		scale_factor (float) - Used to set the scale of the image pyramid used by opencv
		min_neighbors (integer) - Determines the minimum number of neighboring rectangles before a candidate rectangle is detected
		min_size (tuple) - Determines the smallest window the cascade will detect
		cascade_path (str) - contains the path to the cascade used to do face detection
	
	Returns:
		An array of arrays containing positional and dimensional data for detected faces
	
	Examples:
	
	Let's suppose there is an image with two faces you want to detect.
	
	>>> face_list(example_image,1.2,3,(20,20),path/to/cascade)
	[[x1,y1,w1,h1],[x2,y2,w2,h2]]
	
	Where [x1,y1,w1,h1] is an array of the x value, y value, width and height of the first face detected.
	"""
	
	face_cascade = cv2.CascadeClassifier(cascade_path)
	
	gray_image = cv2.imread(imagePath, 0)
	
	faces = face_cascade.detectMultiScale(
		gray_image,
		scaleFactor=scale_factor,
		minNeighbors=min_neighbors,
		minSize=min_size,
		flags = cv2.CASCADE_SCALE_IMAGE
	)
	return faces
	
def bowie_draw(imagePath,face_coords,bowie_path=os.path.join(os.path.dirname(__file__),'data','bowie.png')):
	"""
	bowie_draw(imagePath,face_coords,bowie_path)
	
	Summary:
		Draws the Bowie face over every point found by the face_list function
	
	Args:
		imagePath (str) - A string of the path to the image file you want to draw over
		face_coords (array) - An array of arrays, each one with the positional and dimensional data for a detected face
		bowie_path (str) - A string of the path to the image file that will be used to draw on the image
	
	Returns:
		Saves the image with the drawn-on Bowies, returns True to signal error-free completion
	
	Examples:
	
	Consider the image we detected before, with the two faces. Consider the face data to be stored in the faces variable.
	
	>>> bowie_draw(example_image,faces,path/to/bowie/image)
	True
	
	The image with Bowie drawn over top is saved in the same directory as example_image
	"""
	background = Image.open(imagePath)
	bowie_face = Image.open(bowie_path)
	for (x,y,w,h) in face_coords:
		new_bowie = bowie_face.resize((int(w*1.25),int(h*1.6)))
		background.paste(new_bowie,(int(x-0.125*w),int(y-0.3815*h)),new_bowie)
	background.save(os.path.splitext(imagePath)[0] + " Bowiefied.png","PNG")
	return True
	
if __name__ == "__main__":
	import argparse
	from config import Config

	parser = argparse.ArgumentParser(description='Finds all faces in a picture, and pastes a picture of David Bowie\'s face over them.')
	parser.add_argument('img_dir',
					help = 'Path to the image to run through the Bowienator.')
	parser.add_argument('-scale',default=1.1,type=float,
					help = 'Sets the scale factor for the computer vision.')
	parser.add_argument('-minNeighbors',default=5,type=int,
					help = 'Sets the minimum neighbours for the computer vision.')
	parser.add_argument('-minSize',default=(30,30),nargs=2,type=int,
					help = 'Sets the minimum face size for the computer vision.')
	
	args = parser.parse_args()
	
	all_faces = face_list(args.img_dir,args.scale,args.minNeighbors,args.minSize,Config.CASCADE_PATH)
	bowie_draw(args.img_dir,all_faces,Config.BOWIE_PATH)