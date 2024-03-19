import cv2 

image = cv2.imread('assets/img.jpg')
yukseklik, genislik = image.shape[:2] 
merkez =(genislik//2, yukseklik//2)
dondurme_matrisi = cv2.getRotationMatrix2D(merkez, 90, 1) 
dondurulmus_image = cv2.warpAffine(image, dondurme_matrisi, (genislik, yukseklik))

cv2.imshow("image", image)
cv2.imshow("dondurulmus fotograf", dondurulmus_image)

cv2.waitKey(0)
cv2.destroyAllWindows()