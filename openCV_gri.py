import cv2

# Görüntüyü yükle
image = cv2.imread('a.png')

# Gri tonlamaya dönüştür
gray_image = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Gri tonlama görüntüsünü göster
cv2.imshow('Gri Tonlama', gray_image)

# Gri resmi kaydediyoruz.
cv2.imwrite('gray_img.png', gray_image)

# Bir tuşa basıldığında kapa
cv2.waitKey(0)
cv2.destroyAllWindows()
