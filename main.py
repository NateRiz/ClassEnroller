from file_manager import get_settings
from enroll import Enroll
def main():
    settings = get_settings()
    enroller = Enroll()
    enroller.main_loop()


if __name__ == "__main__":
    main()
