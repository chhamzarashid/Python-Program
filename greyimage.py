from cv2 import cv2
img=cv2.imread("1.jpg")
cv2.imshow("Hamza",img)
cv2.waitKey(0)
cv2.destroyAllWindows()
#convert to greyscale

greyimage=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
cv2.imwrite("Newfile.jpg",greyimage)
cv2.imshow("Hamza",greyimage)
cv2.waitKey(0)
cv2.destroyAllWindows()