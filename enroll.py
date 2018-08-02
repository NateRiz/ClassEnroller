from I import I
from datetime import datetime
from time import sleep
class Enroll:
    success_delay = 45 * 60 * 1000
    failure_delay = 10 * 1000 # Milliseconds
    def __init__(self, notify = None, term = None, subject = None, course_number = None, section = None):
        self.last_run_time = datetime.now()
        self.notify = notify
        self.term = term
        self.subject = subject
        self.course_number = course_number
        self.section = section

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
                I.add_to_planner()
                I.enroll_in_course(subject, course_number, section)
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
