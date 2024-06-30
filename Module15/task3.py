import cv2

# Загрузка каскада Хаара для глаз
eye_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_eye.xml')

# Захват видео с первой доступной камеры
cap = cv2.VideoCapture(0)

while True:
    # Захват кадра
    ret, frame = cap.read()
    if not ret:
        break

    # Преобразование в оттенки серого
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # Распознавание глаз
    eyes = eye_cascade.detectMultiScale(gray, scaleFactor=1.3, minNeighbors=5)

    # Обработка каждого обнаруженного глаза
    for (ex, ey, ew, eh) in eyes:
        # Определение границы области глаз
        eye_region = frame[ey:ey+eh, ex:ex+ew]

        # Размытие области глаз
        blurred_eye = cv2.GaussianBlur(eye_region, (25, 25), 0)

        # Замена области глаз на размытую версию
        frame[ey:ey+eh, ex:ex+ew] = blurred_eye

    # Отображение обработанного кадра
    cv2.imshow('Video', frame)

    # Выход из цикла по нажатию клавиши 'q'
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Освобождение ресурсов
cap.release()
cv2.destroyAllWindows()