import cv2 

image = cv2.imread('assets/img.jpg') #fotoğrafı okuyoruz.

#opencv'de yakınlaştırma ve uzaklaştırma işlemlerini yeniden boyutlandırarak (resize) ile yaparız.
yakinlastirilmis = cv2.resize(image, None, fx= 2.0, fy=2.0, interpolation=cv2.INTER_LINEAR )
#fx ve fy yakınlaştırma ölçeğimiz.
#dsize yerine yeni boyutumuz verilir fakat biz boyut yerine ölçek (fx ve fy) belirttik.
#ölçek belirttiğimiz için dsize parametresini dikkate almadık ve None olarak verdik.

# interpolasyon bilinen veriler arasındaki eksik değerleri hesaplamak için kullanılan bir tekniktir.
# görüntü işleme için, bir pikselin değerini bilinen komşu piksellerin değerlerinden türetmek için kullanılır.
# bizim kullandığımız "inter linear" (çift doğrusal interpolasyon) yöntemi ise
#pikselin x ve y koordinatlarına en yakın 4 komşu pikselin değerlerini kullanır. genel amaçlı kullanılan bir yöntemdir.


uzaklastirilmis = cv2.resize(image, None, fx= 0.1, fy=0.1, interpolation=cv2.INTER_AREA )

cv2.imshow("yakinlastirilmis", yakinlastirilmis)
cv2.imshow("orijinal", image)
cv2.imshow("uzaklastirilmis", uzaklastirilmis)


cv2.waitKey(0)
cv2.destroyAllWindows()