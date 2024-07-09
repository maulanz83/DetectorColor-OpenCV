import cv2
from PIL import Image
from DetectorColor import get_limit


yellow = [0, 255, 255]# yellow in BGR
cap = cv2.VideoCapture(0)  # Ganti 0 dengan jalur ke video file jika Anda menggunakan file video

while True:
    ret, frame = cap.read()

    hsvImages =  cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    lowerLimit, upperLimit = get_limit(color=yellow)

    mask = cv2.inRange(hsvImages, lowerLimit, upperLimit)
    
    mask_ = Image.fromarray(mask)# convert to PIL image

    bbox = mask_.getbbox()# get bounding box of the mask

    if bbox is not None:
        x1, y1, x2, y2 = bbox
        cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 5)
    
    cv2.imshow('frame', frame)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()

cv2.destroyAllWindows()
