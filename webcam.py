import cv2

captura = cv2.VideoCapture(0)
count = 0

while(captura.isOpened()):
    count = count + 1
    ret, frame = captura.read()

    if ret == True:
        print(frame)

        cv2.imshow('video',frame)
        if cv2.waitKey(1) & 0xFF == ord('e'):
            break
print(count)
captura.release()
cv2.destroyAllWindows()