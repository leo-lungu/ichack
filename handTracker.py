import numpy as np
import time
import json
import cv2
from cvzone.HandTrackingModule import HandDetector
import pyttsx3

currentFinger = None

with open("data.json") as f:
    data = json.load(f)

page_1 = data["pages"][0]
page_2 = data["pages"][1]
indexVal1 = (f"{page_1['key_1']}")
middleVal1 = (f"{page_1['key_2']}")
ringVal1 = (f"{page_1['key_3']}")
pinkyVal1 = (f"{page_1['key_4']}")

indexVal2 = (f"{page_2['key_1']}")
middleVal2 = (f"{page_2['key_2']}")
ringVal2 = (f"{page_2['key_3']}")
pinkyVal2 = (f"{page_2['key_4']}")

print(indexVal1, middleVal1, ringVal1, pinkyVal1)

currentPage = 0

cap = cv2.VideoCapture(0)
detector = HandDetector(detectionCon=0.80, maxHands=2)
prev_position = None
prevI_position = None
prevM_position = None
prevR_position = None
prevP_position = None
PrevPalm_position = None
Stability_Threshold = 5
threshold = 20

prev_detection_time = time.time()
delay = 0.8


def euclidean_distance(p1, p2):
    return np.sqrt((p2[0] - p1[0]) ** 2 + (p2[1] - p1[1]) ** 2)


while True:
    success, img = cap.read()
    hands, img = detector.findHands(img)  # With Draw
    # hands = detector.findHands(img, draw=False) # No Draw
    if hands:
        # Hand 1
        hand1 = hands[0]
        lmList1 = hand1["lmList"]  # List of 21 Landmarks points
        bbox1 = hand1["bbox"]  # Bounding Box info x,y,w,h
        centerPoint1 = hand1["center"]  # center of the hand cx,cy
        handType1 = hand1["type"]  # Hand Type Left or Right
        # print(len(lmList1),lmList1)
        # print(bbox1)

        palm_position = lmList1[0]
        if PrevPalm_position is not None:
            diff = abs(palm_position[0] - PrevPalm_position[0]) + abs(palm_position[1] - PrevPalm_position[1])
            if diff > Stability_Threshold:
                PrevPalm_position = palm_position
                prev_position = None
                prevI_position = None
                prevM_position = None
                prevR_position = None
                prevP_position= None

                continue

        PrevPalm_position = palm_position







        # length, info, img = detector.findDistance(lmList1[8], lmList1[12], img) # with draw
        # length, info = detector.findDistance(lmList1[8], lmList1[12])  # no draw
        thumb_position = lmList1[4]
        Start = time.time()
        if currentFinger != "thumb":
            if prev_position is not None:
                diff = euclidean_distance(thumb_position, prev_position)
                if diff > threshold and (time.time() - prev_detection_time) > delay:
                    print("Thumb")

                    prev_position = thumb_position
                    prev_detection_time = time.time()

                    engine = pyttsx3.init()
                    engine.say("Next Page")
                    engine.runAndWait()
                    currentFinger = "thumb"

                    if currentPage == 1:
                        currentPage = 2
                    else:
                        currentPage = 1

            else:
                prev_position = thumb_position
            End = time.time()

        index_position = lmList1[8]
        if currentFinger != "index":
            if prevI_position is not None:
                diff = distance = euclidean_distance(index_position, prevI_position)
                if diff > threshold and (time.time() - prev_detection_time) > delay:
                    print("Index")

                    engine = pyttsx3.init()
                    if currentPage == 1:
                        engine.say(indexVal1)#
                    else:
                        engine.say(indexVal2)
                    engine.runAndWait()
                    prevI_position = index_position
                    prev_detection_time = time.time()
                    currentFinger = "index"
            else:
                prevI_position = index_position

        Middle_position = lmList1[12]
        if currentFinger != "middle":
            if prevM_position is not None:
                diff = distance = euclidean_distance(Middle_position, prevM_position)
                if diff > threshold and (time.time() - prev_detection_time) > delay:
                    print("Middle")
                    prevM_position = Middle_position
                    prev_detection_time = time.time()

                    engine = pyttsx3.init()
                    if currentPage == 1:
                        engine.say(middleVal1)  #
                    else:
                        engine.say(middleVal2)
                    engine.runAndWait()
                    currentFinger = "middle"
            else:
                prevM_position = Middle_position

        Ring_position = lmList1[16]
        if currentFinger != "ring":
            if prevR_position is not None:
                diff = distance = euclidean_distance(Ring_position, prevR_position)
                if diff > threshold and (time.time() - prev_detection_time) > delay:
                    print("Ring")
                    prevR_position = Ring_position
                    prev_detection_time = time.time()

                    engine = pyttsx3.init()
                    if currentPage == 1:
                        engine.say(ringVal1)  #
                    else:
                        engine.say(ringVal2)
                    engine.runAndWait()
                    currentFinger = "ring"
            else:
                prevR_position = Ring_position

        Pinky_position = lmList1[20]
        if currentFinger != "pinky":
            if prevP_position is not None:
                diff = distance = euclidean_distance(Pinky_position, prevP_position)
                if diff > threshold and (time.time() - prev_detection_time) > delay:
                    print("Pinky")
                    prevP_position = Pinky_position
                    prev_detection_time = time.time()

                    engine = pyttsx3.init()
                    if currentPage == 1:
                        engine.say(pinkyVal1)  #
                    else:
                        engine.say(pinkyVal2)
                    engine.runAndWait()
                    currentFinger = "pinky"

            else:
                prevP_position = Pinky_position

    cv2.imshow("Image", img)
    cv2.waitKey(1)