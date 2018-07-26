from I import I
from datetime import datetime
from time import sleep
class Enroll:
    delay = 10 * 1000 # Milliseconds
    def __init__(self, notify = None, term = None, subject = None, course_numbe = None, section = None):
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
                self.notify.send_email(I.available_sections)
                self.notify.send_text(I.available_sections)
            self.try_delay()

    def try_delay(self):
        current_time = datetime.now()
        delta_time = (current_time.timestamp() - self.last_run_time.timestamp) * 1000
        time_to_delay = Enroll.delay - delta_time
        if time_to_delay > 0:
            sleep(time_to_delay)
