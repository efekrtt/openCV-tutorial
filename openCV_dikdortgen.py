import cv2

# Görüntüyü yükle
image = cv2.imread('resized_img.png')

# Dikdörtgen çizmek için koordinatlar
x, y, width, height = 100, 100, 100, 200

# Dikdörtgeni çiz
cv2.rectangle(image, (x, y), (x + width, y + height), (255, 0, 255) , 2) # (255, 0, 255) renk kodu BGR

# dikdortgenli görüntüyü göster
cv2.imshow('dikdortgen', image)

# dikdortgenli görüntüyü kaydediyoruz.
cv2.imwrite('dikdortgenli.png', image)

cv2.waitKey(0)
cv2.destroyAllWindows()
