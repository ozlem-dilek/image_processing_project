import cv2 

image = cv2.imread('assets/img.jpg')

grayscale_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
bgr_to_rgb = cv2.cvtColor(image,cv2.COLOR_BGR2RGB)
bgr_to_hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV) 
cv2.imshow("orijinal", image)
cv2.imshow("bgr'dan gri'ye", grayscale_image)
cv2.imshow("bgr'dan rgb'ye", bgr_to_rgb)
cv2.imshow("bgr'dan hsv'ye", bgr_to_hsv)

cv2.waitKey(0) 
cv2.destroyAllWindows()
