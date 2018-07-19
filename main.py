from file_manager import get_settings
from enroll import Enroll
from notify import Notify
import I
def main():
    settings = get_settings()
    if settings:
        notify = Notify(settings["to"],settings["username"], settings["password"], settings["phone"]
        if len(settings["course"]) == 2:
            enroller = Enroll(notify, settings["course"][0], settings["course"][1])
        elif len(settingsi["course"]) ==3:
            enroller = Enroll(notify, settings["course"][0], settings["course"][1], settings["course"][2])
        else:
            print("Unsupported aamount of arguments")
            return
        enroller.main_loop()
    else:
        print("Error parsing Settings.cfg")


if __name__ == "__main__":
    main()
    I.close_driver()
