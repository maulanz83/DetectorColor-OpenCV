import numpy as np
import cv2

def get_limit(color):
    
    c = np.uint8([[color]])
    hscV = cv2.cvtColor(c, cv2.COLOR_BGR2HSV)

    lowerLimit = hscV[0][0][0] - 10, 100, 100
    upperLimit = hscV[0][0][0] + 10, 255, 255

    lowerLimit = np.array(lowerLimit, dtype=np.uint8)
    upperLimit = np.array(upperLimit, dtype=np.uint8)

    return lowerLimit, upperLimit
