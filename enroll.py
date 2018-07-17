from I import I

class Enroll:

    def __init__(self, subject=None, course_number=None, section = None):
        self.subject = subject
        self.course_number = course_number
        self.section = section

    def main_loop(self):
        I.go_to_url("https://schedule.msu.edu/")
        I.search_for_course(self.subject, self.course_number)
        I.check_for_space_in_sections(self.section)
        I.close_driver()
