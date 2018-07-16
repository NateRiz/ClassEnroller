from file_manager import get_settings
from enroll import Enroll

def main():
    settings = get_settings()
    if settings != "":
        enroller = Enroll(settings[0], settings[1])
        enroller.main_loop()
    else:
        print("Error parsing Settings.cfg")

if __name__ == "__main__":
    main()
