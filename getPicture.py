
import cv2


def getPicture():
	camera = cv2.VideoCapture(0)
	return_value, image = camera.read()
	cv2.imwrite('mood'+'.jpg', image)
	del(camera)
