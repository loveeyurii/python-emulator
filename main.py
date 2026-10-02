# main.py
from phone import Phone


def main():
    phone = Phone(name="PixelSim")
    print("Welcome to PixelSim Phone Emulator")
    print("Type 'help' for commands.")
    phone.run()


if __name__ == "__main__":
    main()
