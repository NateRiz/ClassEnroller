from I import I
from datetime import datetime
from time import sleep
class Enroll:
    success_delay = 10 * 60 * 1000
    failure_delay = 45 * 1000 # Milliseconds
    def __init__(self, notify, term, subject, course_number, section, netid, password):
        self.last_run_time = datetime.now()
        self.notify = notify
        self.term = term
        self.subject = subject
        self.course_number = course_number
        self.section = section
        self.netid = netid
        self.pw = password

    def main_loop(self):
        while True:
            self.last_run_time = datetime.now()
            I.go_to_url("https://schedule.msu.edu/")
            I.search_for_course(self.term, self.subject, self.course_number)
            I.check_for_space_in_sections(self.section)
            if I.available_sections:
                print(">",I.available_sections)
                self.notify.send_email(I.available_sections)
                self.notify.send_text(I.available_sections)
                if self.netid and self.pw:
                    I.add_to_planner()
                    I.enroll_in_course(self.subject, self.course_number, self.section, self.netid, self.password)
                self.try_delay(Enroll.success_delay)
                I.available_sections = ""
            self.try_delay(Enroll.failure_delay)

    def try_delay(self, delay):
        current_time = datetime.now()
        delta_time = (current_time.timestamp() - self.last_run_time.timestamp()) * 1000
        time_to_delay = (delay - delta_time)//1000
        if time_to_delay > 0:
            print("Delaying Script for {} seconds".format(time_to_delay))
            sleep(time_to_delay)
