import cv2

image = cv2.imread('img.jpg') #fotoğrafı okuyoruz.
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY) #fotoğrafı griye dönüştürüyoruz.

cv2.imshow("image", image) #fotoğrafı gösterir.
cv2.imshow("gray image", gray_image) #fotoğrafın griye dönüştürülmüş halini gösterir.

cv2.waitKey(0) # fotoğrafın açılıp kapanmaması için. 0 parametresi herhangi bir tuşa bastığımızda kapanmasını sağlar.
cv2.destroyAllWindows() #açık olan tüm ekranlar kapatılır.