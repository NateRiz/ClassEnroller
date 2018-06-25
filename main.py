from file_manager import get_settings
import I
from enroll import Enroll
def main():
    i = I.I() 
    settings = get_settings()
    enroller = Enroll(i)
    enroller.main_loop()


if __name__ == "__main__":
    main()
