import sys
import tkinter as tk
from tkinter import font
from PIL import ImageTk, Image
import json
import subprocess
import threading

import numpy as np
import time
import json
import cv2
from cvzone.HandTrackingModule import HandDetector
import pyttsx3


class Application(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.pack()
        self.menu_page = MenuPage(self)
        self.master.configure(background='#57C4E5')
        self.menu_page.pack()
        self.defaultFont = font.nametofont("TkDefaultFont")
        self.defaultFont.configure(family="Arial",
                                   size=19,
                                   weight=font.BOLD)

    def switch_to_main(self):
        self.menu_page.pack_forget()
        self.main_page = MainPage(self)
        self.main_page.pack()

    def switch_to_menu(self):
        self.main_page.pack_forget()
        self.main_page.remove_image()
        MainPage.readFile(self)
        self.menu_page.pack()


class MenuPage(tk.Frame):
    def __init__(self, master=None):
        super().__init__(master)
        self.configure(background='#57C4E5')
        self.pack()
        self.create_widgets()

    def create_widgets(self):
        self.welcome = tk.Label(self, bg="#57C4E5")
        self.welcome["text"] = "Welcome to Gesture Speak!\nCommunication made easy."
        self.welcome.grid(row=0, column=0, columnspan=2, pady=50)

        self.startBtn = tk.Button(self, bg='#011627', fg='#FFFFFF')
        self.startBtn["text"] = "Start"
        self.startBtn["command"] = self.start
        self.startBtn.grid(row=1, column=0)

        self.quit_label = tk.Label(self, bg="red")
        self.quit_label["text"] = "While in the camera, press 'Q' to quit!"
        self.quit_label.grid(row=3, column=0, columnspan=2)


        self.commandsBtn = tk.Button(self, bg='#011627', fg='#FFFFFF')
        self.commandsBtn["text"] = "Commands"
        self.commandsBtn["command"] = self.master.switch_to_main
        self.commandsBtn.grid(row=1, column=1)

        self.quit = tk.Button(self, text="QUIT", fg="red", bg='#011627',
                              command=root.destroy)
        self.quit.grid(row=2, column=0, columnspan=2, pady=50)

    def start(self):
        start_thread()


class MainPage(tk.Frame):

    def __init__(self, master=None):
        super().__init__(master)
        self.page_1 = ""
        self.page_2 = ""
        self.indexVal1 = ""
        self.middleVal1 = ""
        self.ringVal1 = ""
        self.pinkyVal1 = ""

        self.indexVal2 = ""
        self.middleVal2 = ""
        self.ringVal2 = ""
        self.pinkyVal2 = ""

        self.readFile()

        self.create_widgets()
        self.lf = Image.open("lefthand.png")
        self.left_hand = ImageTk.PhotoImage(self.lf)
        self.image_label = tk.Label(image=self.left_hand, bg="#57C4E5")
        self.image_label.image = self.left_hand
        self.image_label.pack(side="bottom")

    def create_widgets(self):
        self.tfont = tk.font.Font(size=14)

        self.back = tk.Button(self)
        self.back["text"] = "Go back."
        self.back["command"] = self.master.switch_to_menu
        self.back.grid(row=0, column=2)

        self.save = tk.Button(self)
        self.save["text"] = "Save."
        self.save["command"] = self.saveToFile
        self.save.grid(row=2, column=2)

        self.page1_label = tk.Label(self)
        self.page1_label["text"] = "Page one"
        self.page1_label.grid(row=0, column=1)

        self.page2_label = tk.Label(self)
        self.page2_label["text"] = "Page two"
        self.page2_label.grid(row=0, column=3)

        self.switch_label = tk.Label(self)
        self.switch_label["text"] = "Next page"
        self.switch_label.place(relx=0.5, rely=0.75, anchor="center")

        self.one_label = tk.Label(self)
        self.one_label["text"] = "1"
        self.one_label.grid(row=1, column=0)

        self.two_label = tk.Label(self)
        self.two_label["text"] = "2"
        self.two_label.grid(row=2, column=0)

        self.three_label = tk.Label(self)
        self.three_label["text"] = "3"
        self.three_label.grid(row=3, column=0)

        self.fourth_label = tk.Label(self)
        self.fourth_label["text"] = "4"
        self.fourth_label.grid(row=4, column=0)

        self.index_entry = tk.Text(self, width=20, height=3, font=self.tfont)
        self.index_entry.insert("end", self.indexVal1)
        self.index_entry.grid(row=1, column=1, padx=20, pady=5)

        self.middle_entry = tk.Text(self, width=20, height=3, font=self.tfont)
        self.middle_entry.insert("end", self.middleVal1)
        self.middle_entry.grid(row=2, column=1, padx=20, pady=5)

        self.ring_entry = tk.Text(self, width=20, height=3, font=self.tfont)
        self.ring_entry.insert("end", self.ringVal1)
        self.ring_entry.grid(row=3, column=1, padx=20, pady=5)

        self.pinky_entry = tk.Text(self, width=20, height=3, font=self.tfont)
        self.pinky_entry.insert("end", self.pinkyVal1)
        self.pinky_entry.grid(row=4, column=1, padx=20, pady=5)

        self.index_entry2 = tk.Text(self, width=20, height=3, font=self.tfont)
        self.index_entry2.insert("end", self.indexVal2)
        self.index_entry2.grid(row=1, column=3, padx=20, pady=5)

        self.middle_entry2 = tk.Text(self, width=20, height=3, font=self.tfont)
        self.middle_entry2.insert("end", self.middleVal2)
        self.middle_entry2.grid(row=2, column=3, padx=20, pady=5)

        self.ring_entry2 = tk.Text(self, width=20, height=3, font=self.tfont)
        self.ring_entry2.insert("end", self.ringVal2)
        self.ring_entry2.grid(row=3, column=3, padx=20, pady=5)

        self.pinky_entry2 = tk.Text(self, width=20, height=3, font=self.tfont)
        self.pinky_entry2.insert("end", self.pinkyVal2)
        self.pinky_entry2.grid(row=4, column=3, padx=20, pady=5)

    def remove_image(self):
        self.image_label.destroy()

    def readFile(self):
        with open("data.json") as f:
            data = json.load(f)

        page_1 = data["pages"][0]
        page_2 = data["pages"][1]
        self.indexVal1 = (f"{page_1['key_1']}")
        self.middleVal1 = (f"{page_1['key_2']}")
        self.ringVal1 = (f"{page_1['key_3']}")
        self.pinkyVal1 = (f"{page_1['key_4']}")

        self.indexVal2 = (f"{page_2['key_1']}")
        self.middleVal2 = (f"{page_2['key_2']}")
        self.ringVal2 = (f"{page_2['key_3']}")
        self.pinkyVal2 = (f"{page_2['key_4']}")

    def saveToFile(self):
        with open("data.json") as f:
            data = json.load(f)

        indexVal1 = self.index_entry.get("1.0", "end")
        middleVal1 = self.middle_entry.get("1.0", "end")
        ringVal1 = self.ring_entry.get("1.0", "end")
        pinkyVal1 = self.pinky_entry.get("1.0", "end")

        indexVal2 = self.index_entry2.get("1.0", "end")
        middleVal2 = self.middle_entry2.get("1.0", "end")
        ringVal2 = self.ring_entry2.get("1.0", "end")
        pinkyVal2 = self.pinky_entry2.get("1.0", "end")

        with open("data.json", "w") as f:
            data["pages"][0]["key_1"] = indexVal1
            data["pages"][0]["key_2"] = middleVal1
            data["pages"][0]["key_3"] = ringVal1
            data["pages"][0]["key_4"] = pinkyVal1

            data["pages"][1]["key_1"] = indexVal2
            data["pages"][1]["key_2"] = middleVal2
            data["pages"][1]["key_3"] = ringVal2
            data["pages"][1]["key_4"] = pinkyVal2

            json.dump(data, f)




def camera():

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
    print(indexVal2, middleVal2, ringVal2, pinkyVal2)

    currentPage = 1

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
    delay = 2.1

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
                    prevP_position = None

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
                            engine.say(indexVal1)  #
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

        key = cv2.waitKey(1) & 0xFF
        if key == ord("q"):
            break

    cap.release()
    cv2.destroyAllWindows()

def draw_button(frame, text, x, y, w, h, color=(0, 255, 0), thickness=2):
    cv2.rectangle(frame, (x, y), (x + w, y + h), color, thickness)
    font = cv2.FONT_HERSHEY_SIMPLEX
    text_size = cv2.getTextSize(text, font, 1, 2)[0]
    text_x = x + w // 2 - text_size[0] // 2
    text_y = y + h // 2 - text_size[1] // 2
    cv2.putText(frame, text, (text_x, text_y), font, 1, (255, 255, 255), 2)

def start_thread():
    # Create the thread and run it
    thread = threading.Thread(target=camera())
    thread.start()

if __name__ == "__main__":
    root = tk.Tk()
    root.geometry("1280x720")
    root.title("Gesture Speech")
    root.resizable(False, False)
    app = Application(master=root)
    app.mainloop()
