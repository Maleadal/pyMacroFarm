import pyautogui as pt
import time
import keyboard
import random
import cv2
import mouse


def change_weather():
    keyboard.release('a')
    keyboard.release('d')
    release()
    keyboard.press_and_release('4')
    time.sleep(0.5)
    mouse.right_click()
    time.sleep(0.7)
    click(1515, 435)
    time.sleep(0.5)
    keyboard.press_and_release('2')
    press()


def click(x, y):
    mouse.move(x, y)
    time.sleep(0.2)
    mouse.click(button='left')


def press():
    mouse.press(button='left')


def release():
    mouse.release(button='left')


def walk(direction):
    if direction == "right":
        if keyboard.is_pressed('d'):
            return
        keyboard.release('a')
        keyboard.press('d')
    elif direction == "left":
        if keyboard.is_pressed('a'):
            return
        keyboard.release('d')
        keyboard.press('a')


isMoved = False
sky = (24, 24, 30)
rain = (165, 167, 255)
time.sleep(1)
direction = "right";
if pt.locateOnScreen("images/pause.png", region=(1240, 300, 1640 - 1240, 340 - 300), confidence=0.7) is not None:
    click(1432, 322)
    time.sleep(0.5)
    direction = "right"
    press()
while not keyboard.is_pressed('q'):
    walk(direction)
    if pt.locateOnScreen("images/pause.png", region=(1240, 300, 1640 - 1240, 340 - 300), confidence=0.7) is not None:
        print("Bot stopped. \nReason: Game Paused")
        keyboard.release('d')
        keyboard.release('a')
        release()
        break
    elif pt.pixel(1359, 75) == sky and not isMoved:
        print("Move down mouse")
        release()
        mouse.drag(mouse.get_position()[0], mouse.get_position()[1], mouse.get_position()[0],
                   mouse.get_position()[1] + 20, duration=0.1)
        press()
        isMoved = True
    elif pt.pixel(1755, 569) == rain or pt.pixel(1036, 661) == rain:
        print("It's raining, changing the weather now!")
        change_weather()
        time.sleep(5)
    elif pt.pixel(1036, 661) == sky:
        if(isMoved):
            isMoved = False
        direction = "right"
        print("It's the sky from the left, GO RIGHT NOW!")
    elif pt.pixel(1755, 569) == sky:
        direction = "left"
        print("It's the sky from the right, GO LEFT NOW!")

    time.sleep(0.5)
