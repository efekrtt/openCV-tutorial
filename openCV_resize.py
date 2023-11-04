import cv2

# Görüntüyü yükle
image = cv2.imread('a.png')

# Görüntünün boyutlarını yazdır
print(image.shape)

# Görüntüyü yeniden boyutlandır
resized_image = cv2.resize(image, (480, 480))

# Yeniden boyutlandırılmış görüntüyü kaydet
cv2.imwrite('resized_img.png', resized_image)

cv2.imshow('resized', resized_image)

# Bir tuşa basınca kapansın
cv2.waitKey(0)
cv2.destroyAllWindows()
