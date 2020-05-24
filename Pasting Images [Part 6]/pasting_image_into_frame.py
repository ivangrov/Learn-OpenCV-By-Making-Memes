import cv2
import numpy as np

vc = cv2.VideoCapture(0)
hasFrame, frame = vc.read()


def mouse_listener(event, x, y, flags, param):
    global mouse_x, mouse_y, point_1, point_2, indentX, indentY

    if event == cv2.EVENT_MOUSEMOVE:
        mouse_x = x
        mouse_y = y
        indentX = x
        indentY = y

    elif event == cv2.EVENT_LBUTTONDOWN:

        print(mouse_x, mouse_y)
        # print(image[mouse_y, mouse_x])


cv2.namedWindow("window", cv2.WINDOW_NORMAL)
cv2.resizeWindow("window",1000, 1000)
cv2.setMouseCallback("window", mouse_listener)

height, width, depth = frame.shape


memeImage = cv2.imread('stonks.jpg')

memeImage = cv2.resize(memeImage, (50, 50))

memeHeight, memeWidth, memeDepth = memeImage.shape


indentX = 100
indentY = 200

while cv2.waitKey(1) < 0:

    hasFrame, frame = vc.read()
    frame = frame[ 105:-60, 90:-135]


    frame[indentY : indentY + memeHeight, indentX: indentX + memeWidth] = memeImage




    cv2.imshow('window', frame)


answer = input("Do you wanna save your meme?")

if answer.lower() == "yes":

    name = input("Name your meme: ") + ".jpg"
    cv2.imwrite(name, frame)
