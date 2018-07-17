from file_manager import get_settings
from enroll import Enroll

def main():
    settings = get_settings()
    if settings:
        if len(settings) == 2:
            enroller = Enroll(settings[0], settings[1])
        elif len(settings) ==3:
            enroller = Enroll(settings[0], settings[1], settings[2])
        else:
            print("Unsupported aamount of arguments")
            return
        enroller.main_loop()
    else:
        print("Error parsing Settings.cfg")

if __name__ == "__main__":
    main()
