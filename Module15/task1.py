import cv2
import numpy as np

photo = np.ones((400, 400, 3), dtype=np.uint8) * 0

# Рисуем окружность в центре изображения
center_x = photo.shape[1] // 2
center_y = photo.shape[0] // 2
radius = 100
cv2.circle(photo, (center_x, center_y), radius, (255, 255, 255), thickness=3)

# Рисуем внешнюю границу буквы "U"
cv2.line(photo, (center_x - 50, center_y - 50), (center_x - 50, center_y + 50), (255, 255, 255), thickness=15)
cv2.line(photo, (center_x + 50, center_y - 50), (center_x + 50, center_y + 50), (255, 255, 255), thickness=15)
cv2.ellipse(photo, (center_x, center_y + 50), (50, 30), 0, 0, 180, (255, 255, 255), thickness=15)

# Рисуем внутреннюю границу буквы "U" чтобы создать пустое пространство
cv2.line(photo, (center_x - 35, center_y - 50), (center_x - 35, center_y + 35), (0, 0, 0), thickness=10)
cv2.line(photo, (center_x + 35, center_y - 50), (center_x + 35, center_y + 35), (0, 0, 0), thickness=10)
cv2.ellipse(photo, (center_x, center_y + 50), (35, 20), 0, 0, 180, (0, 0, 0), thickness=10)

cv2.imshow("Photo", photo)
cv2.waitKey(0)
cv2.destroyAllWindows()