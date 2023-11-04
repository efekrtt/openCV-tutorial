import cv2

# Görüntüyü yükle
image = cv2.imread('a.png')

# Görüntüyü göster
cv2.imshow('A', image)

# Pencereyi kapat
cv2.waitKey(0)
cv2.destroyAllWindows()