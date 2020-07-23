import cv2 as cv #import opencv module
import numpy as np #import numpy module

cap = cv.VideoCapture(0);
back = cv.imread('./image.jpg') #Read the background image

while cap.isOpened():
	ret,frame = cap.read()
	if ret:
		hsv = cv.cvtColor(frame,cv.COLOR_BGR2HSV) #BGR color scheme to HSV
		#Find HSV values for the colour of the cloak you want to use. I have used blue here. Select the range as ((hue-10,100,100),(hue+10,255,255))
		l_blue = np.array([110,100,100])
		r_blue = np.array([130,255,255])
		mask = cv.inRange(hsv, l_red, r_red) #Create a mask that only selects colors within the range
		part1 = cv.bitwise_and(back, back, mask=mask) #Take bitwise-and of previously taken background image 'image.jpg' and mask
		mask = cv.bitwise_not(mask) #Create a mask that selects all colors except cloak's color
		part2 = cv.bitwise_and(frame, frame, mask=mask) #Take bitwise-and of current captured frame and the new mask
		cv.imshow("cloak",part1+part2) #Add part1 and part2 (bitwise)

		#To try more morphological effects to make a better cloak, try these effects
		# kernel = np.ones((1,1),np.uint8)
		# dilation = cv.dilate(part1+part2,kernel,iterations = 1)
		# erosion = cv.erode(part1+part2,kernel,iterations = 1)
		# cv.imshow("cloak",dilation)

		if cv.waitKey(5) == ord('q'): #Press q to exit
			break

cap.release()
cv.destroyAllWindows()