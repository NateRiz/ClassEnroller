

class Enroll:
    def __init__(self, i):
        self.i = i

    def main_loop(self):
        self.i.go_to_url("https://schedule.msu.edu/")
        self.i.should_see("Search for Courses")
        self.i.select_from_dropdown("Term",self.term)
        self.i.select_from_dropdown("Subject",self.subject)
        self.i.fill_field("Course Number", self.course_number)
        self.i.click("Find Courses")
