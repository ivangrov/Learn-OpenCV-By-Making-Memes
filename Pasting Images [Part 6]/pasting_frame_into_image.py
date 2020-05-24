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
        print(mouse_x, mouse_y)


    elif event == cv2.EVENT_LBUTTONDOWN:

        print(mouse_x, mouse_y)
        # print(image[mouse_y, mouse_x])


cv2.namedWindow("window", cv2.WINDOW_NORMAL)
cv2.setMouseCallback("window", mouse_listener)



frame = frame[ 105:-60, 100:-135]
height, width, depth = frame.shape

print('FRAME SHAPE: ', width, height)

memeImage = cv2.imread('stonks.jpg')

memeImage = cv2.resize(memeImage, (2000, 1000))
memeHeight, memeWidth, memeDepth = memeImage.shape

origMemeImage = memeImage.copy()


indentY = 150
indentX = 50

print("MEME SHAPE: ", memeWidth, memeHeight)

while cv2.waitKey(1) < 0:

    hasFrame, frame = vc.read()
    frame = frame[ 105:-60, 100:-135]

    memeImage = origMemeImage.copy()
    memeImage[indentY: indentY + height, indentX: indentX + width ] = frame



    cv2.imshow('window',memeImage)


#answer = input("Do you wanna save your meme?")

#if answer.lower() == "yes":

name = input("Name your meme: ") + ".jpg"
cv2.imwrite(name, memeImage)
