import cv2 

image = cv2.imread('img.jpg')
yukseklik, genislik = image.shape[:2] #image.shape'ten dönen ilk iki değeri alıyoruz.
#çünkü sonuncu değer bize fotoğrafın 3 kanallı olduğunu yani r-g-b olduğunu belirtiyor.

merkez =(genislik//2, yukseklik//2) #fotoğrafın koordinatlarının merkezini alıyoruz, döndürme işlemi için.

dondurme_matrisi = cv2.getRotationMatrix2D(merkez, 90, 1) #90 derece döndürme açısı verdik.
#1 parametresi ise yakınlaştırma/uzaklaştırma olmayacağını belirtiyor.

dondurulmus_image = cv2.warpAffine(image, dondurme_matrisi, (genislik, yukseklik))

cv2.imshow("image", image)
cv2.imshow("dondurulmus fotograf", dondurulmus_image)

cv2.waitKey(0)
cv2.destroyAllWindows()