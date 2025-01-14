import cv2
import imutils

# read image
img = cv2.imread('burger.png')

# resize
resizeImg = imutils.resize(img, width=100)

# grayscale
grayimg = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

# blur
bluring = cv2.GaussianBlur(img, (21,21), 0)

#show image
cv2.imshow("original", img)
cv2.imshow("resize", resizeImg)
cv2.imshow("gray" , grayimg)
cv2.imshow("blur" , bluring)

cv2.waitKey(0)
cv2.destroyAllWindows()