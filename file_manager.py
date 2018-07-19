from datetime import datetime
import os

def get_settings():
    path = os.path.join(os.getcwd(), "settings.cfg")
    if not os.path.exists(path):
        log("Could not find settings.cfg.")
        create_settings()
        return []
    with open(path, "r") as file:
        settings = {"to":"", "username":"", "password":"", "phone":""}
        for line in file:
            line = line.strip().replace(" ","")
            if line == "" or line[0] == "#" or line.split(":")<=1:
                continue
            line = line.split(":")
            if line[0] == "To_Email":
                settings["to"] = line[1]
            elif line[0] == "From_Email_Password":
                settings["password" = line[1]
            elif line[0] == "From_Email_Username":
                settings["username"] = line[1]
            elif line[0] == "Phone":
                settings["phone"] = line[1]
            else:
                settings["course"] = line.split(":")
            try:
                settings = [int(s) if s.isdigit() else s for s in settings]
            except ValueError:
                log("Error Parsing Settings: Non-integer found.")
                return {}
        return settings
    return {}


def create_settings():
    with open("settings.cfg","w") as settings:
        template = """#[Class Enroller]\n#Template:$DEPT:$COURSE_NO[:$SECTION]\n#Example: CSE:231\n#Example: CSE:231:4\n#Optional Notifications - GMAIL SUPPORT ONLY:\nTo_Email:email_to_notify@mail.com\nFrom_Email_Username:email_sender@gmail.com\nFrom_Email_Password:password\nPhone:2223334444"""
        settings.write(template)
        log("Created settings.cfg file.")

def log(message):
    path = os.path.join(os.getcwd(), "log.txt")
    if not os.path.exists(path):
        open("log.txt","w").close()
    with open("log.txt","a") as log:
        adjusted_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        log.write("[{}] {}\n".format(adjusted_date, message))
