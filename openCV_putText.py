import cv2

# Görüntüyü yükle
image = cv2.imread('a.png')

# Dikdörtgen çizmek için koordinatlar
x, y, width, height = 100, 100, 200, 200

# Dikdörtgeni çiz
cv2.rectangle(image, (x, y), (x + width, y + height), (0, 255, 0), 2)

# Metni ekleme
text = "ATLAS"
cv2.putText(image, text, (x, y), cv2.FONT_HERSHEY_PLAIN, 2, (0, 0, 255), 2, cv2.LINE_AA)

# Dikdörtgeni içeren görüntüyü göster
cv2.imshow('Dikdörtgen', image)

# Gri resmi kaydediyoruz.
cv2.imwrite('Atlasli_dikdortgenli.png', image)

cv2.waitKey(0)
cv2.destroyAllWindows()
