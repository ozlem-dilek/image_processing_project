import cv2 

image = cv2.imread('assets/img.jpg')
kirpilmis_image = image[0:200, 0:400]

print(image.shape)

cv2.imshow("kirpma islemi uygulanmis fotograf", kirpilmis_image)
cv2.imshow("image", image)

cv2.waitKey(0)
cv2.destroyAllWindows()