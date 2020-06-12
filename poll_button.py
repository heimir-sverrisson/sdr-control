import board
import digitalio
import time

def press_ptt():
    print("Pressing PTT")

def release_ptt():
    print("Releasing PTT")

def main():
    print("Starting")
    button = digitalio.DigitalInOut(board.C0)
    button.direction = digitalio.Direction.INPUT
    ptt = False

    while True:
        if button.value and not ptt:
            press_ptt()
            ptt = True
        if not button.value and ptt:
            release_ptt()
            ptt = False
        time.sleep(0.1)


if __name__ == "__main__":
    main()