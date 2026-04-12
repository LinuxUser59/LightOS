import time
import random
from prompt import main
from clear import clear

DEFAULT_COLOUR = '\033[0m'
LIGHT_GREEN = '\033[92m'
RED = '\033[91m'
GREY = '\033[90m'
ORANGE = '\033[38;5;214m'

def Boot():
    clear()
    initramfs = random.randint(1, 21)
    cpu1 = random.randint(1, 21)
    cpu2 = random.randint(1, 21)
    assign = random.randint(1, 21)

    if initramfs == 20:
        time.sleep(random.randint(1, 5))
        print(f"{DEFAULT_COLOUR}[{RED}  FAIL  {DEFAULT_COLOUR}] {GREY}Failed{DEFAULT_COLOUR} Loading Initramfs...")
        print(f"{ORANGE}    Error loading initramfs, aborting...")
        exit()

    else:
        time.sleep(random.randint(1, 5))
        print(f"{DEFAULT_COLOUR}[{LIGHT_GREEN}  OK  {DEFAULT_COLOUR}] {GREY}Starting{DEFAULT_COLOUR} Loading Initramfs...")
        time.sleep(0.600)
        clear()
        print(f"{DEFAULT_COLOUR}[{LIGHT_GREEN}  OK  {DEFAULT_COLOUR}] {GREY}Finished{DEFAULT_COLOUR} Loading Initramfs...")

        if cpu1 == 20:
            time.sleep(random.randint(1, 5))
            print(f"{DEFAULT_COLOUR}[{RED}  FAIL  {DEFAULT_COLOUR}] {GREY}Failed{DEFAULT_COLOUR} Initialising CPU core 1...")
            print(f"{ORANGE}    Error initialising CPU core 1, aborting...")
            exit()

        else:
            time.sleep(random.randint(1, 5))
            print(f"{DEFAULT_COLOUR}[{LIGHT_GREEN}  OK  {DEFAULT_COLOUR}] {GREY}Finished{DEFAULT_COLOUR} Initialising CPU core 1...")

            if cpu2 == 20:
                time.sleep(random.randint(0, 3))
                print(f"{DEFAULT_COLOUR}[{RED}  FAIL  {DEFAULT_COLOUR}] {GREY}Failed{DEFAULT_COLOUR} Initialising CPU core 2...")
                print(f"{ORANGE}    Error initialising CPU core 2, aborting...")
                exit()

            else:
                time.sleep(random.randint(3, 5))
                print(f"{DEFAULT_COLOUR}[{LIGHT_GREEN}  OK  {DEFAULT_COLOUR}] {GREY}Finished{DEFAULT_COLOUR} Initialising CPU core 2...")

            if assign == 20:
                time.sleep(random.randint(1, 2))
                print(f"{DEFAULT_COLOUR}[{RED}  FAIL  {DEFAULT_COLOUR}] {GREY}Failed{DEFAULT_COLOUR} Assigning disk manager...")
                print(f"{ORANGE}    Error assigning disk manager, aborting...")
                exit()

            else:
                time.sleep(random.randint(4, 5))
                print(f"{DEFAULT_COLOUR}[{LIGHT_GREEN}  OK  {DEFAULT_COLOUR}] {GREY}Finished{DEFAULT_COLOUR} Assigning disk manager...")
                time.sleep(3)
                print(f"{DEFAULT_COLOUR}[{LIGHT_GREEN}  OK  {DEFAULT_COLOUR}] {GREY}Finishing{DEFAULT_COLOUR} Booting system...")
                time.sleep(3)
                clear()


Boot()

main()