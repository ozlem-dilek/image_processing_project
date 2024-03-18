import cv2 

image = cv2.imread('img.jpg')

#opencv'nin varsayılan renk uzayı bgr'dır.
grayscale_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) #fotoğrafı griye dönüştürüyoruz.
bgr_to_rgb = cv2.cvtColor(image,cv2.COLOR_BGR2RGB) #bgr'dan rgb'ye dönüşüm.
bgr_to_hsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV) #bgr'dan hsv'ye (hue-saturation-value (ton-doygunluk-değer)) dönüşüm

cv2.imshow("orijinal", image)
cv2.imshow("bgr'dan gri'ye", grayscale_image)
cv2.imshow("bgr'dan rgb'ye", bgr_to_rgb)
cv2.imshow("bgr'dan hsv'ye", bgr_to_hsv)

cv2.waitKey(0) 
cv2.destroyAllWindows()
