import cv2
import numpy as np

# Загрузка и изменение размера изображения
image = cv2.imread('color_text.jpg')
image = cv2.resize(image, (800, 600))

# Преобразование изображения в оттенки серого
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Применение гауссова размытия
blurred = cv2.GaussianBlur(gray, (9, 9), 0)

# Применение операции Canny к размытому изображению
edges = cv2.Canny(blurred, 100, 200)

# Нахождение контуров на бинаризованном изображении
contours, _ = cv2.findContours(edges, cv2.RETR_LIST, cv2.CHAIN_APPROX_SIMPLE)

# Создание чёрного фона для рисования контуров
black_bg = np.zeros_like(image)

# Окрашивание каждой строки в разные цвета на размытом фоне
colors = [(255, 0, 0), (0, 255, 0), (0, 0, 255)]
for i, contour in enumerate(contours):
    color = colors[i % len(colors)]  # Циклическое использование цветов
    cv2.drawContours(black_bg, [contour], -1, color, cv2.FILLED)

# Отображение результата
cv2.imshow("Processed Image", black_bg)
cv2.waitKey(0)
cv2.destroyAllWindows()