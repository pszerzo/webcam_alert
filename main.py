import glob
import os

import cv2
import time
import emailing

video = cv2.VideoCapture(1)
time.sleep(1)
first_frame = None
status_list = []

def cleaning():
    images = glob.glob("images/*png")
    for img in images:
        os.remove(img)

count = 0
while True:
    status = 0
    check, frame = video.read()
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    gray_frame_gau = cv2.GaussianBlur(gray_frame, (21, 21), 0) #amount of blurness
    if first_frame is None:
        first_frame = gray_frame_gau

    delta_frame = cv2.absdiff(first_frame, gray_frame_gau)
    thresh_frame = cv2.threshold(delta_frame, 45, 255, cv2.THRESH_BINARY)[1]
    #if the value is 30 then it got 255 value
    dil_frame = cv2.dilate(thresh_frame, None, iterations=2)

    contours, check = cv2.findContours(dil_frame, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    #filter out fake object and keep real objects

    for contour in contours:
        if cv2.contourArea(contour) < 5000:
            continue
        x, y, w, h = cv2.boundingRect(contour)
        rectangle = cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 3)
        if rectangle.any():
            status = 1
            cv2.imwrite(f"images/{count}.png", frame)
            count += 1
            all_images = glob.glob("images/*.png")
            index = int(len(all_images)/2)
            image_object = all_images[index]

    status_list.append(status)
    status_list = status_list[-2:] #last two elements

    if status_list[0] == 1 and status_list[1] == 0:
        emailing.send_email(image_object)
        cleaning()

    cv2.imshow("My video", frame)

    key = cv2.waitKey(1)

    if key == ord("q"):
        break

video.release()