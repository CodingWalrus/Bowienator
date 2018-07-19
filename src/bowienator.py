import cv2, argparse, os

from PIL import Image

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

Config.SCALE_FACTOR = args.scale
Config.MIN_NEIGHBORS = args.minNeighbors
Config.MIN_SIZE = tuple(args.minSize)

def face_list(imagePath,config):
	face_cascade = cv2.CascadeClassifier(config.CASCADE_PATH)
	
	gray_image = cv2.imread(imagePath, 0)
	
	faces = face_cascade.detectMultiScale(
		gray_image,
		scaleFactor=config.SCALE_FACTOR,
		minNeighbors=config.MIN_NEIGHBORS,
		minSize=config.MIN_SIZE,
		flags = cv2.CASCADE_SCALE_IMAGE
	)
	return faces
	
def bowie_draw(imagePath,face_coords,config):
	background = Image.open(imagePath)
	bowie_face = Image.open(config.BOWIE_PATH)
	for (x,y,w,h) in face_coords:
		new_bowie = bowie_face.resize((int(w*1.25),int(h*1.6)))
		background.paste(new_bowie,(int(x-0.125*w),int(y-0.3815*h)),new_bowie)
	background.save(os.path.splitext(imagePath)[0] + " Bowiefied.png","PNG")
	
all_faces = face_list(args.img_dir,Config)
bowie_draw(args.img_dir,all_faces,Config)