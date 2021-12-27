import mouse
import keyboard

while True:
    try:
        if keyboard.is_pressed('ctrl+shift+i'):
            mouse.move(641, 488, duration= 0.1)
            mouse.press(button='left')
            print("Holding  click")
    except:
        break