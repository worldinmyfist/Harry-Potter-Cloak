import cv2 as cv #import opencv module

cap = cv.VideoCapture(0); #Open Camera

while cap.isOpened():
	ret,back = cap.read() 
	if ret: #If camera is working
		cv.imshow("image",back) #Show captured Background image
		if cv.waitKey(5) == ord('q'): #Press q to exit
			cv.imwrite('image.jpg', back) #Save image
			break

cap.release()
cv.destroyAllWindows()