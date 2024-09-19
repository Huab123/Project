import webbrowser
import pyautogui
import time


def autoTrain(typeTrain):
    webbrowser.open('https://www.torn.com/gym.php', new=0, autoraise=True)
    time.sleep(5)
    pyautogui.leftClick(typeTrain[0], typeTrain[1], duration=0.1)  # Clicks chosen Train
    time.sleep(1)                                                  # You should set single tap train to use 100 Energy
    pyautogui.hotkey('ctrl', 'w')


def autoCrime():
    done = 0
    webbrowser.open('https://www.torn.com/crimes.php#', new=0, autoraise=True)
    time.sleep(5)
    while done < 3:
        if done == 0:
            pyautogui.leftClick(1250, 675, duration=0.1)  # Clicks to Armed Robberies
            time.sleep(2)
            pyautogui.leftClick(1400, 750, duration=0.1)  # Clicks to Thorough Armored Car
        elif done < 3:
            time.sleep(3)
            pyautogui.leftClick(675, 475, duration=0.1)  # Clicks Try Again
        done += 1
    time.sleep(1)
    pyautogui.hotkey('ctrl', 'w')


def typeGym():
    strength = [775, 475]
    defense = [1025, 475]
    speed = [1275, 475]
    dexterity = [1515, 475]
    while True:
        try:
            typeTrain = int(input("Type of Training Strength(1), Defense(2), Speed(3), Dexterity(4): "))
            if 4 >= typeTrain > 0:
                break
            else:
                print("Must enter value 1-4")
        except ValueError:
            print("Must enter value 1-4")
    if typeTrain == 1:
        return strength
    elif typeTrain == 2:
        return defense
    elif typeTrain == 3:
        return speed
    elif typeTrain == 4:
        return dexterity


def nerveTimer():
    while True:
        try:
            nerveAmt = int(input("Nerve: "))  # User input amount of Nerve
            if nerveAmt > 0:
                break
            else:
                print("You must enter a number greater than 0")
        except ValueError:
            print("You must enter a valid number")
    return nerveAmt * 5


def runScript():
    typeTrain = typeGym()
    nerveTime = nerveTimer()
    minute = 0
    energyTime = 0
    while True:
        print(minute)
        if energyTime % 300 == 0:  # Every 5 Hours auto trains
            autoTrain(typeTrain)
            energyTime = 0
        if minute % nerveTime == 0:  # Every (Nerve amount * 5) minutes auto crimes
            autoCrime()
            minute = 0
        minute += 5
        energyTime += 5
        time.sleep(300)  # Iterates every 5 minutes


if __name__ == '__main__':
    runScript()
