import os
import socket
from clear import clear
from fastfech import fastfetch, Logo

def pwd():
    print(os.getcwd())

def main():

    Logo()

    print("\nWelcome to LightOS! run 'help' for a list of commands.\n")

    while True:
        cmd = input(f"\n\n{os.getlogin()}@{socket.gethostname()}/LightOS> ")

        if cmd == "help":
            clear()
            print("\n\nWelcome to the help menu! Here you'll find a list of commands you can use.")
            print("\n'clear' to clear the screen")
            print("'fastfetch' for system info")
            print("'echo' to echo a string")
            print("'pwd' to print current directory")
            
        elif cmd == "clear":
            clear()

        elif cmd == "fastfetch":
            fastfetch()

        elif cmd == "echo":
            echoTx = input("> ")
            print(echoTx)

        elif cmd == "pwd":
            pwd()

        else:
            print(f"Error: {cmd}: Unknown command")
