import cv2
import numpy as np

image = cv2.imread('benedict_cumberbatch.jpg')

print(str(image.item(100, 100, 0))) #mavi rengin 100 e 100 pikselindeki piksel karşlığı
print(str(image.item(100, 100, 1))) #yeşil rengin 100 e 100 pikselindeki piksel karşlığı
print(str(image.item(100, 100, 2))) # kırmızı rengin 100 e 100 pikselindeki piksel karşlığı

#image.itemset((100,100,2),255)#100e 100 noktasındaki noktanın rengini değiştirir.
image2 = cv2.imread('benedict_cumberbatch.jpg', 0)

print(str(image.shape))#resmin boyutu ve renk çeşitleri
print(str(image2.shape))#resmin boyutu ve renk çeşitleri

print(str(len(image.shape)))#parametre sayısı

print(str(image.size))#renkli resmin kaç piksel olduğu
print(str(image2.size))#siyah beyaz resmin kaç piksel olduğu

#resimleri toplarken veri tipleri aynı olmak zorunda
print(image.dtype)#data tipini verir
print(image2.dtype)

ROI = image[30:200, 150:265]#resimin kırpılacak koordinatları
ROI2 = image[60:230, 270:385] = ROI#üzerine yapıştırır.
#cv2.imshow('roi', ROI)

r, g, b = cv2.split(image)#renkleri ayırıyor
image = cv2.merge((r, g, b))#renkerlin üzerinde düzenleme yaptıktan sonra birleştirmeye yarar.
#blue = image[:,:,0]#mavi bileşenine ulaştık
image[:,:,0] = 255 #resimdeki mavi renkli pikselleri sıfırladı

cv2.imshow('Benedict', image)
cv2.imshow('roi2', ROI2)
cv2.waitKey(0)
cv2.destroyAllWindows()