import cv2

cap = cv2.VideoCapture(0)


def __webcam__():
    while True:
        # Capture frame-by-frame
        ret, img = cap.read()

        # operations on the frame
        gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

        cv2.imshow('OCR running', img)

        if cv2.waitKey(1) == ord('q') or cv2.waitKey(1) == 27:
            break

__webcam__()

cap.release()
cv2.destroyAllWindows()

