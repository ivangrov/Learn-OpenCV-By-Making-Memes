import numpy as np
import cv2



vc = cv2.VideoCapture(0)

while cv2.waitKey(1) < 0:

    hasFrame, frame = vc.read()


    frame = frame[ 100:-100, 130:-150]



    #frame = cv2.resize(frame, (100, 100))

    height, width, depth = frame.shape


    for h in range(height):
        for w in range(width):
            for c in range(depth):

                frame[h, w, c ] = 135 - frame[h, w, c]



    frame = cv2.resize(frame, (500, 500), interpolation=cv2.INTER_NEAREST)

    cv2.putText(frame, "WHEN YOU MAKE MEMES IN PYTHON", (20,50), cv2.FONT_HERSHEY_SIMPLEX, 1.2, (0, 0, 0), 8)
    cv2.putText(frame, "WHEN YOU MAKE MEMES IN PYTHON", (20, 50), cv2.FONT_HERSHEY_SIMPLEX, 1.2, (255, 255, 255), 4)

    cv2.putText(frame, "IN PYTHON", (160, 475), cv2.FONT_HERSHEY_SIMPLEX, 1.2, (0, 0, 0), 8)
    cv2.putText(frame, "IN PYTHON", (160, 475), cv2.FONT_HERSHEY_SIMPLEX, 1.2, (255, 255, 255), 4)

    cv2.imshow("window", frame)


answer = input("Do you wanna save your meme?")

if answer.lower() == "yes":

    name = input("Name your meme: ") + ".jpg"
    cv2.imwrite(name, frame)



