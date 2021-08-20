import pyautogui as pg
from copy import deepcopy
import time
import random


# Read words
with open('words.txt', 'r') as file:
    words = file.read()
words = words.split('\n')

def get_random_color():
    cords = [(166, 494),
            (219, 492),
            (272, 491),
            (164, 544),
            (220, 546),
            (273, 546),
            (169, 598),
            (219, 599),
            (276, 601),
            (378, 442)]
    return cords[random.randint(0, 9)]


def get_random_animation():
    cords = [(347, 267),
            (344, 407),
            (346, 541),
            (144, 533)]
    return cords[random.randint(0, 3)]


def get_random_word(i):
    global words
    word = list(words[i].strip())
    original_word = deepcopy(''.join(word))
    random.shuffle(word)
    return original_word, ''.join(word)


def create_gif(i):
    # Click on Canvas
    pg.click(1153, 570)
    time.sleep(0.5)

    # Click on BG Color
    pg.click(453, 166)
    time.sleep(0.5)

    # Select random color
    pg.click(get_random_color())
    time.sleep(0.5)

    # Click on add text
    pg.click(30, 388)
    time.sleep(0.5)
    
    # Click on Add Heading
    pg.click(216, 265)
    time.sleep(0.5)

    # Write the jumbled word
    original, a = get_random_word(i)
    pg.typewrite(a)
    time.sleep(0.5)

    # Click on Animate
    pg.click(1212, 163)
    time.sleep(0.5)

    # Select random Animation
    pg.click(get_random_animation())
    time.sleep(0.5)

    # Click on Add heading
    pg.click(1369, 117)
    time.sleep(0.5)

    # Double click
    pg.doubleClick()
    time.sleep(0.5)

    # Write heading
    pg.typewrite(original)
    time.sleep(0.5)

    # Click on Download
    pg.click(1785, 109)
    time.sleep(0.5)

    # Click on drop-drop
    pg.click(1875, 245)
    time.sleep(1)

    # Click on GIF
    pg.click(1687, 457)
    time.sleep(0.5)

    # Click on download
    pg.click(1732, 332)
    time.sleep(7)

    # Click on close
    pg.click(1523, 311)
    time.sleep(0.5)

    # Click on select text area
    pg.click(1160, 565)
    time.sleep(0.5)

    # Click on delete
    pg.click(1893, 168)
    time.sleep(0.5)

    

gifs_to_create = len(words)

# Time to navigate to action window
time.sleep(5)

start = time.time()
for i in range(gifs_to_create):
    create_gif(i)

print("Took {0}s".format(time.time()-start))
print("Create {0} gifs!! Saved to Downloads!! -- Nikhil JSK".format(gifs_to_create))
