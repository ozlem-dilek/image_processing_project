import cv2 

img = cv2.imread('img.jpg', cv2.IMREAD_GRAYSCALE)
ret, thresh = cv2.threshold(img,70,255,cv2.THRESH_BINARY)

cv2.imshow("orijinal", img)
cv2.imshow("binarize", thresh)
cv2.imshow("~binarize", ~thresh)

cv2.waitKey(0) 
cv2.destroyAllWindows()
