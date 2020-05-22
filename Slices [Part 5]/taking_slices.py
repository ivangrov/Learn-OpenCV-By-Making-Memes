import cv2
import numpy as np

vc = cv2.VideoCapture(0)

while cv2.waitKey(1) < 0:

    hasFrame, frame = vc.read()
    frame = frame[ 80:-80, 90:-135]

    height, width, depth = frame.shape


    frame[:50] = np.array([0,0,0])
    frame[-50:height] = np.array([0,0,0])


    frame[100:-100,100:-100, 0] = 0
    frame[100:-100, 100:-100, 2] = 0




    cv2.imshow('window', frame)


answer = input("Do you wanna save your meme?")

if answer.lower() == "yes":

    name = input("Name your meme: ") + ".jpg"
    cv2.imwrite(name, frame)
