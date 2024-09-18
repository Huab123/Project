import webbrowser
import pyautogui
import time


def autoTrain():
    webbrowser.open('https://www.torn.com/gym.php', new=0, autoraise=True)
    time.sleep(5)
    pyautogui.leftClick(1275, 475, duration=0.1)
    time.sleep(1)
    pyautogui.hotkey('ctrl', 'w')


def autoCrime():
    done = 0
    webbrowser.open('https://www.torn.com/crimes.php#', new=0, autoraise=True)
    time.sleep(5)
    while done < 3:
        if done == 0:
            pyautogui.leftClick(1250, 675, duration=0.1)
            time.sleep(2)
            pyautogui.leftClick(1400, 750, duration=0.1)
        elif done < 3:
            time.sleep(3)
            pyautogui.leftClick(675, 475, duration=0.1)
        done += 1
    time.sleep(1)
    pyautogui.hotkey('ctrl', 'w')


def nerveTimer():
    while True:
        try:
            nerveAmt = int(input("Nerve: "))
            break
        except ValueError:
            print("You must enter a valid number")
    return nerveAmt * 5


def runScript():
    nerveTime = nerveTimer()
    minute = 0
    energyTime = 0
    while True:
        print(minute)
        if energyTime % 300 == 0:
            autoTrain()
            energyTime = 0
        if minute % nerveTime == 0:
            autoCrime()
            minute = 0
        minute += 5
        energyTime += 5
        time.sleep(300)


if __name__ == '__main__':
    runScript()

